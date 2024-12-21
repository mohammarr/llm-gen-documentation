# Clojure Mathematics Utilities

> _Generated using Claude 3.5 Sonnet model in normal style._

A lightweight Clojure library providing basic mathematical operations and utilities.

## Overview

This library offers a collection of mathematical utility functions including geometric calculations, number classification, and basic mathematical operations. It's designed to be simple, efficient, and easy to integrate into other Clojure projects.

## Features

- Basic greeting functionality
- Geometric calculations (circle area)
- Number classification and analysis
- Mathematical operations (factorial)
- Positive number checking

## Requirements

- Clojure 1.8.0 or higher
- Java JDK 8 or higher

## Installation

Add the following dependency to your `project.clj`:

```clojure
[math-utils "0.1.0"]
```

## Usage

First, require the namespace in your Clojure file:

```clojure
(ns your-namespace
  (:require [math.utils :as utils]))
```

### Examples

```clojure
;; Greeting
(utils/greet "World")
;; => "Hello, World!"

;; Calculate circle area
(utils/circle-area 5)
;; => 78.53975

;; Check if number is positive
(utils/is-positive? -2)
;; => "No"

;; Classify a number
(utils/classify-number 0)
;; => "Zero"

;; Calculate factorial
(utils/factorial 5)
;; => 120
```

## API Documentation

### `greet [name]`
Returns a greeting string with the provided name.
- **Parameters**: `name` (string)
- **Returns**: String

### `circle-area [radius]`
Calculates the area of a circle given its radius.
- **Parameters**: `radius` (number)
- **Returns**: Number (area)

### `is-positive? [num]`
Checks if a number is positive.
- **Parameters**: `num` (number)
- **Returns**: String ("Yes" or "No")

### `classify-number [num]`
Classifies a number as positive, negative, or zero.
- **Parameters**: `num` (number)
- **Returns**: String ("Positive", "Negative", or "Zero")

### `factorial [n]`
Calculates the factorial of a non-negative integer.
- **Parameters**: `n` (non-negative integer)
- **Returns**: Number (factorial result)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```