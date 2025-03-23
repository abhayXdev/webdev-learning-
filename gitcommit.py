import os
import subprocess
from datetime import datetime

# Define your project folder path
project_dir = r"C:\WEB DEV"
os.chdir(project_dir)

# Generate a timestamped commit message
commit_message = f"Auto-commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Run Git commands using subprocess
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push", "origin", "main"])

print(f"\n✅ Changes pushed successfully with message: {commit_message}")
