# Manage API keys

<figure markdown>
  ![Manage API Keys](../images/webui_api_key.png#only-light){ width="800" } ![Manage API Keys](../images/webui_api_key_dark.png#only-dark){ width="800" }
  <figcaption>API keys list page</figcaption>
</figure>

## What are API keys used for

Each application that interacts with VU Dials API server needs to have a valid API key.

API keys are used to identify and *authenticate*[^1] each application that is trying to communicate with the API server. It is also used by the server to know which API key can interact with which VU dial.

Each API key can have access to one or more dials.


## Creating API key

You should create an API key for each application that you want to allow to interact with VU dials.
It is recommended that you create API key for each individual application.

In order to create a new API key, go to `API Keys page` and click on a `+ Create new API key` button in the top right corner.
The `Create new API key` dialog should appear.

<figure markdown>
  ![Create API Key](../images/webui_api_key_create.png#only-light) ![Create API Key](../images/webui_api_key_create_dark.png#only-dark)
  <figcaption>Create new API key dialog</figcaption>
</figure>

| Field | Description
| :---- | :----
| Key Name | Assign a name to easily identify this key.<br>ie. Name of the application that is going to use this key. |

You can select one or more dials that you wish this API key to have access to. Each key should have access to at least one dial.

Once you click `Create` a new API key will be generated and you can find it on the `API key list` page.

You should take a corresponding `API Key` value from the table and enter it into your application.


## Managing API keys

On the `API keys list` each API key will have a `Settings` button.
You can click on this button to change the name of the key or to
You can change keys name or dial access at any time by clicking on its `Settings` button in the API key list.


## Security

!!! note "Note"
    - Each application should use their own API key.
    - You can create as many API keys as you need.
    - Each API key can have one or more dials assigned to them.

!!! warning "Master API key"
    Every server has a `Master API Key` which has administrative access.
    This key is used by `WebUI` and `VU1 Demo App`.
    You should not share/use this key in any other application.

!!! warning "Untrusted apps"
    For the time being VU Dials API server should be considered as *unsecured*[^1].
    You should not expose access or create/assign API keys to potentially untrusted or malicious applications.


[^1]: VU1 API Server uses `http` protocol which is not secure. Also the implementation of API key sharing/storage does not protect against malicious applications. Therefore it is best not to expose the API server to untrusted/hostile networks.
