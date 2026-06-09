"""
StandardLib_OS_Sys.py
Working with the OS and System libraries for file/directory manipulation and system-level operations.
"""

import os
import sys

def main():
    print("--- 1. OS Module: Working with Directories ---")
    current_dir = os.getcwd()
    print(f"Current Working Directory: {current_dir}")
    
    # Create a temporary directory
    temp_dir = "temp_demo_dir"
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
        print(f"Created directory: {temp_dir}")
    
    print("\n--- 2. OS Module: Listing Files ---")
    print(f"Contents of '{current_dir}':")
    items = os.listdir(current_dir)
    # Print first 5 items to keep output short
    for item in items[:5]:
        print(f" - {item}")
        
    print("\n--- 3. OS Module: Path Joining ---")
    # Safely join paths regardless of OS (Windows \ vs Linux /)
    file_path = os.path.join(current_dir, temp_dir, "example.txt")
    print(f"Constructed Path: {file_path}")
    
    # Cleanup
    if os.path.exists(temp_dir):
        os.rmdir(temp_dir)
        print(f"\nRemoved temporary directory: {temp_dir}")

    print("\n--- 4. OS Module: Environment Variables ---")
    path_var = os.environ.get('PATH')
    print(f"PATH Environment Variable (first 100 chars): {path_var[:100]}...")

    print("\n--- 5. Sys Module: Python Version & Path ---")
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Python Executable: {sys.executable}")
    
    print("\n--- 6. Sys Module: Command Line Arguments ---")
    print(f"Script Name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments passed: {sys.argv[1:]}")
    else:
        print("No extra arguments passed to script.")

if __name__ == "__main__":
    main()
