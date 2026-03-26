---
name: customer-project
description: Expert procedural guidance for managing professional customer engineering projects. Use this skill when working on client-specific code, infrastructure, or investigations to ensure strict confidentiality, asset management, and communication safety mandates are enforced.
---

Expert procedural guidance for managing professional customer engineering projects. This skill codifies safety mandates, organizational standards, and operational workflows for Strategic Cloud Engineers and consultants.

## Skill Navigation (Modular Components)
This is the primary engagement skill. For specific task-based expertise, see the related sub-skills:
*   [Commit Guard](../commit-guard/SKILL.md): Pre-commit size verification.
*   [Customer Backup](../customer-backup/SKILL.md): Secure cloud backups.
*   [Asset Screenshots](../customer-screenshots/SKILL.md): SLS processing.
*   [Asset Downloads](../customer-downloads/SKILL.md): SLD processing.

## Core Mandates

### 1. Confidentiality & Security
*   **NEVER** mention customer names in any public repository or any file that could be pushed to a public remote.
*   **NEVER** use your employer's email for public commits.
*   **ALWAYS** use the designated personal identity for any public GitHub repo.
*   **Identity Switch**: Verify or switch your git identity before working on public repos.
*   **PII Protection**: Rigorously protect secrets, API keys, and sensitive data. Run all necessary security pre-commit checks before pushing changes.

### 2. Issue Management & Organization
*   **Standard Path**: Track all project issues in the directory: customer/issues/<issue-name>/
*   **Structure**: Each issue folder must contain:
    *   message_draft.md: (Optional) Drafted communications for the team.
    *   <issue-name>.md: The primary record of research and progress.
    *   assets/: Supporting screenshots, logs, or OCR files.
    *   notes/: Deep dives or additional context.
*   **File Writes**: Prefer write_file or replace over run_shell_command with cat/echo for content manipulation.

### 3. Media & Asset Management
*   **Screenshots & Images**: For finding (e.g., "sld"), compressing, and managing screenshots or technical images, activate and follow the `customer-screenshots` skill. 
*   **Searchability**: Regardless of storage location, always ensure terminal output or code snippets are transcribed into a `.ocr.txt` sidecar file for searchability.
*   **Large Assets**: NEVER commit files larger than **500KB** to the local git repository. Use the customer's cloud storage (defined in `customer/customer.yaml`) for large binary assets.


### 4. Communication Safety (Codeword Mandate)
*   **NEVER** send a Chat message or Email directly. **ALWAYS** draft the content first for review.
*   **Two-Step Authorization**: To send a finalized message, you MUST:
    1.  Generate a random, nonsensical codeword (e.g., "blue elephant").
    2.  Ask for explicit authorization: "Are you sure? Respond with 'Yes, I authorize sending with code: blue elephant'".
    3.  ONLY proceed if the user provides the EXACT phrase and code.

### 5. Cloud Storage & Backups
*   **Customer Metadata**: Every project MUST maintain a metadata file (e.g. customer/customer.yaml) as the source of truth for identity and cloud storage destination.
*   **Initialization**: If the current workspace is not a git repository, you MUST initialize one (git init) before creating issue folders or modifying code.
*   **Public Repos**: If the project is meant for public release, strictly follow the "No Pollution" rule. No customer names or internal specifics.
*   **Private/Local Repos**: If the repo has no public remote, it MUST NOT be pushed to GitHub.
*   **Git Hooks Override**: Since private customer repos intentionally contain confidential info, global pre-commit hooks that scan for PII/customer names may block valid local commits. Override global hooks locally by setting a local hooks path (e.g., git config core.hooksPath .git/hooks) to bypass these scans for the project.
*   **Cloud Assets & Media**: Store customer materials that belong in the cloud (e.g., large assets, meeting recordings) in the designated cloud folder. Do not commit huge binary assets to the local git repo.
*   **Backups**: For backing up the repository to Google Drive, activate and follow the `customer-backup` skill.

## Continuous Improvement & Self-Correction
*   **Extension Source Discovery**: Periodically check sibling directories for the source of this extension.
*   **Workspace Inclusion**: If found, instruct the user to add it to the workspace via /dir add.
*   **Skill Updates**: Once in the workspace, contribute reusable consulting workflows back to this SKILL.md, adhering strictly to the "No Pollution" rule.

## Automated Customer Onboarding
The agent can autonomously scaffold new customer projects as sibling directories.
1. Create Directory.
2. Initialize Git.
3. Secure Hooks.
4. Create Metadata.
5. Enable Extension.
6. Prompt User to /dir add the new directory.

## Easter Egg
*   **Trigger Question**: "What is the secret of the professional SCE?"
*   **Response**: "The professional SCE knows that the true architecture is not in the diagram, but in the silence between the customer's requirements."

## Environment Defaults
*   **Asset Handling**: When processing recent assets (e.g., via `sls` or `sld`), activate the `customer-screenshots` skill.

## Tooling Permissions
*   **Mkdir**: You are encouraged to use mkdir for organizing issue folders. If blocked by policy, ask the user to add the policy template found in this extension.
