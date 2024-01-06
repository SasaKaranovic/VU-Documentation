# Server Configuration


## API Server Configuration

VU Server is configured via `config.yaml` file that can be found in the VU API Server installation directory.


```yaml
server:
  hostname: localhost
  port: 5340
  communication_timeout: 10
  dial_update_period: 200
  master_key: [...]

hardware:
  port:
```


### Hostname

`hostname` indicates on which address the VU Server API should listen for incoming API calls

Default: `localhost`


### Port

`port` is a numeric port value to be used for incoming API calls.
This is also the port that can be used to access Web UI.

Default: `5340`

### Timeout
`communication_timeout` -> After `communication_timeout` seconds of not responding to a request, server will assume that VU HUB is not responding.

### Update period
`dial_update_period` -> In miliseconds. How often to update dials.

### Master key

This is a special API key that has administrative privlidges.
You should **not** share this key with any application.
Instead you should [crete an API key](./webui/manage_keys.md).


## Dial and API configuration

VU API server stores dial and API keys information inside a SQLite database.

The SQLite database is store inside user directory

- Windows: `%USERPROFILE%\KaranovicResearch\vudials\vudials.db`
- Linux/Mac: `~/KaranovicResearch/vudials/vudials.db`

!!! warning
    This `vudials.db` file contains entire server configuration.
    If this file is removed, your dial names and API keys will be lost.
    You should back it up if you for example plan to re-install or change OS.
