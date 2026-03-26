# Testing the Extension

[← Back to README](../README.md)

When developing and modifying this Gemini CLI extension, you do not need to exit your active agent session, restart, and manually prompt to test your changes. Instead, you can use an **In-Session Headless Testing** pattern.

This approach leverages isolated temporary directories and the `gemini` CLI's non-interactive mode to quickly prove that skills, context, and scripts are working as expected.

## The Headless Testing Pattern

You can ask the agent (or run it yourself in the terminal) to execute a test suite using the `-p` (prompt) and `-y` (auto-approve/YOLO) flags in a completely isolated directory.

### Example: Testing the Issue Creation Script

```bash
# 1. Create a clean, isolated temporary workspace
mkdir -p /tmp/fake-project-test
cd /tmp/fake-project-test

# 2. Run the agent headlessly with the extension explicitly enabled
gemini -e customer-project-gemini-extension -p "Activate the customer-project skill. Create a new issue called 'db-migration' using the Python script at /path/to/extension/scripts/create_issue.py." -y

# 3. Verify the output
ls -la customer/issues/db-migration
cat customer/issues/db-migration/db-migration.md
```

## Why Test This Way?

1. **Speed**: It creates a lightning-fast iteration loop. You can modify a Python script or update `SKILL.md`, and immediately run a test command in the same chat window.
2. **Isolation**: By running the test in `/tmp/fake-project-test` and using the `-e` flag, you prove that the extension's rules are correctly scoped to the project and aren't leaking globally.
3. **Reproducibility**: Headless prompts ensure the exact same conditions are met every time you test a feature.

## Testing Isolation (Project vs. Global)

To verify that the extension's ambient context (like the `adc` Google Workspace profile requirement) is not polluting the global environment, you can run a head-to-head test:

```bash
mkdir -p /tmp/customer-a /tmp/internal-b

# Should enforce extension rules
cd /tmp/customer-a && gemini -e customer-project-gemini-extension -p "What is my required Google Workspace profile? Be concise."

# Should return standard defaults
cd /tmp/internal-b && gemini -e none -p "What is my required Google Workspace profile? Be concise."
```
