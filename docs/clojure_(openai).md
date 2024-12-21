# Math App

> _Generated using Open AI 4o mini model._

**Description**: A simple Clojure application that provides various utility functions to perform mathematical operations like greeting, calculating circle area, checking if a number is positive, classifying a number, and calculating factorials.

## Features
- Greets the user with a personalized message.
- Calculates the area of a circle given its radius.
- Checks whether a number is positive or negative.
- Classifies a number as Positive, Negative, or Zero.
- Calculates the factorial of a number.

## Technologies
- Clojure

## Dependencies
- No external dependencies.

## System Requirements
### Java Runtime Environment (JRE)
**Version**: 1.8 or higher
**Description**: Clojure requires Java to run, so make sure a compatible JRE is installed.
### Clojure
**Version**: 1.10.0 or higher
**Description**: Clojure is the language used to build this application.

## Installation
1. Ensure Java (JRE) is installed on your machine.
1. Download and install Clojure from the official website (https://clojure.org/).
1. Clone the repository or download the source code.
1. Navigate to the project directory and run the following command to run the app:
1.   $ lein run

## Usage Instructions
### Basic Usage
Run the main function to see examples of mathematical operations.
#### Example
```clojure
To run the app, execute the following command in your terminal:
  $ lein run
Expected output:
  Hello, World!
  78.53975
  No
  Zero
```

## Configuration
There are no external configuration files or environment variables required for this project. All functions are hardcoded with basic functionality.

## API Documentation
### `greet`
**Description**: Greets the user with a personalized message.

**Parameters**:
- **name**: String - The name of the user to greet.

**Returns**: String - Returns a greeting message string.
### `circle-area`
**Description**: Calculates the area of a circle given its radius.

**Parameters**:
- **radius**: Number - The radius of the circle.

**Returns**: Number - Returns the area of the circle.
### `is-positive?`
**Description**: Checks if the number is positive.

**Parameters**:
- **num**: Number - The number to check.

**Returns**: String - Returns 'Yes' if the number is positive, 'No' otherwise.
### `classify-number`
**Description**: Classifies a number as positive, negative, or zero.

**Parameters**:
- **num**: Number - The number to classify.

**Returns**: String - Returns a string indicating whether the number is 'Positive', 'Negative', or 'Zero'.
### `factorial`
**Description**: Calculates the factorial of a given number.

**Parameters**:
- **n**: Integer - The number to calculate the factorial of.

**Returns**: Integer - Returns the factorial of the number.

## Contributing Guidelines
1. Fork the repository.
1. Clone your fork to your local machine.
1. Create a new branch for your feature or fix.
1. Make your changes and write tests if applicable.
1. Commit your changes with clear commit messages.
1. Push your branch to your fork and submit a pull request.

**Code of Conduct**: Please follow the standard open-source code of conduct, respecting all contributors and maintaining a welcoming environment.

## License
**Type**: MIT

**Description**: The project is licensed under the MIT License. You can freely use, modify, and distribute the code.
