
_BranchUser = 'angelo.savich'
_BranchPrefix = f'user/{_BranchUser}/'
_BranchVersion='v10.10'
BranchName=f'{user/angelo.savich/v10.10/update-help-edoc-18"


--


Assignee: '@krasny.darren.fac'
Reviewer: '@merchant.daniel.fac'

Title: '18i - Updates iPendant Help for v10.10'

Description =

```md
# Summary

<!-- cherry-pick of https://gitlab.one.fanuc.com/fac/facrd/controller/-/merge_requests/1587 | 10.10 upstream -->

Versions:
- 10.1327
- 10.1057

## Requested changes:
- https://gitlab.one.fanuc.com/fac/facrd/issues-ngc/-/issues/1637
- https://gitlab.one.fanuc.com/fac/facrd/issues-ngc/-/issues/1643

##### Summary of Changes:
- `[Brake Check]` - `[h47f04]`
  - [BrakeCheck_R50iA_doc.docx](/uploads/fabfdbf7143230fda71d2584e290a73f/BrakeCheck_R50iA_doc.docx)
- `ALARM_RECOVERY_SCREEN` - [`h67509`]:
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
```
