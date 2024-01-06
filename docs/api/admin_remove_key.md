# Remove API key

{{ api_table('Remove API key', 'admin/keys/remove', 'GET', ['admin_key', 'key']) }}

## Remove API key

Existing API key can be removed through API using key that has privileged access or through [Web UI](../webui/manage_keys.md).


## Example usage

Remove API key through API call.


| Cell name | Example value | Description |
| :-------- | :--------     | :--------   |
| `key` | `hc46e1pukyf8ws7b` | UID of the key that we want to remove |


{{ usage_api_macro('admin/keys/remove', 'GET', {'admin_key':'...', 'key': 'hc46e1pukyf8ws7b'}) }}

Response is JSON object

``` json
{
    "status": "ok",
    "message": "",
    "data": null
}
```

!!! Note
    This operation can only be performed with an API key that has a privileged access (master key).
