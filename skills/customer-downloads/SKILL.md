---
name: customer-downloads
description: Specialized skill for processing and managing downloaded technical assets. Activates on the 'sld' (see latest download) keyword to ingest and process the most recent file from the system downloads directory.
---

Expert guidance for ingesting technical assets from the system downloads directory.

## Core Mandates

### 1. Ingestion (The 'sld' Workflow)
*   **Discovery**: When the 'sld' keyword is used, search the system's primary downloads directory for the most recently modified file.
*   **Action**: Securely move the file into the current workspace's `customer/issues/<issue-name>/assets/` directory.

### 2. Mandatory Processing
*   **Asset Type**: If the asset is an image (JPG/PNG), immediately activate and follow the processing rules in the [customer-screenshots](../customer-screenshots/SKILL.md) skill (compression and OCR).
*   **Non-Media**: For logs or configuration files, ensure they are appropriately named and placed in the issue's `assets/` or `notes/` directory.

### 3. Data Minimization
*   **Source Cleanup**: Ensure no fragments of confidential customer data remain in the generic system downloads folder after ingestion.
