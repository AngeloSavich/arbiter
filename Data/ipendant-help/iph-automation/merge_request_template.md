# Summary

cherry-pick of <https://gitlab.one.fanuc.com/fac/facrd/controller/-/merge_requests/1587> | 10.10 upstream

Versions:

- 10.1326
- 10.1055

## Requested changes

- <https://gitlab.one.fanuc.com/fac/facrd/issues-ngc/-/issues/1465>
- <https://gitlab.one.fanuc.com/fac/facrd/issues-ngc/-/issues/1628>

##### Summary of Changes

- `ANGLE_ENTRY_SHIFT`
  - Punctuation change to include period at the end of help page title
- `ZDT_EOAT_Setup`:
  - Separates ZDT EOAT help page sections by section instead of chapter (formatting)
- `TEST_CYCLE_SPOT_WELD`
  - New Section
  - Replacing TEST_CYCLE_SPOT_SCREEN
- `MOTION_PERFORMANCE`
  - Renamed to `PAYLOAD`

## Change Results

##### Screens Changed

- [h4c001-ZDT_EOAT_SETUP.zip](/uploads/030bc43ff05ec18bd7520ca0b22922f2/h4c001-ZDT_EOAT_SETUP.zip)
- [h12201-PAYLOAD.zip](/uploads/f5c0553790f69b61719b21bf7431a397/h12201-PAYLOAD.zip)
- [s3b801-TEST_CYCLE_SPOT_WELD.zip](/uploads/d7ad6b6fc2c6a10237decc9992a700cb/s3b801-TEST_CYCLE_SPOT_WELD.zip)
- [h0fe01-ANGLE_ENTRY_SHIFT.zip](/uploads/8dbe449bf90db0c2cb683a7598ed2de2/h0fe01-ANGLE_ENTRY_SHIFT.zip)

##### Steps to test

1. Download each zip and repeat the processes for each
2. Unzip folder `h12201-PAYLOAD.zip` and extract folder `h12201`
3. Open extracted folder `h12201`
   - **Note**: If you are still in the .zip folder, you have not extracted folder `h12201`
4. Launch `index.html` in browser to view

## Build / Release

- [helpeg.zip](/uploads/4cf72171b6f9eafe440a79c9d0decde4/helpeg.zip)
- [build.log](/uploads/6d01c4bf0acfe4522f4e29be5a41e172/build.log)


-------------------------


# Summary

cherry-pick of https://gitlab.one.fanuc.com/fac/facrd/controller/-/merge_requests/1719 | 10.10 upstream

Versions:
- 10.1327
- 10.1057 (or 10.1058)

## Requested changes:
- https://gitlab.one.fanuc.com/fac/facrd/issues-ngc/-/issues/1637
- https://gitlab.one.fanuc.com/fac/facrd/issues-ngc/-/issues/1643

##### Summary of Changes:
- `Brake Check` - `h47f04`
  - [BrakeCheck_R50iA_doc.docx](/uploads/fabfdbf7143230fda71d2584e290a73f/BrakeCheck_R50iA_doc.docx)
- `ALARM_RECOVERY_SCREEN` - `h67509`:
  - Fixes help_id

## Change Results: 

##### Screens Changed:

- [h67509-ALARM_RECOVERY_SCREEN.zip](/uploads/1683b895b0248226a133eb57adebfec1/h67509-ALARM_RECOVERY_SCREEN.zip)
- [h47f04-BRAKE_CHECK.zip](/uploads/c76534c9f55fdb0ffbdb1a418e2a8c7b/h47f04-BRAKE_CHECK.zip)

##### Steps to test:

1. Download each zip and repeat the processes for each
2. Unzip folder `h67509-ALARM_RECOVERY_SCREEN.zip` and extract folder `h67509`
3. Open extracted folder `h67509`
   - **Note**: If you are still in the .zip folder, you have not extracted folder `h67509`
4. Launch `index.html` in browser to view

## Build / Release
- [helpeg.zip](/uploads/2a297e2042156cd028401e4b77b2e61a/helpeg.zip)
- [build.log](/uploads/d6d1919ce6b7f3e34143a54fed682c91/pub.log)