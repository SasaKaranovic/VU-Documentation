# Backlight easing

{{ api_table('Set backlight easing', 'dial/{DIAL_UID}/easing/backlight', 'GET', ['key', 'period', 'step']) }}

When dial backlight changes value, VU dials will not instantly change the backlight color.
Instead VU dial  will start to change each individual `Red`, `Green` and `Blue` channel towards the requested backlight color.


## Why have this feature?

When the backlight value changes, depending on use-case it could be desirable to gradually fade from one color to another. In other cases we might want the backlight color to change very fast.

We could have picked the *Goldilocks[^1] behavior* of the dial that looks good and hard-code it for everyone.
But we did not want to prescribe how end-user has to use VU dials and how they *behave*.

Anything that can be configured, we allowed the the end-user to configure what they feel is best for them.

Depending on what VU dials are being used for, maybe you want the backlight to slowly fade from one color to another. Or maybe you the backlight to quickly transition to the requested color.


## Configure backlight *behavior*

There are two parameters that define how fast or slow the dial backlight will update

| Parameter | Unit | Default | Description |
| :-------- | :-------- | :-------- | :-------- |
| Update period | Milliseconds | `50ms` | How often can the backlight change value. |
| Maximum step | Percent | `5%` | What is the maximum allowed change of the backlight for each update period |

Lower period value means indicator updates more often.
Higher period value means indicator updates less often.

Lower step value means smaller backlight changes per update period.
Higher step value means larger backlight changes per update period.

## Example usage

We want to configure dial `3E0075000650564139323920` so that every `50 milliseconds` it can move dial indicator by maximum of `5%`.

This means our `period` is `50` and step is `5`.

{{ usage_api_macro('dial/3E0075000650564139323920/easing/backlight', 'GET', {'key':'...', 'period':50, 'step':5}) }}

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
