# Calibrate dial

{{ api_table('Calibrate dial', 'dial/{DIAL_UID}/calibrate', 'GET', ['key', 'value']) }}

API route to calibrate dial.

!!! note "Factory calibrated"
    All VU dials come pre-calibrated from the factory!


## How to calibrate a dial

Query Parameters `value` can be any integer from `0` to `2048`.

We are looking for a `value` for which dial indicator (needle) will be perfectly vertical.

Calibration process:

1. Send calibration `value` (ie `600`)
2. Dial will move the indicator
3. Check the position of the indicator
4a. If dial indicator is leaning towards left side, go to step 1. and increase the value
4b. If dial indicator is leaning towards right side, go to step 1. and decrease the value
5. Repeat steps 1-4 until dial indicator is perfectly vertical

!!! warning "No undo"
    Dial does not store previous calibration values.
    Sending new calibration value will overwrite the previous value.

!!! warning "Caution"
    All dials come pre-calibrated from the factory.
    You should never have to re calibrate them.

---

## Example usage

Calibrate dial `3E0075000650564139323920` to value `600`

{{ usage_api_macro('dial/3E0075000650564139323920/calibrate', 'GET', {'key':'...', 'value': 600}) }}

Response is a JSON object

``` json
{
    "status": "ok",
    "message": "Update queued",
    "data": null
}
```

---


