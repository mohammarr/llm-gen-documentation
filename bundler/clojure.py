import os
import re
import shutil
import json
import argparse
import fnmatch

def bundle_code(project_root, output_file, config):
    """Bundles code into a single file by removing comments and whitespace."""

    if not os.path.exists(project_root):
        print(f"Error: Project root '{project_root}' does not exist.")
        return None, None

    total_characters = 0
    bundled_content = ""

    for root, _, files in os.walk(project_root):
        for filename in files:
            filepath = os.path.join(root, filename)

            if not _should_process_file(filepath, config):
                continue

            try:
                with open(filepath, 'r', encoding='utf-8') as f:  # Open in read mode
                    content = f.read()

                    if config.get("remove_comments", True):
                        content = _remove_comments(content, filename)
                    if config.get("remove_whitespace", True):
                        content = _remove_whitespace(content)

                    bundled_content += content + "\n\n"  # Add content and separators
                    total_characters += len(content)

                print(f"Bundled: {filepath}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
                return None, None  # Return None if an error occurs

    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(bundled_content)
        print(f"Bundled code written to: {output_file}")
    except Exception as e:
        print(f"Error writing bundled code: {e}")
        return None, None

    return total_characters, len(bundled_content.encode('utf-8')) # Return total characters and total bytes

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
    parser = argparse.ArgumentParser(description="Bundles code into a single file.")
    parser.add_argument("project_root", help="Path to the project root directory.")
    parser.add_argument("-o", "--output", help="Path to the output file (default: bundled.txt).")
    parser.add_argument("-c", "--config", help="Path to the config file (default: config.json)", default="config.json")

    args = parser.parse_args()

    project_root = args.project_root
    output_file = args.output or f"bundle\\{os.path.basename(project_root)}.txt" # Updated output directory name
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

    total_characters, total_bytes = bundle_code(project_root, output_file, config)

    if total_characters is not None:
        print("Code bundling complete.")
        print(f"Total characters in bundled code: {total_characters}")

        approximate_tokens = total_characters / 4
        print(f"Approximate token count: {approximate_tokens:.0f}")
        print(f"Total bytes in bundled code: {total_bytes}")
    else:
        print("Code bundling failed.")