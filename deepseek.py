import json

def json_to_markdown(json_data):
    """
    Converts a JSON structure into a Markdown-formatted string.
    """
    markdown = []

    # Project Section
    markdown.append("# {name}\n\n".format(**json_data["project"]))
    markdown.append("> _Generated using Deepseek model._\n\n{description}\n".format(**json_data["project"]))
    markdown.append("## Features\n")
    markdown.append("- " + "\n- ".join(json_data["project"]["features"]) + "\n")

    # Technologies Section
    markdown.append("## Technologies\n")
    markdown.append("- **Language**: {language}\n".format(**json_data["technologies"]))
    if json_data["technologies"]["frameworks"]:
        markdown.append("- **Frameworks**: {}\n".format(", ".join(json_data["technologies"]["frameworks"])))
    if json_data["technologies"]["dependencies"]:
        markdown.append("- **Dependencies**: {}\n".format(", ".join(json_data["technologies"]["dependencies"])))

    # System Requirements Section
    markdown.append("## System Requirements\n")
    markdown.append("- **OS**: {}\n".format(json_data["system_requirements"]["os"]))
    markdown.append("- **Software**: {}\n".format(", ".join(json_data["system_requirements"]["software"])))
    if json_data["system_requirements"]["tools"]:
        markdown.append("- **Tools**: {}\n".format(", ".join(json_data["system_requirements"]["tools"])))

    # Installation Section
    markdown.append("## Installation\n")
    for step in json_data["installation"]["steps"]:
        markdown.append("- " + step + "\n")

    # Usage Section
    markdown.append("## Usage\n")
    for instruction in json_data["usage"]["instructions"]:
        markdown.append(instruction + "\n")
    markdown.append("### Examples\n")
    for example in json_data["usage"]["examples"]:
        markdown.append("### `{function}`\n".format(**example))
        markdown.append("{description}\n".format(**example))
        markdown.append("```clojure\n{example}\n```\n".format(**example))

    # Configuration Section
    markdown.append("## Configuration\n")
    markdown.append("{details}\n".format(**json_data["configuration"]))

    # API Documentation Section
    markdown.append("## API Documentation\n")
    if json_data["api_documentation"]["functions"]:
        markdown.append("### Functions\n")
        for func in json_data["api_documentation"]["functions"]:
            markdown.append("### `{name}`\n".format(**func))
            markdown.append("- **Params**: {params}\n".format(**func))
            markdown.append("- **Description**: {description}\n".format(**func))

    # Contributing Section
    markdown.append("## Contributing\n")
    for guideline in json_data["contributing"]["guidelines"]:
        markdown.append("- " + guideline + "\n")

    # License Section
    markdown.append("## License\n")
    markdown.append("{details}\n".format(**json_data["license"]))

    return "\n".join(markdown)


def main():
    json_data = {
        "project": {
            "name": "Math Utility Application",
            "description": "A simple Clojure application that provides utility functions for mathematical operations and number classification.",
            "features": [
                "Greeting function",
                "Calculate the area of a circle",
                "Check if a number is positive",
                "Classify a number as positive, negative, or zero",
                "Calculate the factorial of a number"
            ]
        },
        "technologies": {
            "language": "Clojure",
            "frameworks": [],
            "dependencies": []
        },
        "system_requirements": {
            "os": "Any OS with JVM support",
            "software": [
                "Java Development Kit (JDK) 8 or higher",
                "Clojure 1.10 or higher"
            ],
            "tools": [
                "Leiningen (optional, for dependency management and project setup)"
            ]
        },
        "installation": {
            "steps": [
                "Ensure you have JDK 8 or higher installed on your system.",
                "Install Clojure by following the official [Clojure installation guide](https://clojure.org/guides/install_clojure).",
                "Clone the repository to your local machine using `git clone <repository-url>`.",
                "Navigate to the project directory: `cd math-utility-app`."
            ]
        },
        "usage": {
            "instructions": [
                "To run the application, execute the following command in the terminal:",
                "```bash",
                "clojure -M -m math.app",
                "```",
                "This will invoke the `main` function, which demonstrates the usage of the utility functions."
            ],
            "examples": [
                {
                    "function": "greet",
                    "description": "Prints a greeting message.",
                    "example": "(utils/greet \"World\")\n;; Output: Hello, World!"
                },
                {
                    "function": "circle-area",
                    "description": "Calculates the area of a circle given its radius.",
                    "example": "(utils/circle-area 5)\n;; Output: 78.53975"
                },
                {
                    "function": "is-positive?",
                    "description": "Checks if a number is positive.",
                    "example": "(utils/is-positive? -2)\n;; Output: No"
                },
                {
                    "function": "classify-number",
                    "description": "Classifies a number as positive, negative, or zero.",
                    "example": "(utils/classify-number 0)\n;; Output: Zero"
                },
                {
                    "function": "factorial",
                    "description": "Calculates the factorial of a number.",
                    "example": "(utils/factorial 5)\n;; Output: 120"
                }
            ]
        },
        "configuration": {
            "details": "No specific configuration is required for this application. All functionality is self-contained within the provided Clojure namespaces."
        },
        "api_documentation": {
            "endpoints": [],
            "functions": [
                {
                    "name": "greet",
                    "params": ["name"],
                    "description": "Returns a greeting message with the provided name."
                },
                {
                    "name": "circle-area",
                    "params": ["radius"],
                    "description": "Calculates the area of a circle using the given radius."
                },
                {
                    "name": "is-positive?",
                    "params": ["num"],
                    "description": "Checks if the provided number is positive and returns 'Yes' or 'No'."
                },
                {
                    "name": "classify-number",
                    "params": ["num"],
                    "description": "Classifies the provided number as positive, negative, or zero."
                },
                {
                    "name": "factorial",
                    "params": ["n"],
                    "description": "Calculates the factorial of the provided number."
                }
            ]
        },
        "contributing": {
            "guidelines": [
                "Fork the repository and create a new branch for your feature or bugfix.",
                "Ensure your code adheres to the Clojure coding standards.",
                "Write clear and concise commit messages.",
                "Submit a pull request with a detailed description of your changes."
            ]
        },
        "license": {
            "name": "MIT License",
            "details": "This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details."
        }
    }

    # Convert JSON to Markdown
    markdown_content = json_to_markdown(json_data)

    # Save to README.md
    with open("docs\clojure_(deepseek).md", "w") as readme_file:
        readme_file.write(markdown_content)

    print("README.md has been generated successfully!")


if __name__ == "__main__":
    main()