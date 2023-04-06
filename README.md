[![forthebadge](https://forthebadge.com/images/badges/made-with-crayons.svg)](https://forthebadge.com)

# subtitle-renamer-scripts
A way to rename subtitles in nested folders. Useful for legal torrenting.

# Usage
Just execute the script with the file path as the only argument.

## qBittorent
Via: "qbittorrent run external program on completion" in settings.

Be sure to escape the file path here!

`python C:\github\folder\here\subtitle-renamer-scripts\renamer.py "%R"`

## Testing

You can run the script on the `sample_data` directory to test things out.

```bash
sh format_sample_data.sh
python renamer.py sample_data\
```
