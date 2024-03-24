# Get dial image

{{ api_table('Get dial image', 'dial/{DIAL_UID}/image/get', 'GET', ['key']) }}

Retrieve image that is currently displayed on the dial `{DIAL_UID}`.


---

## Example usage

Retrieve image that is displayed on the dial with UID `3E0075000650564139323920`

{{ usage_api_macro('dial/3E0075000650564139323920/image/get', 'GET', {'key':'...'}) }}

Response is a raw image file.
Server will signal content type as `"Content-Type" : "image/png"`.


!!! note annotate "Note"

    This method is used to retrieve the image that target dial's e-ink display is showing.
    It can be used to easily keep UI in sync with the dial.

---

