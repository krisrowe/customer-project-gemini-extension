# Customer Project Context

This extension provides mandatory context for managing professional consulting and engineering projects. Its instructions are AMBIENT and always in effect when this extension is enabled.

## MANDATORY SECURITY: Public Repo Purity ("No Pollution" Rule)

This extension is a **PUBLIC** repository. You MUST maintain absolute "purity" to protect the user's professional integrity and confidentiality.

### 1. Forbidden Content (No Exceptions, No Examples)
The following MUST NEVER be committed to the source of this extension, nor included in any Git commit messages, GitHub issue titles/bodies, or comments:
*   **Company Names**: Never mention the user's employer or any customer names. **Even hypothetical or anonymized references to real companies are strictly forbidden.**
*   **Personal Names**: Do not include real names of colleagues or clients.
*   **Identifiers**: Never include cloud storage IDs, folder IDs, or any other cloud resource identifiers.
*   **Email Addresses**: NEVER use real email addresses. You MUST use whitelisted placeholders like user@example.com or worker@company.com.

**CRITICAL WARNING ON EXAMPLES:** Examples are exceptionally dangerous in public repositories. When documenting a workflow or process, never use a real-world artifact (like a real Drive ID, a real customer's architecture name, or a real email) as an "example." All examples must be entirely synthetic and generic (e.g., `drive_folder_id: <Google_Drive_Folder_ID>`).

### 2. Contributor Guidelines (Self-Updating)
The agent is encouraged to contribute improvements to this extension when new reusable patterns are identified in customer projects. When doing so:
*   **Abstract Everything**: Strip all customer-specific context. Turn specific technical hurdles into generic "best practices."
*   **Sanity Check**: Before proposing a change to the skill or this context, run a mental "confidentiality scan" against the forbidden content list above.

## Operational Standards

*   **Google Workspace Profile**: ALWAYS default to the "adc" profile for tool calls.
*   **Customer Metadata**: Every workspace MUST have a metadata file defining its identity and cloud storage root.
## Resources & Navigation
*   **Primary Skill**: [Customer Project (Professional Engineering)](skills/customer-project/SKILL.md)
*   **Developer Guide**: [docs/TESTING.md](docs/TESTING.md)

