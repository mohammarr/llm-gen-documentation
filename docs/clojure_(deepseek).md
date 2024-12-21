# Math Utility Application


> _Generated using Deepseek model._

A simple Clojure application that provides utility functions for mathematical operations and number classification.

## Features

- Greeting function
- Calculate the area of a circle
- Check if a number is positive
- Classify a number as positive, negative, or zero
- Calculate the factorial of a number

## Technologies

- **Language**: Clojure

## System Requirements

- **OS**: Any OS with JVM support

- **Software**: Java Development Kit (JDK) 8 or higher, Clojure 1.10 or higher

- **Tools**: Leiningen (optional, for dependency management and project setup)

## Installation

- Ensure you have JDK 8 or higher installed on your system.

- Install Clojure by following the official [Clojure installation guide](https://clojure.org/guides/install_clojure).

- Clone the repository to your local machine using `git clone <repository-url>`.

- Navigate to the project directory: `cd math-utility-app`.

## Usage

To run the application, execute the following command in the terminal:

```bash

clojure -M -m math.app

```

This will invoke the `main` function, which demonstrates the usage of the utility functions.

### Examples

### `greet`

Prints a greeting message.

```clojure
(utils/greet "World")
;; Output: Hello, World!
```

### `circle-area`

Calculates the area of a circle given its radius.

```clojure
(utils/circle-area 5)
;; Output: 78.53975
```

### `is-positive?`

Checks if a number is positive.

```clojure
(utils/is-positive? -2)
;; Output: No
```

### `classify-number`

Classifies a number as positive, negative, or zero.

```clojure
(utils/classify-number 0)
;; Output: Zero
```

### `factorial`

Calculates the factorial of a number.

```clojure
(utils/factorial 5)
;; Output: 120
```

## Configuration

No specific configuration is required for this application. All functionality is self-contained within the provided Clojure namespaces.

## API Documentation

### Functions

### `greet`

- **Params**: ['name']

- **Description**: Returns a greeting message with the provided name.

### `circle-area`

- **Params**: ['radius']

- **Description**: Calculates the area of a circle using the given radius.

### `is-positive?`

- **Params**: ['num']

- **Description**: Checks if the provided number is positive and returns 'Yes' or 'No'.

### `classify-number`

- **Params**: ['num']

- **Description**: Classifies the provided number as positive, negative, or zero.

### `factorial`

- **Params**: ['n']

- **Description**: Calculates the factorial of the provided number.

## Contributing

- Fork the repository and create a new branch for your feature or bugfix.

- Ensure your code adheres to the Clojure coding standards.

- Write clear and concise commit messages.

- Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
