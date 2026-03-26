# Customer Project Gemini Extension

Expert guidance, safety mandates, and standardized workflows for professional customer engineering and consulting projects.

This extension is designed for Strategic Cloud Engineers (SCEs) and consultants who manage multiple customer-specific workspaces. It codifies best practices for confidentiality, automated project scaffolding, and rigorous asset management.

## 🎬 Quick Demo (The Consultant UX)
Here is what using this extension looks like in practice. Notice how the agent automatically handles the project scaffolding, security checks, and evidence management without requiring you to remember the boilerplate.

```bash
# 1. Enter your private customer workspace
cd /path/to/projects/acme-corp

# 2. Launch the agent
gemini
```

**Inside the Gemini CLI:**
> **You:** "Activate the `customer-project` skill. Check my latest email from Bob at Acme Corp. Start tracking a new issue for this called 'api-auth-failure' that includes his email as a .md file. Then, do the research and create a draft email reply. Give me the link to review it in Gmail."
> 
> **Gemini:** *(Autonomously creates the `customer/issues/api-auth-failure/` directory, copies the email context into `api-auth-failure.md`, researches the codebase, and uses the `gmail.createDraft` tool).* 
> "I have scaffolded the issue, tracked the context, and drafted a reply. You can review the draft here: `https://mail.google.com/...`"
> 
> **You:** "The draft looks great. Send it."
> 
> **Gemini:** "Because this is a customer project, I must enforce the Two-Step Authorization mandate. Are you sure? Respond with 'Yes, I authorize sending with code: purple platypus'."
> 
> **You:** "Yes, I authorize sending with code: purple platypus"
> 
> **Gemini:** *(Autonomously sends the email).*

---

## 🚀 Quick Start

### 1. Register with Gemini CLI (One-time)
Register the extension to make its skills available on your machine.

**Option A: Install from GitHub (Easiest)**
```bash
gemini extensions install https://github.com/krisrowe/customer-project-gemini-extension
```

**Option B: Clone and Link (For Development & Self-Updating)**
```bash
git clone https://github.com/krisrowe/customer-project-gemini-extension.git /path/to/projects/customer-project-gemini-extension
gemini extensions link /path/to/projects/customer-project-gemini-extension
```

**Recommended: Scope to Workspaces**
By default, the CLI enables new extensions globally. Since this extension includes specialized behaviors—like automatically initializing Git repos or overriding commit hooks for private projects—it is recommended to disable it globally and enable it only in specific customer directories:
```bash
gemini extensions disable --scope user customer-project-gemini-extension
```

### 2. Enable for a Project
Navigate to your specific customer repository and enable the extension for that workspace:
```bash
cd /path/to/customer-project
gemini extensions enable --scope workspace customer-project-gemini-extension
```

---

## 🛠️ Prerequisites
This extension automates workflows that rely on the following MCP servers:
- **`google-workspace`**: For email ingestion and draft creation.
- **`consult`**: For security scanning and identity management.

## 🛡️ Professional Standards

This extension enforces professional standards across engagements:
- **Codeword Authorization**: Uses a two-step verification process before sending external communications (Email/Chat).
- **Identity Management**: Enforces the use of Application Default Credentials (`adc`) and prevents the use of employer-specific email addresses in public contexts.
- **PII Protection**: Directs the agent to scan and scrub PII, secrets, and customer names before potential public operations.


## ✨ Core Capabilities

### 📂 Automated Issue Scaffolding
Standardize how technical investigations are tracked without manual boilerplate:
- **Automation**: The `customer-project` skill autonomously handles scaffolding via a bundled Python script.
- **Invocation**: Simply ask the agent to "open a new issue called `<issue-name>`".
- **Result**: Autonomously creates a consistent directory structure (`customer/issues/<name>/`) with dedicated folders for `assets`, `notes`, and a pre-templated progress tracking markdown file.


### 🖼️ Media & Asset Management
Standardized workflow for processing technical assets:
- **Automation**: Includes `customer-screenshots` skill and `process_screenshot.py` utility.
- **Compression**: Automatically uses `sips` to compress screenshots (Standard: Max 1920px, Quality 30%).
- **Size Enforcement**: Enforces a 500KB limit for Git commits, directing larger files to cloud storage.
- **Searchability**: Mandates the creation of `.ocr.txt` sidecar files for technical images to ensure terminal output is searchable via `grep`.
- **Ingestion**: Recognizes the "sld" workflow to autonomously find and ingest the latest files from local staging areas.

### ☁️ Secure Cloud Backups (Google Drive)
Because private customer repositories contain confidential information, they should **never** be pushed to public GitHub. While an internal, private Git server (like self-hosted GitLab or Bitbucket) is always the preferred remote destination, this extension provides a secure alternative when a private Git host is unavailable by automating remote backups to Google Drive:
- **Metadata-Driven**: Uses a `customer/customer.yaml` file as the source of truth for Google Drive folder IDs.
- **Secure Bundling**: Directs the agent to create full Git bundle backups locally and upload those bundles directly to the customer's dedicated Google Drive folder.
- **Size-Aware**: Included `customer-backup` skill compares the new local bundle size vs. the remote backup size before overwriting to prevent accidental binary bloat.

*(Note: We are actively tracking a future enhancement to support [Google Cloud Storage (GCS) buckets](https://github.com/krisrowe/customer-project-gemini-extension/issues/3) as a machine-independent, identity-scoped alternative to Google Drive).*

### 🔄 Continuous Improvement
The extension source code is self-aware. When used in environments where the source is present, the agent is encouraged to proactively update the `SKILL.md` with newly discovered reusable patterns, creating a growing knowledge base for all projects.

## 🤝 Contributing
Contributions are welcome! Please review the [CONTRIBUTING.md](CONTRIBUTING.md) for security guidelines before opening a Pull Request.

To test your changes locally, check out the [Headless Testing Guide](docs/TESTING.md).

## ⚖️ License
MIT
