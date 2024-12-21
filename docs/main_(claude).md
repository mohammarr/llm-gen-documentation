# Number Utilities
> _Documentation generated using Claude 3.5 Sonnet model._ 

A Clojure library that provides utility functions for working with numbers and basic mathematical operations.

## Overview

This library includes functions for basic mathematical calculations, number classification, and greeting functionality. It's written in Clojure and provides a simple, functional approach to common numerical operations.

## Features

- Number classification (positive, negative, zero)
- Basic mathematical calculations (circle area, factorial)
- Positive number checking
- Greeting function

## Requirements

- Clojure 1.8.0 or higher
- Java Runtime Environment (JRE) 8 or higher

## Installation

Add the following dependency to your `project.clj`:

```clojure
[number-utilities "0.1.0"]
```

## Usage

First, require the namespace in your Clojure code:

```clojure
(ns your-project.core
  (:require [project.main :as utils]))
```

### Available Functions

#### Greeting
```clojure
(greet "World")
; => "Hello, World!"
```

#### Circle Area Calculation
```clojure
(circle-area 5)
; => 78.53975 ; Area of circle with radius 5
```

#### Number Classification
```clojure
(is-positive? 42)
; => "Yes"

(classify-number -7)
; => "Negative"

(classify-number 0)
; => "Zero"
```

#### Factorial Calculation
```clojure
(factorial 5)
; => 120 ; 5!
```

## API Documentation

### `greet [name]`
- **Description**: Returns a greeting string with the given name
- **Parameters**: `name` - A string representing the name to greet
- **Returns**: String with format "Hello, {name}!"

### `circle-area [radius]`
- **Description**: Calculates the area of a circle
- **Parameters**: `radius` - A number representing the circle's radius
- **Returns**: Number representing the circle's area

### `is-positive? [num]`
- **Description**: Checks if a number is positive
- **Parameters**: `num` - A number to check
- **Returns**: "Yes" if positive, "No" otherwise

### `classify-number [num]`
- **Description**: Classifies a number as positive, negative, or zero
- **Parameters**: `num` - A number to classify
- **Returns**: String "Positive", "Negative", or "Zero"

### `factorial [n]`
- **Description**: Calculates the factorial of a non-negative integer
- **Parameters**: `n` - A non-negative integer
- **Returns**: The factorial of n (n!)

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