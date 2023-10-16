# testdata
Public DESHIMA datasets for testing related codes

## List of observations

| Run ID | Log ID | Source | Obstable | Az (deg) | El (deg) | ALMA PWV (mm) |
| --- | --- | --- | --- | --- | --- | --- |
| 1010 | 20171103184436 | saturn | saturn_zscan_cont | 86.3 | 83.5 | n/a |
| 1184 | 20171111103248 | skydip | skydip_el32-88 | 180.4 | 88 | 0.52 |
| 1187 | 20171111110002 | mars | mars_azel_raster_240_d3_t4 | 71.2 | 45.6 | 0.51 |
| 1243 | 20171113070539 | orikl | orikl_radec_raster_240_d6_t4 | -26.2 | 70.6 | 2.85 |
| 1308 | 20171115052750 | uranus | uranus_daisy_60 | -59.4 | 34.4 | 2.49 |

## List of datasets

| Type | Description |
| --- | --- |
| `cosmos/cosmos_<log ID>` | Series of raw data and logs of DESHIMA and ASTE
| `ddb/ddb_20180619.fits.gz` | DESHIMA database (DDB) compiled on June 19, 2018
| `dfits/dfits_<log ID>.fits.gz` | Merged DESHIMA FITS (DFITS) created by [dmerge:1.0.0](https://github.com/deshima-dev/dmerge/releases/tag/v1.0.0)
