import os
import subprocess

# Function to clone GitHub repository if not already cloned
def clone_repo(url, folder):
    if not os.path.exists(folder):
        print(f"📥 Cloning the repo {url}...")
        subprocess.run(["git", "clone", url, folder])
    else:
        print(f"📁 Repository already exists at {folder}")
