#!/usr/bin/env python3
import os
import sys
import subprocess

def get_file_size(file_path):
    if os.path.exists(file_path):
        size_bytes = os.path.getsize(file_path)
        for unit in ['B', 'KB', 'MB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}", os.path.getsize(file_path)
            size_bytes /= 1024.0
    return "Unknown", 0

def process_image(input_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return False

    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_compressed.jpg"
    
    print(f"Compressing: {input_path} -> {output_path}...")
    
    try:
        # Standard: Max Dimension 1920px, Quality 30%
        cmd = [
            'sips', '-Z', '1920', 
            '-s', 'format', 'jpeg', 
            '-s', 'formatOptions', '30', 
            input_path, '--out', output_path
        ]
        subprocess.run(cmd, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during compression: {e.stderr.decode()}")
        return False
    except FileNotFoundError:
        print("Error: 'sips' command not found. This utility requires macOS.")
        return False

    size_str, size_bytes = get_file_size(output_path)
    print(f"\n✅ Compression complete.")
    print(f"Compressed Size: {size_str}")
    
    limit = 500 * 1024 # 500KB
    if size_bytes > limit:
        print(f"⚠️  WARNING: File still exceeds 500KB hard limit.")
        print(f"This file SHOULD NOT be committed to the local git repository.")
        print(f"Please move it to the customer's cloud storage (Google Drive).")
    elif size_bytes > 200 * 1024:
        print(f"ℹ️  Note: File is above 200KB target, but below 500KB limit.")
    else:
        print(f"✅ File is within the target size (< 200KB).")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 process_screenshot.py <image_path>")
        sys.exit(1)
    
    success = process_image(sys.argv[1])
    if not success:
        sys.exit(1)
