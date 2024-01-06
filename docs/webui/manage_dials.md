# Manage Dials


<figure markdown>
  ![VU Dials Web UI](../images/webui_dial_settings.png#only-light){ width="800" } ![VU Dials Web UI](../images/webui_dial_settings_dark.png#only-dark){ width="800" }
  <figcaption>Dial Settings Page</figcaption>
</figure>


### Dial Settings

This page gives you more information about the selected dial as well as the option to view current dial image, change dial name, identify dial and set dial behavior.


### Dial information

Section header shows dial name that is used to easily identify each dial in the system.

It also includes a table that shows some basic information about the dial

| Cell | Value | Description
| :---- | :---- | :----
| Dial status | `Online` / `Offline` | Shows if dial is currently present in the system |
| Dial UID | `UID` | Unique identifier that was assigned to this dial during manufacturing |
| Dial generation | `VU1` | What is the generation/configuration of this dial. |
| Dial type | `HUB+Dial` / `Dial` | Identifies if this dial is acting as `dial and hub` or `dial` |
| Firmware version | `Firmware timestamp` | Flag indicating firmware version |
| Firmware build | `build hash` | Firmware build hash  |
| Hardware revision | `hardware stamp` | Flag indicating hardware and firmware configuration |
| Protocol version | `v1` | Indicates which VU protocol(s) this hardware supports |
| Needle update period | `x ms` | How often (in `ms`) does the dial value change |
| Max needle step per period | `x %` | How much (in `%`) can the dial value change per each period |
| Backlight update period | `x ms` | How often (in `ms`) does the backlight change |
| Max backlight step per period | `x %` | How much (in `%`) can the backlight value change per each period |

!!! Note
    Dial/backlight `update period` and `max step value per period` define the *behaviour* of the dial.
    These can be fine tuned to allow the dial to be very responsive or to gently change between values.
    You can read these as
    > "Every `[update period]` milliseconds the dial value/backlight can change by maximum of `[step per period]` percent.

### Dial background

This section shows image that is currently displayed on the dial e-ink display.


### Set dial name

Here you can assign a name to the dial.

By default, dials will not have the name set.


### Identify dial

Since dials do not come with a name assigned and only have UID. It is convenient to have a way to identify a physical dial that you are configuring.

You can click on `Red`, `Green`, `Blue` and the dials backlight will be set to that color and also nedle will be set to `50%` value. This can come in handy to identify which dial you are currently configuring.

### Dial behaviour

These are default presets that allow you to quickly change dial *behaviour*.
Dial *behaviour* is defined by a `update period` and `maximum step`. This determines how often the dial value or backlight will update and also what is the maximum change it can make between each period.


| Preset | Values | Description
| :---- | :---- | :----
| Responsive | Indicator `50ms/20%`<br>Backlight `50ms/20%` | Dial indicator and backlight will change values rapidly. <br>Dial indicator has tiny but non-negligible mass. When there is a large dial value change, indicator can overshoot and then undershoot couple of times (oscillate) due to indicators mass.  |
| Balanced |  Indicator `50ms/5%`<br>Backlight `50ms/10%` | Dial indicator and backlight will change relatively fast but the dial indicator should not oscillate too much on large value changes. |
| Smooth |  Indicator `50ms/1%`<br>Backlight `50ms/5%` | Dial indicator and backlight will change gradually. This gives the effect that backlight is slowly fading between colors and the value indicator will move smoothly between values. |


!!! Note
    These are presets defined for convenience and as a quick demo for users to try out.
    Each application driving the dial can change these values individually and for each individual dial at any time and to whichever value the app/end-user requires.


