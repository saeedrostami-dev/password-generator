# Password Generator

A Python project for learning object-oriented programming (OOP), software design, input validation, and automated testing.

## About the Project

Password Generator is an educational project developed as part of my Python learning journey.

The main goal is to practice the process of designing, implementing, testing, and organizing a Python project. This version focuses on object-oriented programming (OOP), with different classes responsible for generating different types of passwords.

## Features

- **PIN Generator:** Generates numeric passwords.
- **Random Password Generator:** Generates random passwords with optional numbers and symbols.
- **Memorable Password Generator:** Generates passwords using randomly selected words, with configurable separators and capitalization.
- **Input Validation:** Validates constructor arguments and raises appropriate exceptions for invalid inputs.
- **Automated Testing:** Uses `pytest` to test functionality and input validation.
- **Secure Randomness:** Uses Python's `secrets` module for random password generation.

## Technologies

- Python
- Object-Oriented Programming (OOP)
- `secrets`
- `string`
- NLTK
- pytest

## Project Structure

```text
solution01/
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
git clone https://github.com/saeed-dev/password-generator.git
```

### 2. Navigate to this solution

```bash
cd Password_Generator/solutions/solution01
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Download the NLTK words corpus

The memorable password generator uses the NLTK English words corpus when a custom vocabulary is not provided.

```bash
python -m nltk.downloader words
```

## Usage

The following examples assume that the project is run from the `solution01` directory.

### PIN Password

```python
from src.main import PinPasswordGenerator

generator = PinPasswordGenerator(length=6)
password = generator.generate()

print(password)
```

### Random Password

```python
from src.main import RandomPasswordGenerator

generator = RandomPasswordGenerator(
    length=12,
    include_numbers=True,
    include_symbols=True,
)

password = generator.generate()

print(password)
```

### Memorable Password

```python
from src.main import MemorablePasswordGenerator

generator = MemorablePasswordGenerator(
    number_of_words=3,
    separator="-",
    capitalization=True,
)

password = generator.generate()

print(password)
```

## Running Tests

Run the following command from the `solution01` directory:

```bash
python -m pytest -v
```

The tests cover password generation, output characteristics, and invalid inputs.

## Learning Objectives

Through this project, I am practicing:

- Designing classes and defining clear responsibilities.
- Using inheritance and abstract base classes.
- Working with constructors, instance attributes, and methods.
- Validating input and handling exceptions.
- Writing automated tests with `pytest`.
- Using parameterized tests to reduce repetition.
- Organizing source code, tests, and project dependencies.
- Following a structured software development workflow.

## Future Improvements

Possible next steps include:

- Implementing a function-based version of the password generator.
- Comparing object-oriented and function-based designs.
- Improving test coverage and project documentation.
- Exploring additional password generation strategies.

## Disclaimer

This is an educational project created for learning and practice. It is not intended to be presented as a production-ready password management solution.
