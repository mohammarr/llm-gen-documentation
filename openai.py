import json

def json_to_markdown(json_data):
    # Convert the JSON data to a dictionary
    data = json.loads(json_data)
    
    # Initialize markdown string
    markdown = f"# {data['project']['name']}\n\n"
    markdown += f"> _Generated using Open AI 4o mini model._\n\n**Description**: {data['project']['description']}\n\n"
    
    markdown += "## Features\n"
    for feature in data['project']['features']:
        markdown += f"- {feature}\n"
    
    markdown += "\n## Technologies\n"
    for tech in data['project']['technologies']:
        markdown += f"- {tech}\n"
    
    markdown += "\n## Dependencies\n"
    for dep in data['project']['dependencies']:
        markdown += f"- {dep}\n"
    
    markdown += "\n## System Requirements\n"
    for requirement in data['system_requirements']['software']:
        markdown += f"### {requirement['name']}\n"
        markdown += f"**Version**: {requirement['version']}\n"
        markdown += f"**Description**: {requirement['description']}\n"
    
    markdown += "\n## Installation\n"
    for step in data['installation']['steps']:
        markdown += f"1. {step}\n"
    
    markdown += "\n## Usage Instructions\n"
    markdown += f"### Basic Usage\n{data['usage_instructions']['basic_usage'][0]}\n"
    markdown += "#### Example\n"
    if data['usage_instructions']['example']:
        markdown += f"```clojure\n"
        for line in data['usage_instructions']['example']:
            markdown += f"{line}\n"
        markdown += f"```\n"
    
    markdown += "\n## Configuration\n"
    markdown += f"{data['configuration']['details']}\n"
    
    markdown += "\n## API Documentation\n"
    for function in data['api_documentation']['functions']:
        markdown += f"### `{function['name']}`\n"
        markdown += f"**Description**: {function['description']}\n\n"
        markdown += f"**Parameters**:\n"
        for param in function['parameters']:
            markdown += f"- **{param['name']}**: {param['type']} - {param['description']}\n"
        markdown += f"**Returns**: {function['returns']['type']} - {function['returns']['description']}\n"
    
    markdown += "\n## Contributing Guidelines\n"
    for step in data['contributing_guidelines']['steps']:
        markdown += f"1. {step}\n"
    markdown += f"\n**Code of Conduct**: {data['contributing_guidelines']['code_of_conduct']}\n"
    
    markdown += "\n## License\n"
    markdown += f"**Type**: {data['license']['type']}\n\n"
    markdown += f"**Description**: {data['license']['description']}\n"
    
    return markdown

json_input = ""
with open("readme.json", "r") as file:
  json_input = file.read()
 
# Convert JSON to Markdown
markdown_output = json_to_markdown(json_input)

# Write to markdown file
with open("docs\\clojure_(openai).md", "w") as file:
    file.write(markdown_output)

print("README.md file has been generated successfully.")
