import os

def create_project_structure(base_path):
    # Define the folder structure
    folders = [
        "data/raw",
        "data/processed",
        "data/external",
        "data/interim",
        "notebooks",
        "scripts",
        "models",
        "reports/figures",
        "src/data",
        "src/features",
        "src/models",
        "src/visualization",
        "tests",
        "azure",  # For Azure-specific configurations
        "deploy"  # For deployment scripts
    ]

    # Create the folders
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created: {folder_path}")

    # Create placeholder files
    placeholder_files = [
        os.path.join(base_path, "README.md"),
        os.path.join(base_path, ".gitignore"),
        os.path.join(base_path, "requirements.txt"),
        os.path.join(base_path, "Dockerfile"),  # For containerization
        os.path.join(base_path, "azure-pipelines.yml")  # For Azure CI/CD
    ]

    for file in placeholder_files:
        with open(file, 'w') as f:
            f.write("")
        print(f"Created: {file}")

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    create_project_structure(base_path)