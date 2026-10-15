# Password Generator — Functional Approach

A Python project for learning function-based programming, software design, input validation, and automated testing.

## About the Project

Password Generator is an educational project developed as part of my Python learning journey.

The main goal is to practice the process of designing, implementing, testing, and organizing a Python project. This version focuses on a functional approach, using standalone functions to generate different types of passwords.

It provides the same core functionality as Solution 01, which uses object-oriented programming (OOP), allowing both approaches to be compared.

## Features

- **PIN Generator:** Generates numeric passwords of a specified length.
- **Random Password Generator:** Generates random passwords with optional numbers and symbols.
- **Memorable Password Generator:** Generates passwords using randomly selected words, with configurable word counts and separators.
- **Input Validation:** Validates function arguments and raises appropriate exceptions for invalid inputs.
- **Automated Testing:** Uses `pytest` to test functionality and input validation.
- **Secure Randomness:** Uses Python's `secrets` module for random selection.

## Technologies

- Python
- Function-based programming
- `secrets`
- `string`
- NLTK
- pytest

## Project Structure

```text
solution02/
├── README.md
├── requirements.txt
├── src/
│   └── main.py
└── tests/
    └── test_password.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/saeedrostami-dev/Password_Generator.git
```

### 2. Navigate to this solution

```bash
cd Password_Generator/solutions/solution02
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Download the NLTK words corpus

The memorable password generator uses the NLTK English words corpus.

```bash
python -m nltk.downloader words
```

## Usage

The following examples assume that the project is run from the `solution02` directory.

### PIN Password

```python
from src.main import generate_pin

password = generate_pin(length=6)

print(password)
```

### Random Password

```python
from src.main import generate_random_password

password = generate_random_password(
    length=12,
    include_numbers=True,
    include_symbols=True,
)

print(password)
```

### Memorable Password

```python
from src.main import generate_memorable_password

password = generate_memorable_password(
    word_count=3,
    separator="-",
)

print(password)
```

## Running Tests

Run the following command from the `solution02` directory:

```bash
python -m pytest -v
```

The test suite covers password generation, output characteristics, and invalid inputs.

## Learning Objectives

Through this project, I am practicing:

- Designing functions with clear responsibilities.
- Organizing code into reusable functions.
- Choosing appropriate function parameters and return values.
- Validating input and handling exceptions.
- Writing automated tests with `pytest`.
- Using parameterized tests to reduce repetition.
- Organizing source code, tests, and project dependencies.
- Comparing functional and object-oriented approaches.
- Following a structured software development workflow.

## Future Improvements

Possible next steps include:

- Comparing object-oriented and function-based designs.
- Improving test coverage and project documentation.
- Exploring additional password generation strategies.
- Refactoring repeated validation logic where appropriate.

## Disclaimer

This is an educational project created for learning and practice. It is not intended to be presented as a production-ready password management solution.