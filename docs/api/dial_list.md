# Dial List

{{ api_table('Retrieve Dial List', 'dial/list', 'GET', ['key']) }}

API route used to retrieve list of available dials.


!!! note annotate "Note"

    The server will return only the dials that are available for the API key that was used to make the call.

---

## Example usage

{{ usage_api_macro('dial/list', 'GET', {'key':'...'}) }}

Response is a JSON object

``` json
{
    "status": "ok",
    "message": "",
    "data": [
        {
            "uid": "590056000650564139323920",
            "dial_name": "CPU (hub)",
            "value": 31,
            "backlight": {
                "red": 39,
                "green": 3,
                "blue": 39
            },
            "image_file": "img_590056000650564139323920"
        },
        {
            "uid": "4C0065000650564139323920",
            "dial_name": "MEM",
            "value": 40,
            "backlight": {
                "red": 39,
                "green": 3,
                "blue": 39
            },
            "image_file": "img_4C0065000650564139323920"
        },
        {
            "uid": "3E0075000650564139323920",
            "dial_name": "GPU",
            "value": 16,
            "backlight": {
                "red": 39,
                "green": 3,
                "blue": 39
            },
            "image_file": "img_3E0075000650564139323920"
        },
        {
            "uid": "550075000650564139323920",
            "dial_name": "NET",
            "value": 2,
            "backlight": {
                "red": 39,
                "green": 11,
                "blue": 17
            },
            "image_file": "img_550075000650564139323920"
        }
    ]
}
```

---


