# Coze Python API SDK

[![PyPI version](https://img.shields.io/pypi/v/cozepy.svg)](https://pypi.org/project/cozepy/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cozepy)
[![codecov](https://codecov.io/github/coze-dev/coze-py/graph/badge.svg?token=U6OKGQXF0E)](https://codecov.io/github/coze-dev/coze-py)

## Introduction

The Coze API SDK for Python is a versatile tool for integrating Coze's open APIs into
your projects.

- Supports all Coze open APIs and authentication APIs
- Supports both synchronous and asynchronous SDK calls
- Optimized for streaming apis, returning Stream and AsyncStream objects
- Optimized for list apis, returning Iterator Page objects
- Features a simple and user-friendly API design for ease of use

## Requirements

Python 3.7 or higher.

## Install

```shell
pip install cozepy
```

## Usage

### Examples

<table>
    <tr>
        <th>Module</th>
        <th>Example</th>
        <th>File</th>
    </tr>
    <tr>
        <td rowspan="5">Auth</td>
        <td>JWT OAuth</td>
        <td><a href="./examples/auth_oauth_jwt.py">examples/auth_oauth_jwt.py</a></td>
    </tr>
    <tr>
        <td>Web OAuth</td>
        <td><a href="./examples/auth_oauth_web.py">examples/auth_oauth_web.py</a></td>
    </tr>
    <tr>
        <td>PKCE OAuth</td>
        <td><a href="./examples/auth_oauth_pkce.py">examples/auth_oauth_pkce.py</a></td>
    </tr>
    <tr>
        <td>Device OAuth</td>
        <td><a href="./examples/auth_oauth_device.py">examples/auth_oauth_device.py</a></td>
    </tr>
    <tr>
        <td>Personal Access Token</td>
        <td><a href="./examples/auth_pat.py">examples/auth_pat.py</a></td>
    </tr>
    <tr>
        <td rowspan="4">Websockets</td>
        <td>Audio Speech by Websocket</td>
        <td><a href="./examples/websockets_audio_speech.py">examples/websockets_audio_speech.py</a></td>
    </tr>
    <tr>
        <td>Audio Transcription by Websocket</td>
        <td><a href="./examples/websockets_audio_transcriptions.py">examples/websockets_audio_transcriptions.py</a></td>
    </tr>
    <tr>
        <td>Audio Chat by Websocket</td>
        <td><a href="./examples/websockets_chat.py">examples/websockets_chat.py</a></td>
    </tr>
    <tr>
        <td>Audio Chat Realtime by Websocket</td>
        <td><a href="./examples/websockets_chat_realtime_gui.py">examples/websockets_chat_realtime_gui.py</a></td>
    </tr>
    <tr>
        <td rowspan="7">Bot Chat</td>
        <td>Bot Chat with Steam</td>
        <td><a href="./examples/chat_stream.py">examples/chat_stream.py</a></td>
    </tr>
    <tr>
        <td>Bot Chat without Steam</td>
        <td><a href="./examples/chat_no_stream.py">examples/chat_no_stream.py</a></td>
    </tr>
    <tr>
        <td>Bot Chat with Conversation</td>
        <td><a href="./examples/chat_conversation_stream.py">examples/chat_conversation_stream.py</a></td>
    </tr>
    <tr>
        <td>Bot Chat with Image</td>
        <td><a href="./examples/chat_multimode_stream.py">examples/chat_multimode_stream.py</a></td>
    </tr>
    <tr>
        <td>Bot Chat with Audio</td>
        <td><a href="./examples/chat_simple_audio.py">examples/chat_simple_audio.py</a></td>
    </tr>
    <tr>
        <td>Bot Chat with Audio One-One</td>
        <td><a href="./examples/chat_oneonone_audio.py">examples/chat_oneonone_audio.py</a></td>
    </tr>
    <tr>
        <td>Bot Chat With Local Plugin</td>
        <td><a href="./examples/chat_local_plugin.py">examples/chat_local_plugin.py</a></td>
    </tr>
    <tr>
        <td rowspan="5">Workflow Run & Chat</td>
        <td>Workflow Run with Stream</td>
        <td><a href="./examples/workflow_stream.py">examples/workflow_stream.py</a></td>
    </tr>
    <tr>
        <td>Workflow Run without Stream</td>
        <td><a href="./examples/workflow_no_stream.py">examples/workflow_no_stream.py</a></td>
    </tr>
    <tr>
        <td>Workflow Async Run & Fetch</td>
        <td><a href="./examples/workflow_async.py">examples/workflow_async.py</a></td>
    </tr>
    <tr>
        <td>Workflow Chat with Stream</td>
        <td><a href="./examples/workflow_chat_stream.py">examples/workflow_chat_stream.py</a></td>
    </tr>
    <tr>
        <td>Workflow chat with Image and Stream</td>
        <td><a href="./examples/workflow_chat_multimode_stream.py">examples/workflow_chat_multimode_stream.py</a></td>
    </tr>
    <tr>
        <td rowspan="2">Conversation</td>
        <td>Conversation</td>
        <td><a href="./examples/conversation.py">examples/conversation.py</a></td>
    </tr>
    <tr>
        <td>List Conversation</td>
        <td><a href="./examples/conversation_list.py">examples/conversation_list.py</a></td>
    </tr>
    <tr>
        <td rowspan="1">Dataset</td>
        <td>Create Dataset</td>
        <td><a href="./examples/dataset_create.py">examples/dataset_create.py</a></td>
    </tr>
    <tr>
        <td rowspan="1">Audio</td>
        <td>Audio Example by HTTP</td>
        <td><a href="./examples/audio.py">examples/audio.py</a></td>
    </tr>
    <tr>
        <td rowspan="1">Bot</td>
        <td>Publish Bot</td>
        <td><a href="./examples/bot_publish.py">examples/bot_publish.py</a></td>
    </tr>
    <tr>
        <td rowspan="1">File</td>
        <td>Upload File</td>
        <td><a href="./examples/files_upload.py">examples/files_upload.py</a></td>
    </tr>
    <tr>
        <td rowspan="1">template</td>
        <td>Duplicate Template</td>
        <td><a href="./examples/template_duplicate.py">examples/template_duplicate.py</a></td>
    </tr>
    <tr>
        <td rowspan="1">User</td>
        <td>Get Current User</td>
        <td><a href="./examples/users_me.py">examples/users_me.py</a></td>
    </tr>
    <tr>
        <td rowspan="1">Workspace</td>
        <td>List Workspaces</td>
        <td><a href="./examples/workspace.py">examples/workspace.py</a></td>
    </tr>
    <tr>
        <td rowspan="3">Other</td>
        <td>Timeout Config</td>
        <td><a href="./examples/timeout.py">examples/timeout.py</a></td>
    </tr>
    <tr>
        <td>Log Config</td>
        <td><a href="./examples/log.py">examples/log.py</a></td>
    </tr>
    <tr>
        <td>Exception Usage</td>
        <td><a href="./examples/exception.py">examples/exception.py</a></td>
    </tr>
</table>

### Initialize the Coze client

Firstly, you need to access https://www.coze.com/open/oauth/pats (for the cn environment,
visit https://www.coze.cn/open/oauth/pats).

Click to add a new token. After setting the
appropriate name, expiration time, and permissions, click OK to generate your personal
access token.

Please store it in a secure environment to prevent this personal access
token from being disclosed.

```python
import os

from cozepy import Coze, TokenAuth, COZE_COM_BASE_URL

# Get an access_token through personal access token or oauth.
coze_api_token = os.getenv("COZE_API_TOKEN")
# The default access is api.coze.com, but if you need to access api.coze.cn,
# please use base_url to configure the api endpoint to access
coze_api_base = os.getenv("COZE_API_BASE") or COZE_COM_BASE_URL

coze = Coze(auth=TokenAuth(coze_api_token), base_url=coze_api_base)
```

coze api access_token can also be generated via the OAuth App. For details, refer to:

- [web-oauth-app](https://github.com/coze-dev/coze-py?tab=readme-ov-file#web-oauth-app)
- [jwt-oauth-app](https://github.com/coze-dev/coze-py?tab=readme-ov-file#jwt-oauth-app)
- [pkce-oauth-app](https://github.com/coze-dev/coze-py?tab=readme-ov-file#pkce-oauth-app)
- [device-oauth-app](https://github.com/coze-dev/coze-py?tab=readme-ov-file#device-oauth-app)

### Chat

Create a bot instance in Coze, copy the last number from the web link as the bot's ID.

#### Non-stream Chat

To simplify the call, the SDK provides a wrapped function to complete non-streaming chat,
polling, and obtaining the messages of the chat. Developers can use create_and_poll to
simplify the process.

```python
import os

from cozepy import Coze, TokenAuth, Message, ChatStatus

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

chat_poll = coze.chat.create_and_poll(
    # id of bot
    bot_id='bot_id',
    # id of user, Note: The user_id here is specified by the developer, for example, it can be the
    # business id in the developer system, and does not include the internal attributes of coze.
    user_id='user_id',
    # user input
    additional_messages=[Message.build_user_question_text("How are you?")]
)
for message in chat_poll.messages:
    print(message.content, end="")

if chat_poll.chat.status == ChatStatus.COMPLETED:
    print()
    print("token usage:", chat_poll.chat.usage.token_count)
```

#### Stream Chat

Call the coze.chat.stream method to create a chat. The create method is a streaming
chat and will return a Chat Iterator. Developers should iterate the iterator to get
chat event and handle them.

```python
import os

from cozepy import Coze, TokenAuth, Message, ChatEventType

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

# The return values of the streaming interface can be iterated immediately.
for event in coze.chat.stream(
        # id of bot
        bot_id='bot_id',
        # id of user, Note: The user_id here is specified by the developer, for example, it can be the
        # business id in the developer system, and does not include the internal attributes of coze.
        user_id='user_id',
        # user input
        additional_messages=[Message.build_user_question_text("How are you?")]
):
    if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
        print(event.message.content, end="")

    if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
        print()
        print("token usage:", event.chat.usage.token_count)
```

### Bots

You can create, update, publish and get the list of bots via api.

```python
import os
from cozepy import Coze, TokenAuth

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

# retrieve bot info
bot = coze.bots.retrieve(bot_id='bot id')

# list bot list
# open your workspace, browser url will be https://www.coze.com/space/<this is workspace id>/develop
# copy <this is workspace id> as workspace id
bots_page = coze.bots.list(space_id='workspace id', page_num=1)
bots = bots_page.items

# create bot
bot = coze.bots.create(
    # id of workspace, open your workspace, browser url will be https://www.coze.com/space/<this is workspace id>/develop
    # copy <this is workspace id> as workspace id
    space_id='workspace id',
    # name of bot
    name='bot name',
    # description of bot
    description='bot description',
)

# update bot info
coze.bots.update(
    # id of workspace
    bot_id='bot id',
    # name of bot
    name='bot name',
    # description of bot
    description='bot description',
)

# delete bot
bot = coze.bots.publish(bot_id='bot id')
```

### Conversations

Users can create conversations, and conduct conversations, inquire about messages,
etc. on conversations.

```python
import os
from cozepy import Coze, TokenAuth, Message, MessageContentType

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

# If there is a need to build a context with user-assistant question-and-answer pairs,
# a conversation can be created through the create interface.
conversation = coze.conversations.create(
    messages=[
        # user question: how are you?
        Message.build_user_question_text('who are you?'),
        # assistant answer: I am Coze Bot.
        Message.build_assistant_answer('I am Coze Bot.')
    ],
)

# retrieve conversation
conversation = coze.conversations.retrieve(conversation_id=conversation.id)

# append message to conversation
message = coze.conversations.messages.create(
    # id of conversation
    conversation_id=conversation.id,
    content='how are you?',
    content_type=MessageContentType.TEXT,
)

# retrieve message
message = coze.conversations.messages.retrieve(conversation_id=conversation.id, message_id=message.id)

# update message
coze.conversations.messages.update(
    conversation_id=conversation.id,
    message_id=message.id,
    content='hey, how are you?',
    content_type=MessageContentType.TEXT,
)

# delete message
coze.conversations.messages.delete(conversation_id=conversation.id, message_id=message.id)

# list messages
message_list = coze.conversations.messages.list(conversation_id=conversation.id)
```

### Files

Coze enables users to upload pictures and files. The uploaded pictures and files
can be utilized in the bot avatar and multimodal conversations.

```python
import os
from pathlib import Path
from cozepy import Coze, TokenAuth

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

# upload file
file = coze.files.upload(file=Path('/filepath'))

# retrieve file info
coze.files.retrieve(file_id=file.id)
```

### Workflows

Coze also enables users to directly invoke the workflow.

#### Non-stream workflow run

```python
import os
from cozepy import Coze, TokenAuth, Stream, WorkflowEvent, WorkflowEventType

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

result = coze.workflows.runs.create(
    # id of workflow
    workflow_id='workflow id',
    # params
    parameters={
        'input_key': 'input value',
    }
)
```

#### Stream workflow run

The returned result of the streaming interface is an iterator and can be directly iterated.

When the workflow incorporates question-and-answer nodes, the streaming interface will
return the INTERRUPT event.

Users should call the resume interface to submit the results of the question-and-answer.

The return value of resume remains an iterator, so recursive processing might be necessary here.

```python
import os

from cozepy import Coze, TokenAuth, Stream, WorkflowEvent, WorkflowEventType

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))


def handle_workflow_iterator(stream: Stream[WorkflowEvent]):
    for event in stream:
        if event.event == WorkflowEventType.MESSAGE:
            print('got message', event.message)
        elif event.event == WorkflowEventType.ERROR:
            print('got error', event.error)
        elif event.event == WorkflowEventType.INTERRUPT:
            # Users should call the resume interface to submit the results of the question-and-answer
            handle_workflow_iterator(coze.workflows.runs.resume(
                workflow_id='workflow id',
                event_id=event.interrupt.interrupt_data.event_id,
                resume_data='hey',
                interrupt_type=event.interrupt.interrupt_data.type,
            ))


handle_workflow_iterator(coze.workflows.runs.stream(
    # id of workflow
    workflow_id='workflow id',
    # params
    parameters={
        'input_key': 'input value',
    }
))
```

### Knowledge

```python
import os
from cozepy import Coze, TokenAuth, DocumentBase, DocumentSourceInfo, DocumentChunkStrategy, DocumentUpdateRule

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

# create knowledge documents by local_file
documents = coze.knowledge.documents.create(
    # id of dataset
    dataset_id='dataset id',
    # document data
    document_bases=[
        DocumentBase(
            name='document name',
            source_info=DocumentSourceInfo.build_local_file('local file content')
        )
    ],
    # chunk strategy, needed when first create
    chunk_strategy=DocumentChunkStrategy.build_auto()
)

# create knowledge documents by web_page
documents = coze.knowledge.documents.create(
    # id of dataset
    dataset_id='dataset id',
    # document data
    document_bases=[
        DocumentBase(
            name='document name',
            source_info=DocumentSourceInfo.build_web_page('https://example.com')
        )
    ],
    # chunk strategy, needed when first create
    chunk_strategy=DocumentChunkStrategy.build_auto()
)

# update knowledge document
coze.knowledge.documents.update(
    # id of document
    document_id='document id',
    # name of document
    document_name='name',
    # update rule, current set to no auto-update
    update_rule=DocumentUpdateRule.build_no_auto_update()
)

# delete knowledge document
coze.knowledge.documents.delete(document_ids=['document id'])

# list knowledge documents
paged_documents = coze.knowledge.documents.list(
    # id of dataset
    dataset_id='dataset id',
    page_num=1,
    page_size=10
)
```

### OAuth App

#### Web OAuth App

Firstly, users need to access https://www.coze.com/open/oauth/apps. For the cn environment,
users need to access https://www.coze.cn/open/oauth/apps to create an OAuth App of the type
of Web application.

The specific creation process can be referred to in the document:
https://www.coze.com/docs/developer_guides/oauth_code. For the cn environment, it can be
accessed at https://www.coze.cn/docs/developer_guides/oauth_code.

After the creation is completed, three parameters, namely the client ID, client secret,
and redirect link, can be obtained. For the client secret, users need to keep it securely
to avoid leakage.

```python
import os
from cozepy import Coze, TokenAuth, WebOAuthApp

# client ID
web_oauth_client_id = os.getenv("COZE_WEB_OAUTH_CLIENT_ID")
# client secret
web_oauth_client_secret = os.getenv("COZE_WEB_OAUTH_CLIENT_SECRET")

web_oauth_app = WebOAuthApp(
    client_id=web_oauth_client_id,
    client_secret=web_oauth_client_secret,
)
```

The WebOAuth authorization process is to first generate a coze authorization link and
send it to the coze user requiring authorization.

Once the coze user opens the link, they can see the authorization consent button.

```python
# redirect link
web_oauth_redirect_uri = os.getenv("COZE_WEB_OAUTH_REDIRECT_URI")

# Generate the authorization link and direct the user to open it.
url = web_oauth_app.get_oauth_url(redirect_uri=web_oauth_redirect_uri)
```

After the user clicks the authorization consent button, the coze web page will redirect
to the redirect address configured in the authorization link and carry the authorization
code and state parameters in the address via the query string.

```python
# Open the authorization link in your browser and authorize this OAuth App
# After authorization, you will be redirected to the redirect_uri with a code and state
# You can use the code to get the access token
code = 'mock code'

# After obtaining the code after redirection, the interface to exchange the code for a
# token can be invoked to generate the coze access_token of the authorized user.
oauth_token = web_oauth_app.get_access_token(redirect_uri=web_oauth_redirect_uri, code=code)

# use the access token to init Coze client
coze = Coze(auth=TokenAuth(oauth_token.access_token))

# When the token expires, you can also refresh and re-obtain the token
oauth_token = web_oauth_app.refresh_access_token(oauth_token.refresh_token)
```

#### JWT OAuth App

Firstly, users need to access https://www.coze.com/open/oauth/apps. For the cn environment,
users need to access https://www.coze.cn/open/oauth/apps to create an OAuth App of the type
of Service application.

The specific creation process can be referred to in the document:
https://www.coze.com/docs/developer_guides/oauth_jwt. For the cn environment, it can be
accessed at https://www.coze.cn/docs/developer_guides/oauth_jwt.

After the creation is completed, three parameters, namely the client ID, private key,
and public key id, can be obtained. For the client secret and public key id, users need to
keep it securely to avoid leakage.

```python
import os
from cozepy import Coze, TokenAuth, JWTOAuthApp

# client ID
jwt_oauth_client_id = os.getenv("COZE_JWT_OAUTH_CLIENT_ID")
# private key
jwt_oauth_private_key = os.getenv("COZE_JWT_OAUTH_PRIVATE_KEY")
# public key id
jwt_oauth_public_key_id = os.getenv("COZE_JWT_OAUTH_PUBLIC_KEY_ID")

jwt_oauth_app = JWTOAuthApp(
    client_id=jwt_oauth_client_id,
    private_key=jwt_oauth_private_key,
    public_key_id=jwt_oauth_public_key_id,
)
```

The jwt oauth type requires using private to be able to issue a jwt token, and through
the jwt token, apply for an access_token from the coze service.

The sdk encapsulates this procedure, and only needs to use get_access_token to obtain
the access_token under the jwt oauth process.

```python
# The jwt process does not require any other operations, you can directly apply for a token
oauth_token = jwt_oauth_app.get_access_token(ttl=3600)

# use the access token to init Coze client
coze = Coze(auth=TokenAuth(oauth_token.access_token))

# The jwt oauth process does not support refreshing tokens. When the token expires,
# just directly call get_access_token to generate a new token.
```

#### PKCE OAuth App

PKCE stands for Proof Key for Code Exchange, and it's an extension to the OAuth 2.0 authorization
code flow designed to enhance security for public clients, such as mobile and single-page
applications.

Firstly, users need to access https://www.coze.com/open/oauth/apps. For the cn environment,
users need to access https://www.coze.cn/open/oauth/apps to create an OAuth App of the type
of Mobile/PC/Single-page application.

The specific creation process can be referred to in the document:
https://www.coze.com/docs/developer_guides/oauth_pkce. For the cn environment, it can be
accessed at https://www.coze.cn/docs/developer_guides/oauth_pkce.

After the creation is completed, three parameters, namely the client ID can be obtained.

```python
import os

from cozepy import PKCEOAuthApp

# client ID
pkce_oauth_client_id = os.getenv("COZE_PKCE_OAUTH_CLIENT_ID")
# redirect link
web_oauth_redirect_uri = os.getenv("COZE_WEB_OAUTH_REDIRECT_URI")

pkce_oauth_app = PKCEOAuthApp(client_id=pkce_oauth_client_id)
```

In the pkce oauth process, first, need to select a suitable code_challenge_method.
Coze supports two types: plain and s256.

Then, based on the selected code_challenge_method type, hash the code_verifier into
the code_challenge. Finally, based on the callback address,
code_challenge, and code_challenge_method, an authorization link can be generated.

```python
# In the SDK, we have wrapped up the code_challenge process of PKCE. Developers only need
# to select the code_challenge_method.
code_verifier = "random code verifier"
url = pkce_oauth_app.get_oauth_url(
    redirect_uri=web_oauth_redirect_uri,
    code_verifier=code_verifier,
    code_challenge_method="S256"
)
```

Developers should lead users to open up this authorization link.

When the user consents to the authorization, Coze will redirect with the code to the
callback address configured by the developer, and the developer can obtain this code.

```python
# Open the authorization link in your browser and authorize this OAuth App
# After authorization, you can exchange code_verifier for access token
code = 'mock code'

# After obtaining the code after redirection, the interface to exchange the code for a
# token can be invoked to generate the coze access_token of the authorized user.
oauth_token = pkce_oauth_app.get_access_token(
    redirect_uri=web_oauth_redirect_uri, code=code, code_verifier=code_verifier
)

# use the access token to init Coze client
coze = Coze(auth=TokenAuth(oauth_token.access_token))

# When the token expires, you can also refresh and re-obtain the token
oauth_token = pkce_oauth_app.refresh_access_token(oauth_token.refresh_token)
```

#### Device OAuth App

The OAuth 2.0 device flow, also known as the device authorization grant, is an extension to t
e OAuth 2.0 protocol designed for devices that have limited input capabilities or lack a suitable
browser.

Firstly, users need to access https://www.coze.com/open/oauth/apps. For the cn environment,
users need to access https://www.coze.cn/open/oauth/apps to create an OAuth App of the type
of TVs/Limited Input devices/Command line programs.

The specific creation process can be referred to in the document:
https://www.coze.com/docs/developer_guides/oauth_device_code. For the cn environment, it can be
accessed at https://www.coze.cn/docs/developer_guides/oauth_device_code.

After the creation is completed, three parameters, namely the client ID can be obtained.

```python
import os
from cozepy import Coze, TokenAuth, DeviceOAuthApp

# client ID
device_oauth_client_id = os.getenv("COZE_DEVICE_OAUTH_CLIENT_ID")

device_oauth_app = DeviceOAuthApp(client_id=device_oauth_client_id)
```

In the device oauth authorization process, developers need to first call the interface
of Coze to generate the device code to obtain the user_code and device_code.

Then generate the authorization link through the user_code, guide the user to open the
link, fill in the user_code, and consent to the authorization.

Developers need to call the interface of Coze to generate the token through the device_code.

When the user has not authorized or rejected the authorization, the interface will throw an
error and return a specific error code.

After the user consents to the authorization, the interface will succeed and return the
access_token.

```python
# First, you need to request the server to obtain the device code required in the device auth flow
device_code = device_oauth_app.get_device_code()

# The returned device_code contains an authorization link. Developers need to guide users
# to open up this link.
# open device_code.verification_url
```

The developers then need to use the device_code to poll Coze's interface to obtain the token.

The SDK has encapsulated this part of the code in and handled the different returned error
codes. The developers only need to invoke get_access_token.

```python
try:
    oauth_token = device_oauth_app.get_access_token(
        device_code=device_code.device_code,
        poll=True,
    )
except CozePKCEAuthError as e:
    if e.error == CozePKCEAuthErrorType.ACCESS_DENIED:
        # The user rejected the authorization.
        # Developers need to guide the user to open the authorization link again.
        pass
    elif e.error == CozePKCEAuthErrorType.EXPIRED_TOKEN:
        # The token has expired. Developers need to guide the user to open
        # the authorization link again.
        pass
    else:
        # Other errors
        pass

    raise  # for example, re-raise the error

# use the access token to init Coze client
coze = Coze(auth=TokenAuth(oauth_token.access_token))

# When the token expires, you can also refresh and re-obtain the token
oauth_token = device_oauth_app.refresh_access_token(oauth_token.refresh_token)
```

### Debug

The SDK support returning the logid of the request, which can be used to debug the request.
You can get the logid from the response of the request and submit it to the coze support team for further assistance.

```python
import os
from cozepy import Coze, AsyncCoze, TokenAuth

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

bot = coze.bots.retrieve(bot_id='bot id')
print(bot.response.logid) # support for CozeModel

stream = coze.chat.stream(bot_id='bot id', user_id='user id')
print(stream.response.logid) # support for stream

workspaces = coze.workspaces.list()
print(workspaces.response.logid) # support for paged

messages = coze.chat.messages.list(conversation_id='conversation id', chat_id='chat id')
print(messages.response.logid) # support for list(simple list, not paged)
```


### Async usage

cozepy supports asynchronous calls through `httpx.AsyncClient`.

Just replace the `Coze` client with the `AsyncCoze` client to use all the asynchronous calls of the Coze OpenAPI.

```python
import os
import asyncio

from cozepy import TokenAuth, Message, AsyncCoze

coze = AsyncCoze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))


async def main() -> None:
    chat = await coze.chat.create(
        bot_id='bot id',
        # id of user, Note: The user_id here is specified by the developer, for example, it can be the business id in the developer system, and does not include the internal attributes of coze.
        user_id='user id',
        additional_messages=[
            Message.build_user_question_text('how are you?'),
            Message.build_assistant_answer('I am fine, thank you.')
        ],
    )
    print('chat', chat)


asyncio.run(main())
```

### Streaming usage

Bot chat and workflow run support running in streaming mode.

chat streaming example:

```python
import os
from cozepy import Coze, TokenAuth, ChatEventType, Message

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

stream = coze.chat.stream(
    bot_id='bot id',
    # id of user, Note: The user_id here is specified by the developer, for example, it can be the
    # business id in the developer system, and does not include the internal attributes of coze.
    user_id='user id',
    additional_messages=[
        Message.build_user_question_text('how are you?'),
        Message.build_assistant_answer('I am fine, thank you.')
    ],
)
for event in stream:
    if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
        print('got message delta:', event.message.content)
```

workflow streaming example:

```python
import os
from cozepy import Coze, TokenAuth, Stream, WorkflowEvent, WorkflowEventType

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))


def handle_workflow_iterator(stream: Stream[WorkflowEvent]):
    for event in stream:
        if event.event == WorkflowEventType.MESSAGE:
            print('got message', event.message)
        elif event.event == WorkflowEventType.ERROR:
            print('got error', event.error)
        elif event.event == WorkflowEventType.INTERRUPT:
            handle_workflow_iterator(coze.workflows.runs.resume(
                workflow_id='workflow id',
                event_id=event.interrupt.interrupt_data.event_id,
                resume_data='hey',
                interrupt_type=event.interrupt.interrupt_data.type,
            ))


handle_workflow_iterator(coze.workflows.runs.stream(
    workflow_id='workflow id',
    parameters={
        'input_key': 'input value',
    }
))
```

Asynchronous calls also support streaming mode:

```python
import os
import asyncio

from cozepy import TokenAuth, ChatEventType, Message, AsyncCoze

coze = AsyncCoze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))


async def main():
    stream = coze.chat.stream(
        bot_id='bot id',
        # id of user, Note: The user_id here is specified by the developer, for example, it can be the
        # business id in the developer system, and does not include the internal attributes of coze.
        user_id='user id',
        additional_messages=[
            Message.build_user_question_text('how are you?'),
            Message.build_assistant_answer('I am fine, thank you.')
        ],
    )
    async for event in stream:
        if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
            print('got message delta:', event.message.content)


asyncio.run(main())
```

### Paginator Iterator

The result returned by all list interfaces (both synchronous and asynchronous) is a paginator, which supports iteration.

Take the example of listing the bots in a space to explain the three ways to use the paginator iterator:

#### 1. Not using iterators

```python
import os
from cozepy import Coze, TokenAuth

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

# open your workspace, browser url will be https://www.coze.com/space/<this is workspace id>/develop
# copy <this is workspace id> as workspace id
bots_page = coze.bots.list(space_id='workspace id', page_size=10)
bots = bots_page.items
total = bots_page.total
has_more = bots_page.has_more
```

#### 2. Iterate over the paginator, getting T

```python
import os
from cozepy import Coze, TokenAuth

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

# open your workspace, browser url will be https://www.coze.com/space/<this is workspace id>/develop
# copy <this is workspace id> as workspace id
bots_page = coze.bots.list(space_id='workspace id', page_size=10)
for bot in bots_page:
    print('got bot:', bot)
```

Asynchronous methods also support:

```python
import os
import asyncio

from cozepy import TokenAuth, AsyncCoze

coze = AsyncCoze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))


async def main():
    # open your workspace, browser url will be https://www.coze.com/space/<this is workspace id>/develop
    # copy <this is workspace id> as workspace id
    bots_page = await coze.bots.list(space_id='workspace id', page_size=10)
    async for bot in bots_page:
        print('got bot:', bot)


asyncio.run(main())
```

#### 3. Iterate over the paginator iter_pages to get the next page paginator

```python
import os
from cozepy import Coze, TokenAuth

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))

# open your workspace, browser url will be https://www.coze.com/space/<this is workspace id>/develop
# copy <this is workspace id> as workspace id
bots_page = coze.bots.list(space_id='workspace id', page_size=10)
for page in bots_page.iter_pages():
    print('got page:', page.page_num)
    for bot in page.items:
        print('got bot:', bot)
```

Asynchronous methods also support:

```python
import asyncio
import os

from cozepy import TokenAuth, AsyncCoze

coze = AsyncCoze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))


async def main():
    # open your workspace, browser url will be https://www.coze.com/space/<this is workspace id>/develop
    # copy <this is workspace id> as workspace id
    bots_page = await coze.bots.list(space_id='workspace id', page_size=10)
    async for page in bots_page.iter_pages():
        print('got page:', page.page_num)
        for bot in page.items:
            print('got bot:', bot)


asyncio.run(main())
```

### Config

#### Log Config

coze support config logging level

```python
import logging

from cozepy import setup_logging

# open debug logging, default is warning
setup_logging(level=logging.DEBUG)
```

#### Timeout Config

Coze client is built on httpx, and supports passing a custom httpx.Client when initializing
Coze, and setting a timeout on the httpx.Client

```python
import os

import httpx

from cozepy import COZE_COM_BASE_URL, Coze, TokenAuth, SyncHTTPClient

# Coze client is built on httpx, and supports passing a custom httpx.Client when initializing
# Coze, and setting a timeout on the httpx.Client
http_client = SyncHTTPClient(timeout=httpx.Timeout(
    # 600s timeout on elsewhere
    timeout=600.0,
    # 5s timeout on connect
    connect=5.0
))

# Init the Coze client through the access_token and custom timeout http client.
coze = Coze(auth=TokenAuth(token=os.getenv("COZE_API_TOKEN")),
            base_url=COZE_COM_BASE_URL,
            http_client=http_client
            )
```
