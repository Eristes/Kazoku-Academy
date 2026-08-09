import os

# --- Configuration ---
suffix = "WEEK2026"    # part after the number
count = 37             # total folders
start = 1              # starting number
parent_dir = "."       # "." = current directory

# --- Create folders ---
for i in range(start, start + count):
    # Format: two digits with leading zero → then suffix
    folder_name = f"{i:02d}{suffix}"
    folder_path = os.path.join(parent_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created: {folder_path}")
