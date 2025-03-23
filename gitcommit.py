import os

project_dir = r"C:\WEB DEV"  # Replace with your actual project path
os.chdir(project_dir)

# Default commit message
commit_message = "Auto-commit: Latest changes"

os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push origin main")

print("\n✅ Changes pushed successfully to GitHub!")
