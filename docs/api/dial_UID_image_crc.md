# Get dial image CRC

{{ api_table('Get dial image CRC', 'dial/{DIAL_UID}/image/crc', 'GET', ['key']) }}

Retrieve CRC32 signature of the image that is currently displayed on the dial `{DIAL_UID}`


---

## Example usage

Retrieve CRC32 of the image that is displayed on the dial with UID `3E0075000650564139323920`

{{ usage_api_macro('dial/3E0075000650564139323920/image/crc', 'GET', {'key':'...'}) }}


Response is a JSON object

```json
{
    "status": "ok",
    "message": "",
    "data": "12E2F173"
}
```
