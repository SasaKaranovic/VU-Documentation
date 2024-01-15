# Set dial name

{{ api_table('Set dial name', 'dial/{DIAL_UID}/image/get', 'GET', ['key', 'name']) }}

Each VU dial has a unique ID (UID) that uniquely identifies each dial.
These are very helpful internally, but they can be hard to consume by humans.

Each dial also has a `friendly name` or `name` that can be assigned to each dial.
This is helpful because it allows easy identification of each dial.


!!! note annotate "Note"

    Dial name can be used to designate what that dial is showing ie `CPU Load` or it can be used to indicate dial's position in your setup ie `Top right`.

    Dial name is only used for easier 'human' identification of each dial and server will allow you to name them to whatever your wish.

    You can have empty or duplicate dial names... but you really shouldn't.

---

## Example usage

Set/rename dial with UID `3E0075000650564139323920` to `CPU Load`

{{ usage_api_macro('dial/3E0075000650564139323920/set', 'POST', {'key':'...', 'name':'CPU Load'}) }}


Response is a JSON object

``` json
{
    "status": "ok",
    "message": "",
    "data": null
}
```

---


