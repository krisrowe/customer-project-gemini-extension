---
name: customer-backup
description: Securely back up local-only customer repositories to Google Drive. Use this skill when you need to create a Git bundle and upload it to the customer's cloud storage, ensuring size-aware confirmation and version management.
---

Expert guidance for backing up private, local-only repositories using Git bundles and Google Drive.

## Procedural Workflow

### 1. Local Preparation
*   **Identify Destination**: Read `customer/customer.yaml` to get the `slug` and `drive_folder_id`.
*   **Create Bundle**: Run `python3 ${extensionPath}/scripts/prepare_backup.py`. This will create `<slug>-repo.bundle` and report its size.

### 2. Remote Audit
*   **Search Drive**: Use `drive.search` with a query like `name = '<slug>-repo.bundle' and '<drive_folder_id>' in parents`.
*   **Fetch Metadata**: If a file is found, get its `size` (converted to MB) and its `id`.

### 3. User Confirmation (Mandatory)
Before uploading, you MUST present a report:
*   **Local Bundle**: `<filename>` (`XX.X MB`)
*   **Remote Backup**: `<file_id>` (`YY.Y MB`)
*   **Comparison**: "The new backup is `ZZ%` [larger/smaller] than the existing one."
*   **Authorization**: "This will overwrite the existing backup at the same File ID on Google Drive. Respond with 'Yes, I authorize overwrite' to proceed."

### 4. Upload & Cleanup
*   **Execution**: Once authorized, use the appropriate Drive tool to upload the new bundle, ensuring it overwrites the existing file if found.
*   **Local Cleanup**: Delete the local `.bundle` file after a successful upload to keep the workspace clean.


## Automation
For consistency, you are encouraged to use a supporting script for the local bundle creation and size calculation if one is provided in the extension's `scripts/` directory.
