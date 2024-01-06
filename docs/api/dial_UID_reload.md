# Reload hardware info

{{ api_table('Reload HW information', 'dial/{DIAL_UID}/reload', 'GET', ['key']) }}

API route used to retrieve list of available dials.


!!! note annotate "Note"

    The server will return only the dials that are available for the API key that was used to make the call.

---

## Example usage

Force retrieve hardware information for dial with UID `3E0075000650564139323920`

{{ usage_api_macro('dial/3E0075000650564139323920/reload', 'GET', {'key':'...'}) }}

Response is a JSON object

``` json
{
    "status": "ok",
    "message": "",
    "data": {
        "index": "10",
        "uid": "3E0075000650564139323920",
        "dial_name": "GPU Usage",
        "value": 5,
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
            "backlight_period": 50
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
        "image_file": "C:\\Users\\Sasa\\Desktop\\git\\StreaCom\\GaugeServer\\upload\\img_3E0075000650564139323920",
        "update_deadline": 1699686054.8635087,
        "value_changed": true,
        "backlight_changed": false,
        "image_changed": false,
        "dial_build_hash": "4a30e9c73d5cb2fad377f33fe19ea25c35d25394",
        "dial_fw_version": "20231006",
        "dial_hw_version": "KaranovicResearch/Hub_and_Dial_G050",
        "dial_protocol_version": "v1",
        "easing_dial_step": 20,
        "easing_dial_period": 50,
        "easing_backlight_step": 20,
        "easing_backlight_period": 50
    }
}
```

---

!!! warning annotate "Force reload"

    This API call will force server to re-interrogate dial information.
    You should avoid unnecessary re-reading of dial information.
    Dial information is cached on the server side in the dial database and can be retrieved using `Dial Information` call.
