import abc
import time
from urllib.parse import quote_plus, urlparse

from authlib.jose import jwt
from typing_extensions import Literal

from cozepy.config import COZE_CN_BASE_URL, COZE_COM_BASE_URL
from cozepy.model import CozeModel
from cozepy.request import Requester
from cozepy.util import gen_s256_code_challenge, random_hex


class OAuthToken(CozeModel):
    # The requested access token. The app can use this token to authenticate to the Coze resource.
    access_token: str
    # How long the access token is valid, in seconds (UNIX timestamp)
    expires_in: int
    # An OAuth 2.0 refresh token. The app can use this token to acquire other access tokens after the current access token expires. Refresh tokens are long-lived.
    refresh_token: str = ""
    # fixed: Bearer
    token_type: str = ""


class DeviceAuthCode(CozeModel):
    # device code
    device_code: str
    # The user code
    user_code: str
    # The verification uri
    verification_uri: str
    # The interval of the polling request
    interval: int = 5
    # The expiration time of the device code
    expires_in: int

    @property
    def verification_url(self):
        return f"{self.verification_uri}?user_code={self.user_code}"


class OAuthApp(object):
    def __init__(self, client_id: str, base_url: str, www_base_url: str):
        self._client_id = client_id
        self._base_url = base_url
        self._api_endpoint = urlparse(base_url).netloc
        self._www_base_url = www_base_url
        self._requester = Requester()

    def _get_oauth_url(
        self,
        redirect_uri: str,
        state: str,
        code_challenge: str = None,
        code_challenge_method: str = None,
        workspace_id: str = None,
    ):
        params = {
            "response_type": "code",
            "client_id": self._client_id,
            "redirect_uri": redirect_uri,
            "state": state,
        }
        if code_challenge:
            params["code_challenge"] = code_challenge
            params["code_challenge_method"] = code_challenge_method
        uri = f"{self._get_www_base_url}/api/permission/oauth2/authorize"
        if workspace_id:
            uri = f"{self._get_www_base_url}/api/permission/oauth2/workspace_id/{workspace_id}/authorize"
        return uri + "?" + "&".join([f"{k}={quote_plus(v)}" for k, v in params.items()])

    def _refresh_access_token(self, refresh_token: str) -> OAuthToken:
        url = f"{self._base_url}/api/permission/oauth2/token"
        body = {
            "grant_type": "refresh_token",
            "client_id": self._client_id,
            "refresh_token": refresh_token,
        }
        return self._requester.request("post", url, OAuthToken, body=body)

    @property
    def _get_www_base_url(self) -> str:
        if self._www_base_url:
            return self._www_base_url
        if self._base_url in [COZE_CN_BASE_URL, COZE_COM_BASE_URL]:
            return self._base_url.replace("api", "www")
        return self._base_url


class JWTOAuthApp(OAuthApp):
    """
    JWT OAuth App.
    """

    def __init__(self, client_id: str, private_key: str, public_key_id: str, base_url: str = COZE_COM_BASE_URL):
        """
        :param client_id:
        :param private_key:
        :param public_key_id:
        :param base_url:
        """
        self._client_id = client_id
        self._base_url = base_url
        self._api_endpoint = urlparse(base_url).netloc
        self._token = ""
        self._private_key = private_key
        self._public_key_id = public_key_id
        super().__init__(client_id, base_url, www_base_url="")

    def get_access_token(self, ttl: int) -> OAuthToken:
        """
        Get the token by jwt with jwt auth flow.
        """
        jwt_token = self._gen_jwt(self._api_endpoint, self._private_key, self._client_id, self._public_key_id, 3600)
        url = f"{self._base_url}/api/permission/oauth2/token"
        headers = {"Authorization": f"Bearer {jwt_token}"}
        body = {
            "duration_seconds": ttl,
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        }
        return self._requester.request("post", url, OAuthToken, headers=headers, body=body)

    def _gen_jwt(self, api_endpoint: str, private_key: str, client_id: str, kid: str, ttl: int):
        now = int(time.time())
        header = {"alg": "RS256", "typ": "JWT", "kid": kid}
        payload = {
            "iss": client_id,
            "aud": api_endpoint,
            "iat": now,
            "exp": now + ttl,
            "jti": random_hex(16),
        }
        s = jwt.encode(header, payload, private_key)
        return s.decode("utf-8")


