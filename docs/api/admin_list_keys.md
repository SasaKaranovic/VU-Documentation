# List API Keys

{{ api_table('List API keys', 'admin/keys/list', 'GET', ['admin_key']) }}

## API List

This API route returns the list of available API keys.

JSON response will return `data` key that contains all available API keys.

| Cell name | Example value | Description |
| :-------- | :--------     | :--------   |
| `key_name` | "SK Demo Key" | Human readable API key name. Used to easily identify key. |
| `key_uid` | `hc46e1pukyf8ws7b` | This is the API key. This value is shared with application to allow access to API server.
| `dials` | `[ "590056000650564139323920", "4C0065000650564139323920", "3E0075000650564139323920", "550075000650564139323920" ]` | List of dial UIDs that this API key has access to. |


## Example usage

List of available API keys can be retrieved by sending the following API request

{{ usage_api_macro('admin/keys/list', 'GET', {'admin_key':'...'}) }}

Response is JSON object

``` json
{
    "status": "ok",
    "message": "",
    "data": [
        {
            "key_name": "MASTER_KEY",
            "key_uid": "...",
            "priviledges": 99,
            "dials": []
        },
        {
            "key_name": "SK Demo Key",
            "key_uid": "hc46e1pukyf8ws7b",
            "priviledges": 1,
            "dials": [
                "590056000650564139323920",
                "4C0065000650564139323920",
                "3E0075000650564139323920",
                "550075000650564139323920"
            ]
        }
    ]
}
```

!!! Note
    This operation can only be performed with an API key that has a privileged access (master key).
