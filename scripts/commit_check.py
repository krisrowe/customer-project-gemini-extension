#!/usr/bin/env python3
import subprocess
import os
import sys

def get_staged_files():
    try:
        result = subprocess.run(['git', 'diff', '--cached', '--name-only'], capture_output=True, text=True, check=True)
        return result.stdout.splitlines()
    except subprocess.CalledProcessError:
        return []

def format_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0

def main():
    files = get_staged_files()
    if not files:
        print("No files staged for commit.")
        return

    large_files = []
    limit = 500 * 1024 # 500KB
    
    print("Checking staged files for repository bloat...")
    for f in files:
        if os.path.exists(f):
            size = os.path.getsize(f)
            if size > limit:
                large_files.append((f, size))
    
    if large_files:
        print("\n⚠️  WARNING: LARGE FILES DETECTED")
        print("---------------------------------")
        for f, size in large_files:
            print(f"- {f} ({format_size(size)})")
        print("\nREMINDER: This repository is backed up as a single large Git bundle file.")
        print("Unlike standard repositories that push incremental deltas to a remote, bundle-based")
        print("backups grow linearly with the total size of the repository database.")
        print("Large files will significantly degrade backup performance and storage efficiency.")
        sys.exit(1)
    else:
        print("✅ No large files detected.")

if __name__ == "__main__":
    main()
