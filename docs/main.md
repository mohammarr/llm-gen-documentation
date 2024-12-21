# project.main - Clojure Utility Functions

> _Documentation generated using Gemini 1.5 flash model._ 

A small Clojure library providing utility functions for working with numbers.

## Analysis

* **Purpose:** Provides basic utility functions for common mathematical and string manipulation tasks.
* **Technologies:** Clojure
* **Frameworks:** None (Pure Clojure functions)
* **Dependencies:** None (Standalone library)
* **Requirements:** A Clojure environment (e.g., Leiningen, Babashka)

## Installation

No installation required. You can directly use the functions within your Clojure project.

**Steps:**

1. Ensure you have a Clojure environment set up (e.g., Leiningen, Babashka).

## Usage

To use the functions in this library, require the `project.main` namespace in your Clojure project:

```clojure
(require '[project.main :as main])

;; Example usage:
(println (main/greet "Alice")) ; Prints: Hello, Alice!
```

## API

### Available Functions

### `greet`

Greets a person by name.

**Parameters:**

* `name`: string - The name of the person to greet.

**Returns:**

A greeting string (e.g., "Hello, Alice!").

**Examples:**

```clojure
(main/greet "Alice") ; Output: Hello, Alice!
```

### `circle-area`

Calculates the area of a circle.

**Parameters:**

* `radius`: number - The radius of the circle.

**Returns:**

The area of the circle.

**Examples:**

```clojure
(main/circle-area 5) ; Output: 78.53975
```

### `is-positive?`

Checks if a number is positive.

**Parameters:**

* `num`: number - The number to check.

**Returns:**

"Yes" if the number is positive, "No" otherwise.

**Examples:**

```clojure
(main/is-positive? 5)  ; Output: Yes
```

```clojure
(main/is-positive? -2) ; Output: No
```

### `classify-number`

Classifies a number as positive, negative, or zero.

**Parameters:**

* `num`: number - The number to classify.

**Returns:**

"Positive", "Negative", or "Zero" depending on the number's value.

**Examples:**

```clojure
(main/classify-number 3)  ; Output: Positive
```

```clojure
(main/classify-number -1) ; Output: Negative
```

```clojure
(main/classify-number 0)  ; Output: Zero
```

### `factorial`

Calculates the factorial of a non-negative integer using recursion.

**Parameters:**

* `n`: integer - The non-negative integer.

**Returns:**

The factorial of n.

**Examples:**

```clojure
(main/factorial 5) ; Output: 120
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Make changes and write unit tests for your modifications.
3. Submit a pull request with a clear description of your changes.

## License

* **Type:** MIT License
* See LICENSE file for details.
