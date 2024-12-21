import os
import re
import shutil
import json
import argparse
import fnmatch

def bundle_code(project_root, output_dir, config):
    """Bundles code by removing comments and unnecessary whitespace and calculates size."""

    if not os.path.exists(project_root):
        print(f"Error: Project root '{project_root}' does not exist.")
        return

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    shutil.copytree(project_root, output_dir)

    total_characters = 0

    for root, _, files in os.walk(output_dir):
        for filename in files:
            filepath = os.path.join(root, filename)

            if not _should_process_file(filepath, config):
                continue

            try:
                with open(filepath, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    original_len = len(content)

                    if config.get("remove_comments", True):
                        content = _remove_comments(content, filename)
                    if config.get("remove_whitespace", True):
                        content = _remove_whitespace(content)

                    if len(content) != original_len:
                        f.seek(0)
                        f.truncate()
                        f.write(content)

                    total_characters += len(content) # Accumulate characters

                print(f"Processed: {filepath}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

    return total_characters # Return total characters

def _should_process_file(filepath, config):
    """Checks if a file should be processed based on include/exclude patterns."""
    include_patterns = config.get("include_patterns", ["*"])
    exclude_patterns = config.get("exclude_patterns", [])
    for pattern in exclude_patterns:
        if fnmatch.fnmatch(filepath, pattern):
            return False

    for pattern in include_patterns:
        print(pattern)
        if fnmatch.fnmatch(filepath, pattern):
            return True

    return False

def _remove_comments(content, filename):
    """Removes comments from code based on file type."""
    if filename.endswith((".py", ".cpp", ".c", ".java", ".js", ".ts", ".go", ".rs")):
        content = re.sub(r"/\*[\s\S]*?\*/|//.*", "", content)
    elif filename.endswith((".sh", ".bash")):
        content = re.sub(r"#.*", "", content)
    elif filename.endswith(".clj"):
        content = re.sub(r";;.*", "", content)
        content = re.sub(r"#_.*?\n", "", content)
        content = re.sub(r"#\{[\s\S]*?\}", "", content)
    return content

def _remove_whitespace(content):
    """Removes unnecessary whitespace."""
    content = re.sub(r"\n\s*\n", "\n", content)
    content = re.sub(r"[ \t]+$", "", content, flags=re.MULTILINE)
    return content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bundles code by removing comments and whitespace.") # Updated description
    parser.add_argument("project_root", help="Path to the project root directory.")
    parser.add_argument("-o", "--output", help="Path to the output directory (default: bundled_<project_root>).", default=None) # Updated default output name
    parser.add_argument("-c", "--config", help="Path to the config file (default: config.json)", default="config.json")

    args = parser.parse_args()

    project_root = args.project_root
    output_directory = args.output or f"bundled_{os.path.basename(project_root)}" # Updated output directory name
    config_file = args.config

    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error with config file: {e}. Using default configuration.")
        config = {
            "include_patterns": ["*.py", "*.clj", "*.cpp", "*.c", "*.java", "*.js", "*.ts", "*.go", "*.rs", "*.sh", "*.bash"],
            "exclude_patterns": ["test/*", "tests/*", "docs/*", "examples/*"],
            "remove_comments": True,
            "remove_whitespace": True
        }

    total_characters = bundle_code(project_root, output_directory, config) # Get total characters

    if total_characters is not None: # Check if bundling was successful
        print("Code bundling complete.")
        print(f"Total characters in bundled code: {total_characters}")

        # Approximate token count (1 token ≈ 4 characters)
        approximate_tokens = total_characters / 4
        print(f"Approximate token count: {approximate_tokens:.0f}") # Format to whole number

        # Bytes Calculation
        total_bytes = os.path.getsize(output_directory)
        for root, _, files in os.walk(output_directory):
            for file in files:
                total_bytes += os.path.getsize(os.path.join(root, file))
        print(f"Total bytes in bundled code: {total_bytes}")
    else:
        print("Code bundling failed.")