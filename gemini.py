import json

def json_to_markdown(json_data):
  """Converts a JSON representation of a README to Markdown format."""

  markdown = f"# {json_data['title']}\n\n"
  markdown += f"> _Generated using Gemini 1.5 flash model._\n\n{json_data['description']}\n\n"

  # Analysis Section
  markdown += "## Analysis\n\n"
  markdown += f"* **Purpose:** {json_data['analysis']['purpose']}\n"
  markdown += f"* **Technologies:** {', '.join(json_data['analysis']['technologies'])}\n"
  markdown += (
      f"* **Frameworks:** {', '.join(json_data['analysis']['frameworks'])}\n"
  )
  markdown += f"* **Dependencies:** {', '.join(json_data['analysis']['dependencies'])}\n"
  markdown += f"* **Requirements:** {', '.join(json_data['analysis']['requirements'])}\n\n"

  # Documentation Sections
  markdown += "## Installation\n\n"
  markdown += f"{json_data['installation']['description']}\n\n"
  if json_data['installation'].get('steps'):
    markdown += "**Steps:**\n\n"
    for step in json_data['installation']['steps']:
      markdown += f"{step}\n"
    markdown += "\n"

  markdown += "## Usage\n\n"
  markdown += f"{json_data['usage']['description']}\n\n"
  markdown += f"```clojure\n{json_data['usage']['example']}\n```\n\n"

  markdown += "## API\n\n"
  markdown += f"### {json_data['api']['title']}\n\n"
  for function in json_data['api']['functions']:
    markdown += f"### `{function['name']}`\n\n"
    markdown += f"{function['description']}\n\n"

    if function.get('parameters'):
      markdown += "**Parameters:**\n\n"
      for param in function['parameters']:
        markdown += f"* `{param['name']}`: {param.get('type', '')} - {param['description']}\n"
      markdown += "\n"

    if function.get('returns'):
      markdown += "**Returns:**\n\n"
      markdown += f"{function['returns']['description']}\n\n"

    if function.get('examples'):
      markdown += "**Examples:**\n\n"
      for example in function['examples']:
        markdown += f"```clojure\n{example}\n```\n\n"

  # Add sections for Contributing and License if present
  if json_data.get('contributing'):
    markdown += "## Contributing\n\n"
    markdown += f"{json_data['contributing']['description']}\n\n"
    for guideline in json_data['contributing']['guidelines']:
      markdown += f"{guideline}\n"
    markdown += "\n"

  if json_data.get('license'):
    markdown += "## License\n\n"
    markdown += f"* **Type:** {json_data['license']['type']}\n"
    markdown += f"* {json_data['license']['text']}\n"

  return markdown

if __name__ == "__main__":
  with open("readme.json", "r") as f:
    json_data = json.load(f)

  markdown_output = json_to_markdown(json_data)

  with open("docs\clojure_(gemini).md", "w", encoding="utf-8") as f:
    f.write(markdown_output)

  print("README.md generated successfully!")