print("Working with files and folders")

import os

old_path = r"..\projects"
new_path = r"..\new_project_dir"

if os.path.exists(old_path) and not os.path.exists(new_path):
    print(f"Directory was renamed from {old_path} to {new_path}")
