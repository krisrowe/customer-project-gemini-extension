---
name: customer-screenshots
description: Specialized skill for processing and managing technical screenshots. Activates on the 'sls' (see latest screenshot) keyword to ingest, compress, and transcribe visual assets, typically from the system desktop or screenshot directory.
---

Expert guidance for managing technical screenshots. This skill ensures that visual assets are lean, searchable, and properly stored.

## Core Mandates

### 1. Ingestion (The 'sls' Workflow)
*   **Discovery**: When the 'sls' keyword is used, search the system's default screenshot location (e.g., Desktop) for the most recently modified image file.
*   **Action**: Securely move the file into the current workspace's `customer/issues/<issue-name>/assets/` directory.

### 2. Mandatory Processing
Every screenshot MUST be processed before being added to a repository.
*   **Compression**: Use `sips` to keep files lightweight.
    *   **Standard**: Max Dimension 1920px, Quality 30%.
    *   **Command**: `sips -Z 1920 -s format jpeg -s formatOptions 30 <input> --out <output>`
*   **Size Verification**:
    *   **Target**: < 200KB.
    *   **Hard Limit**: 500KB. If an image exceeds this after compression, it MUST be moved to the customer's secure cloud storage instead of Git.

### 3. Searchability (OCR)
*   **Sidecars**: Always create a `.ocr.txt` file (e.g., `screenshot_name.ocr.txt`) alongside the image.
*   **Content**: Manually transcribe the key text, logs, or code shown in the image into this text file to ensure the repository remains searchable via `grep`.

### 4. Storage & Hygiene
*   **Git Tracking**: Only track the compressed version and its `.ocr.txt` sidecar.
*   **Data Minimization**: Ensure raw, uncompressed originals are securely moved to cloud storage or deleted once the compressed version is tracked.
