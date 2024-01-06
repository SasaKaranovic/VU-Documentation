# Dial backlight

{{ api_table('Set dial backlight', 'dial/{DIAL_UID}/backlight', 'GET', ['key', 'red', 'green', 'blue']) }}

Set the RGB backlight of the dial `{DIAL_UID}` to desired value.

Each channel (`red`, `green`, `blue`) can be set to any value in the `0-100` range where `0` represents fully off and `100` represents fully on.


!!! note annotate "Color accuracy"

    VU1 dials have RGB backlight but the color accuracy is not calibrated.
    Also the backlight range is `0-100%` instead of more common `0-255` range.
    You can play around with different values to find correct color.


---

## Example usage

Set backlight of dial `3E0075000650564139323920` to `50% RED`, `20% GREEN` and `40% BLUE`

{{ usage_api_macro('dial/{DIAL_UID}/backlight', 'GET', {'key':'...', 'red':50, 'green':20, 'blue':40}) }}

Response is a JSON object

```json
{
    "status": "ok",
    "message": "Update queued",
    "data": null
}
```
---


