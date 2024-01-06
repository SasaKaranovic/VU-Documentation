# Provision new dials

{{ api_table('Provision new dials', 'dial/provision', 'GET', ['admin_key']) }}

## What is provisioning

When new dial is added to the system for the first time it needs to register with the VU hub.
This process is called provisioning.

!!! Note
    VU1 Dials that come in packs of 4 (1 HUB + 3 Dials) come already provisioned to the hub.
    You should do this step only if adding new/additional dials.

## Provision dial

New dial can be provisioned by sending a requesting to the VU HUB to scan the bus for new dial and provision it.

{{ usage_api_macro('dial/provision', 'GET', {'admin_key':'...'}) }}

Response is JSON object

``` json
{
    "status": "ok",
    "message": "",
    "data": null
}
```

After this step, if there was a new dial on the bus, it should appear in the dial list and can be configured and used by the system.

If there are multiple new dials connected to the bus, you should repeat this process until all dials are registered.

!!! Note
    This operation can only be performed with an API key that has a privileged access (master key).
