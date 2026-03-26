#!/usr/bin/env python3
import os
import sys
import subprocess
import yaml

def get_file_size(file_path):
    if os.path.exists(file_path):
        size_bytes = os.path.getsize(file_path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}", os.path.getsize(file_path)
            size_bytes /= 1024.0
    return "Unknown", 0

def main():
    yaml_path = os.path.join("customer", "customer.yaml")
    if not os.path.exists(yaml_path):
        print(f"Error: {yaml_path} not found.")
        sys.exit(1)
        
    with open(yaml_path, 'r') as f:
        config = yaml.safe_load(f)
        
    slug = config.get('slug')
    if not slug:
        print("Error: 'slug' not found in customer.yaml")
        sys.exit(1)
        
    bundle_name = f"{slug}-repo.bundle"
    
    print(f"Creating Git bundle: {bundle_name}...")
    try:
        subprocess.run(['git', 'bundle', 'create', bundle_name, '--all'], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating bundle: {e.stderr.decode()}")
        sys.exit(1)
        
    size_str, size_bytes = get_file_size(bundle_name)
    print(f"\n✅ Bundle created successfully.")
    print(f"Local Bundle Size: {size_str}")
    print(f"Target Filename: {bundle_name}")
    print(f"Target Drive Folder ID: {config.get('drive_folder_id', 'Not set')}")
    
if __name__ == "__main__":
    main()
