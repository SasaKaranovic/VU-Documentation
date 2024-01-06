# Dial easing

{{ api_table('Set dial easing', 'dial/{DIAL_UID}/easing/dial', 'GET', ['key', 'period', 'step']) }}

When value of the dial changes, VU dials will not instantly move the dial indicator (needle) to that value.
Instead VU dial will store that value internally and gradually over time move the dial indicator towards that value.

## Why have this feature?

Historically analog VU dials behaved differently depending on what value they are displaying and how the driving circuit is designed.

For large value changes, dial indicator can overshoot or undershoot the value and even oscillate for a few milliseconds. This is the "authentic" VU indicator look and feel.
But for some application maybe you want the needle to move more gradually or allow it to oscillate and overshoot but not too much.

We could have easily picked the *Goldilocks[^1] behavior* of the dial that looks good and hard-code it for everyone.
But we did not want to prescribe how end-user has to use VU dials and how they *behave*.

Anything that can be configured, we allowed the the end-user to configure what they feel is best for them.

Depending on what VU dials are being used for, maybe you want the dial to be very responsive and immediately jump to the value as soon as it changes. Or maybe you want them to smoothly *glide* from value to value.


## Configure dial *behavior*

There are two parameters that define how fast or slow the dial indicator will update

| Parameter | Unit | Default | Description |
| :-------- | :-------- | :-------- | :-------- |
| Update period | Milliseconds | `50ms` | How often can the dial indicator change value. |
| Maximum step | Percent | `5%` | What is the maximum allowed change of the dial indicator for each update period |

Lower period value means indicator updates more often.
Higher period value means indicator updates less often.

Lower step value means smaller dial indicator changes per update period.
Higher step value means larger dial indicator changes per update period.

## Example usage

We want to configure dial `3E0075000650564139323920` so that every `50 milliseconds` it can move dial indicator by maximum of `5%`.

This means our `period` is `50` and step is `5`.

{{ usage_api_macro('dial/3E0075000650564139323920/status', 'GET', {'key':'...', 'period':50, 'step':5}) }}

Response is JSON object

``` json
{
    "status": "ok",
    "message": "",
    "data": null
}
```

[^1]:
Not too fast, not too slow. Just the right amount.
Reference to [Goldilocks principle](https://en.wikipedia.org/wiki/Goldilocks_principle){:target="_blank"}
