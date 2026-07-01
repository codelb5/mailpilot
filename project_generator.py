from pathlib import Path

PROJECT_NAME = "./"

# ==========================
# Root folders
# ==========================

ROOT_FOLDERS = [
    "backend",
    "frontend",
]

# ==========================
# Backend folders
# ==========================

BACKEND_FOLDERS = [
    "src",
    "src/api",
    "src/api/routes",
    "src/ai",
    "src/auth",
    "src/config",
    "src/database",
    "src/database/repositories",
    "src/gmail",
    "src/llm",
    "src/models",
    "src/prompts",
    "src/services",
    "src/toolkits",
    "src/utils",
    "tests",
    "docs",
    "scripts",
    "logs",
]

# ==========================
# Python packages
# ==========================

PYTHON_PACKAGES = [
    "src",
    "src/api",
    "src/api/routes",
    "src/ai",
    "src/auth",
    "src/config",
    "src/database",
    "src/database/repositories",
    "src/gmail",
    "src/llm",
    "src/models",
    "src/services",
    "src/toolkits",
    "src/utils",
]

# ==========================
# Files
# ==========================

FILES = [
    "main.py",
    # "pyproject.toml",
    ".env",
    ".env.example",
    ".gitignore",
    "README.md",
    "Dockerfile",
    "docker-compose.yml",
]

# ==========================
# Helpers
# ==========================


def create_folder(path: Path):

    path.mkdir(parents=True, exist_ok=True)


def create_file(path: Path):

    if not path.exists():
        path.touch()


def create_init(package: Path):

    init = package / "__init__.py"

    if not init.exists():
        init.touch()


# ==========================
# Main
# ==========================


def main():

    project_root = Path(PROJECT_NAME)

    create_folder(project_root)

    print(f"\nCreating project: {PROJECT_NAME}\n")

    # Root folders
    for folder in ROOT_FOLDERS:

        path = project_root / folder

        create_folder(path)

        print("📁", path)

    backend = project_root / "backend"

    # Backend folders
    for folder in BACKEND_FOLDERS:

        path = backend / folder

        create_folder(path)

        print("📁", path)

    # __init__.py
    for package in PYTHON_PACKAGES:

        package_path = backend / package

        create_init(package_path)

        print("🐍", package_path / "__init__.py")

    # Files
    for file in FILES:

        path = backend / file

        create_file(path)

        print("📄", path)

    print("\nProject structure created successfully!")


if __name__ == "__main__":
    main()
