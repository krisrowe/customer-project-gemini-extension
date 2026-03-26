---
name: commit-guard
description: Pre-commit safety check to prevent repository bloat. Use this skill whenever you are about to commit changes to a private customer repository to ensure large files are not accidentally included and to verify compliance with bundle-based backup constraints.
---

Expert guidance for performing safe Git commits in private repositories. This skill ensures that the local repository database remains lightweight and optimized for Git bundle-based backups.

## Core Mandates

### 1. Staged File Verification
Before executing any `git commit` command, you MUST verify the size of all staged files. 
*   **Automation**: Use the bundled Python script: `python3 ${extensionPath}/scripts/commit_check.py`.
*   **Threshold**: Any file larger than **500KB** is considered a risk for repository bloat.

### 2. User Notification & Approval
If large files are detected, you MUST pause and present a warning to the user.
*   **The Bundle Reminder**: Remind the user that private repositories are backed up as **large Git bundle files**. Explain that unlike standard Git remotes that use delta-based pushing, bundles grow with the total repository size, making large files exceptionally costly for backup performance.
*   **Explicit Confirmation**: Ask the user: "These files will increase the size of every future backup bundle. Are you sure you want to commit them to the Git history, or should they be moved to cloud storage instead?"

### 3. Resolution Strategies
If the user decides against committing a large file:
1.  **Unstage**: `git restore --staged <file>`.
2.  **Move to Cloud**: Relocate the file to the customer's Google Drive folder (defined in `customer/customer.yaml`).
3.  **Ignore**: Ensure the file type or path is added to `.gitignore`.
4.  **Reference**: If necessary, create a small text file or markdown note in the repo referencing the cloud-stored asset.

## Integration
This skill is designed to work in tandem with the `customer-project` skill. While `customer-project` handles the overall engagement, `commit-guard` provides surgical focus on the moment of commit.
