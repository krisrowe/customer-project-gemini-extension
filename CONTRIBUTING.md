# Contributing

Thank you for considering contributing to the Customer Project Gemini Extension!

## ⚠️ MANDATORY: The "No Pollution" Rule
This is a **public** repository. You MUST maintain absolute purity to protect professional integrity and confidentiality. 

Before opening a Pull Request, ensure your changes do not contain:
- **Company Names**: No employer names, no customer names.
- **Personal Names**: No real names of colleagues or clients.
- **Identifiers**: No real Google Drive Folder IDs, Doc IDs, or cloud resource identifiers. Use synthetic placeholders (e.g., `<Google_Drive_Folder_ID>`).
- **Emails**: No real email addresses. Use whitelisted placeholders like `user@example.com`.

## Testing Your Changes
You are expected to test your modifications (especially to `SKILL.md` or bundled scripts) before submitting them. 

You can test changes rapidly without restarting your agent session by using isolated temporary directories and headless CLI executions. 

👉 **Read the full testing guide here: [docs/TESTING.md](docs/TESTING.md)**

## Making a Pull Request
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-new-workflow`).
3. Commit your changes (`git commit -m 'feat: Add amazing new workflow'`).
4. Ensure the pre-commit scan passes cleanly.
5. Push to the branch and open a Pull Request.
