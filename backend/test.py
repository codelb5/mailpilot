import os

# Custom list of folders to ignore (added mail-venv here)
EXCLUDE_DIRS = {
    "mail-venv",
    "__pycache__",
    ".git",
    ".vscode",
    ".idea",
    "venv",
    "node_modules",
}


def generate_markdown_tree(dir_path, prefix=""):
    """
    Recursively generates a markdown string representing the directory tree.
    """
    try:
        # Filter out the excluded directories
        items = [item for item in os.listdir(dir_path) if item not in EXCLUDE_DIRS]
    except PermissionError:
        return ""

    # Sort items so folders appear first, then files alphabetically
    items.sort(key=lambda x: (not os.path.isdir(os.path.join(dir_path, x)), x.lower()))

    markdown_str = ""
    count = len(items)

    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = i == count - 1

        # Select the correct branch visual
        connector = "└── " if is_last else "├── "
        markdown_str += f"{prefix}{connector}{item}\n"

        # Recurse into subdirectories
        if os.path.isdir(path):
            next_prefix = prefix + ("    " if is_last else "│   ")
            markdown_str += generate_markdown_tree(path, next_prefix)

    return markdown_str


if __name__ == "__main__":
    root_dir = os.getcwd()
    root_name = os.path.basename(root_dir) or "Root"

    print(f"Scanning directory: {root_dir}...\n")

    # Generate tree structure string
    tree_content = f"{root_name}/\n" + generate_markdown_tree(root_dir)
    markdown_output = f"```text\n{tree_content}```"

    # Write to file
    output_filename = "project_structure.md"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(markdown_output)

    print(
        f"Success! Markdown tree saved to '{output_filename}' (skipping mail-venv and __pycache__)"
    )
