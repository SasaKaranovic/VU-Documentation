# Set dial image

{{ api_table('Set dial image', 'dial/{DIAL_UID}/image/set', 'POST', ['key', 'imgfile', 'force']) }}

Set dial image (e-ink image) to provided image file.

Please note that the image file has to be uploaded as `form-data`.


## Sending new image

Server expects the image to meet following requirements

- Size: `144 x 200`
- Type: `PNG` / `JPG` / `JPEG`


After the image has been uploaded server will perform CRC32 comparison of binary image contents against existing image that is stored on the server. This is a simple check to compare new image to the existing one.

- If image contents is different, server will send the image to the target dial
- If image contents is same, server will ignore this request and return success

!!! note annotate "Image upload - E-Ink"

    E-Ink displays are awesome, but they have a big technical limitation. Updating the display contents is very slow. To fully update the screen it can take anywhere from 2-5 seconds.


!!! warning annotate "Force image upload"

    If `force` query parameter is set, server will skip the image comparison and always send the image to the dial. This should *not* be used under normal circumstances.



---

## Example usage

Set the image of dial with UID `3E0075000650564139323920` to image `my_awesome_image.png`

Please note that `my_awesome_image.png` is the image you will have to upload using `form-data`.

{{ usage_api_macro('dial/3E0075000650564139323920/image/set', 'POST', {'key':'...', 'imgfile':'my_awesome_image.png'}) }}

Response is a JSON object

```json
{
    "status": "ok",
    "message": "",
    "data": null
}
```

---

