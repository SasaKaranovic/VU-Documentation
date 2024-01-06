# API Server Messaging

API server is listening for `HTTP` requests on `ip` and `port` that are defined in the server configuration.
By default the server is listening on `http://localhost:5340`


Each request that is sent to API server will receive a response that is a JSON object with following structure[^1]:

```json
{
    "status": "",   // Status: `ok` or `fail`
    "message": "",  // Message: Extra information
    "data": []      // Data: Data ie. dial information
}
```

## Status

The `status` will always be either `ok` or `fail`.

## Message
The `message` will give a human readable representation of the status.

## Data

The `data` will contain any information that was requested from the server.
If there was no data, this array will be empty.


!!! note annotate "Exception"

    Certain requests request specific type of response, for example get dial image. In this case the server will return raw binary data instead of JSON object.


[^1]: Certain requests request specific type of response, for example get dial image. In this case the server will return raw binary data instead of JSON object.
