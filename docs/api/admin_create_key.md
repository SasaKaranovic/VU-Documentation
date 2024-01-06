# Create API key

{{ api_table('Create API key', 'admin/keys/create', 'POST', ['admin_key', 'name', 'dials']) }}


## Create API key

New API key can be created through API using key that has privileged access or through [Web UI](../webui/manage_keys.md).


## Example usage

New API key can be created through API call.


| Cell name | Example value | Description |
| :-------- | :--------     | :--------   |
| `name` | "SK Demo Key" | Human readable API key name. Used to easily identify key. |
| `dials` | `3C0037001150303352313520;3C0037001150303452313521` | List of dials that this API key should have access too. Use `;` as the dial UID separator. |


{{ usage_api_macro('admin/keys/create', 'POST', {'admin_key':'...', 'name': 'SK Demo Key', 'dials': '3C0037001150303352313520;3C0037001150303452313521'}) }}

Response is JSON object

``` json
{
    "status": "ok",
    "message": "",
    "data": "hc46e1pukyf8ws7b"
}
```

Data field contains the value of the newly created API key.


!!! Note
    This operation can only be performed with an API key that has a privileged access (master key).
