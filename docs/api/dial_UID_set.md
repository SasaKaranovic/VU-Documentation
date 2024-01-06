# Set dial value

{{ api_table('Set dial value', 'dial/{DIAL_UID}/set', 'GET', ['key', 'value']) }}

Set dial indicator (needle) to desired value.

## Query Parameters

### Key

API key used to authenticate this request

### Value

Desired dial value (`0-100`)

Value of `0` will set the dial indicator (needle) to the left most position
Value of `100` will set the dial indicator (needle) to the right most position


## Example usage

Set value to `30%` for dial with UID `3E0075000650564139323920`

{{ usage_api_macro('dial/3E0075000650564139323920/set', 'GET', {'key':'...', 'value': 30}) }}


Response is a JSON object

```json
{
    "status": "ok",
    "message": "Update queued",
    "data": null
}
```

---


!!! note annotate "Note"

    For completeness and transparency, there is an additional route (`/setRaw`) that allows for setting `RAW` dial value that can be in the range `0-2048`.
    However this method circumvents both calibration and easing configuration.
    Therefore it should not be used.
