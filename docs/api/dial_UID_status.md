# Dial Information

{{ api_table('Retrieve dial information', 'dial/{DIAL_UID}/status', 'GET', ['key']) }}

Retrieve status information for `DIAL_UID`.


!!! note annotate "Note"

    API key needs to have appropriate access to target dial.

---

## Example usage

Retrieve information for a dial with UID `3E0075000650564139323920`

{{ usage_api_macro('dial/3E0075000650564139323920/status', 'GET', {'key':'...'}) }}


Response is a JSON object

```json
{
    "status": "ok",
    "message": "",
    "data": {
        "index": "10",
        "uid": "3E0075000650564139323920",
        "dial_name": "GPU",
        "value": 6,
        "rgbw": [
            39,
            11,
            17,
            0
        ],
        "easing": {
            "dial_step": 20,
            "dial_period": 50,
            "backlight_step": 20,
            "backlight_period": "50"
        },
        "fw_hash": "4a30e9c73d5cb2fad377f33fe19ea25c35d25394",
        "fw_version": "20231006",
        "hw_version": "KaranovicResearch/Hub_and_Dial_G050",
        "protocol_version": "v1",
        "backlight": {
            "red": 39,
            "green": 11,
            "blue": 17,
            "white": 0
        },
        "image_file": "img_3E0075000650564139323920",
        "update_deadline": 1699674582.9629712,
        "value_changed": false,
        "backlight_changed": false,
        "image_changed": false
    }
}
```

---


