# Get easing configuration

{{ api_table('Retrieve Easing Configuration', 'dial/{DIAL_UID}/easing/get', 'GET', ['key']) }}


## Dial behaviour

For each dial multiple parameters can be configured:

- How often does the dial indicator change value and what is the maximum step it can make for that period.
- How often does the dial backlight change and what is the maximum allowed backlight change for that period.

These parameters can be configured using [set dial easing](./dial_UID_easing_dial.md) and [set backlight easing](./dial_UID_easing_backlight.md) respectively.

All of these parameters define the dial *behaviour* or how does the dial "look and feel".

It is possible to query the dial to retrieve current configuration of these parameters. This can be used to verify that requested values have been applied or to inspect what is the current dial behaviour.
Also this information and more is available through [dial status](./dial_UID_status.md) API call.

## Example usage

If we want to inspect what is the current easing configuration of dial with UID `3E0075000650564139323920` we would send the following HTTP request :

{{ usage_api_macro('dial/3E0075000650564139323920/status', 'GET', {'key':'...'}) }}

Response is a JSON object

``` json
{
    "status": "ok",
    "message": "not supported yet",
    "data": null
}
```