class PKCEOAuthApp(OAuthApp):
    """
    PKCE OAuth App.
    """

    def __init__(self, client_id: str, base_url: str = COZE_COM_BASE_URL, www_base_url: str = ""):
        self._token = ""
        self._requester = Requester()
        super().__init__(
            client_id,
            base_url,
            www_base_url,
        )

    def get_oauth_url(
        self,
        redirect_uri: str,
        state: str,
        code_verifier: str,
        code_challenge_method: Literal["plain", "S256"] = "plain",
        workspace_id: str = None,
    ):
        """
        Get the pkce flow authorized url.

        :param redirect_uri: The redirect_uri of your app, where authentication responses can be sent and received by
        your app. It must exactly match one of the redirect URIs you registered in the OAuth Apps.
        :param state: A value included in the request that is also returned in the token response. It can be a string
        of any hash value.
        :param code_verifier:
        :param code_challenge_method:
        :param workspace_id:
        :return:
        """
        code_challenge = code_verifier if code_challenge_method == "plain" else gen_s256_code_challenge(code_verifier)

        return self._get_oauth_url(
            redirect_uri,
            state,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            workspace_id=workspace_id,
        )

    def get_access_token(self, redirect_uri: str, code: str, code_verifier: str) -> OAuthToken:
        """
        Get the token with pkce auth flow.

        :param redirect_uri:
        :param code_verifier:
        :param code:
        :return:
        """
        url = f"{self._base_url}/api/permission/oauth2/token"
        body = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self._client_id,
            "redirect_uri": redirect_uri,
            "code_verifier": code_verifier,
        }
        return self._requester.request("post", url, OAuthToken, body=body)

    def refresh_access_token(self, refresh_token: str) -> OAuthToken:
        return self._refresh_access_token(refresh_token)


class Auth(abc.ABC):
    """
    This class is the base class for all authorization types.

    It provides the abstract methods for getting the token type and token.
    """

    @property
    @abc.abstractmethod
    def token_type(self) -> str:
        """
        The authorization type used in the http request header.

        eg: Bearer, Basic, etc.

        :return: token type
        """

    @property
    @abc.abstractmethod
    def token(self) -> str:
        """
        The token used in the http request header.

        :return: token
        """

    def authentication(self, headers: dict) -> None:
        """
        Construct the authorization header in the http headers.

        :param headers: http headers
        :return: None
        """
        headers["Authorization"] = f"{self.token_type} {self.token}"


class TokenAuth(Auth):
    """
    The fixed access token auth flow.
    """

    def __init__(self, token: str):
        # TODO: 其他 sdk 实现
        assert isinstance(token, str)
        assert len(token) > 0
        self._token = token

    @property
    def token_type(self) -> str:
        return "Bearer"

    @property
    def token(self) -> str:
        return self._token


class JWTAuth(Auth):
    """
    The JWT auth flow.
    """

    def __init__(
        self,
        client_id: str,
        private_key: str,
        public_key_id: str,
        ttl: int = 7200,
        base_url: str = COZE_COM_BASE_URL,
    ):
        assert isinstance(client_id, str)
        assert isinstance(private_key, str)
        assert isinstance(public_key_id, str)
        assert isinstance(ttl, int)
        assert ttl > 0
        assert isinstance(base_url, str)

        self._client_id = client_id
        self._ttl = ttl
        self._base_url = base_url
        self._token = None
        self._oauth_cli = JWTOAuthApp(self._client_id, private_key, public_key_id, base_url=self._base_url)

    @property
    def token_type(self) -> str:
        return "Bearer"

    @property
    def token(self) -> str:
        token = self._generate_token()
        return token.access_token

    def _generate_token(self):
        if self._token is not None and int(time.time()) < self._token.expires_in:
            return self._token
        self._token = self._oauth_cli.get_access_token(self._ttl)
        return self._token
