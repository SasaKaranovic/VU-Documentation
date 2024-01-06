# Update API key

{{ api_table('Update API key', 'admin/keys/update', 'GET', ['admin_key', 'key', 'name', 'dials']) }}

## Update API key

Existing API key can be updated through API using key that has privileged access or through [Web UI](../webui/manage_keys.md).

This route can be used to update API key name and dial access.

## Example usage

We want to update API key with UID `hc46e1pukyf8ws7b` to only have access to dial `3C0037001150303452313521` and rename it to `Weather App API Key`.


{{ usage_api_macro('admin/keys/create', 'GET', {'admin_key':'...', 'key':'hc46e1pukyf8ws7b', 'name': 'Weather App API Key', 'dials': '3C0037001150303452313521'}) }}

Response is JSON object

``` json
{
    "status": "ok",
    "message": "",
    "data": null
}
```


!!! Note
    You need to provide both key `name` and list of `dials` that you wish this key to have access to.


!!! Note
    This operation can only be performed with an API key that has a privileged access (master key).
