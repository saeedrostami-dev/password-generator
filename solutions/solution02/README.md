# Password Generator — Functional Approach

A Python project for learning function-based programming, software design, input validation, exception handling, and automated testing.

## About the Project

Password Generator is an educational project developed as part of my Python learning journey.

The main goal is to practice designing, implementing, testing, and organizing a Python project. This implementation uses standalone functions to generate different types of passwords.

This is Solution 02 of the repository. Solution 01 implements the same core functionality using object-oriented programming (OOP), allowing both approaches to be compared.

## Features

- **PIN Generator:** Generates numeric passwords of a specified length.
- **Random Password Generator:** Generates random passwords with optional numbers and symbols.
- **Memorable Password Generator:** Generates passwords using randomly selected words, with configurable word counts and separators.
- **Input Validation:** Validates function arguments and raises appropriate exceptions for invalid inputs.
- **Exception Handling:** Provides an informative error when the required NLTK words corpus is unavailable.
- **Automated Testing:** Uses `pytest` to test functionality, output characteristics, and invalid inputs.
- **Secure Randomness:** Uses Python's `secrets` module for random selection.

## Technologies

- Python
- Function-based programming
- `secrets`
- `string`
- NLTK
- `pytest`

## Project Structure

```text id="n7s1ka"
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

```bash id="z9a2w3"
git clone https://github.com/saeedrostami-dev/Password_Generator.git
```

### 2. Navigate to Solution 02

```bash id="c2d6p8"
cd Password_Generator/solutions/solution02
```

### 3. Create and activate a virtual environment

```bash id="m5v8r1"
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment using PowerShell:

```powershell id="q4t6x2"
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash id="u8j3w5"
python -m pip install -r requirements.txt
```

### 5. Download the NLTK words corpus

The memorable password generator uses the NLTK English words corpus.

```bash id="k2p7r9"
python -m nltk.downloader words
```

This download is normally required only once for the relevant Python environment. If the corpus is missing, the generator raises an informative `LookupError`.

## Usage

The following examples assume that the commands are run from the `solutions/solution02` directory.

### PIN Password

```python id="b4n8s6"
from src.main import generate_pin

password = generate_pin(length=6)

print(password)
```

### Random Password

```python id="e3f7h2"
from src.main import generate_random_password

password = generate_random_password(
    length=12,
    include_numbers=True,
    include_symbols=True,
)

print(password)
```

### Memorable Password

```python id="v6c1m9"
from src.main import generate_memorable_password

password = generate_memorable_password(
    word_count=3,
    separator="-",
)

print(password)
```

## Running Tests

Run the following command from the `solutions/solution02` directory:

```bash id="r5x2j8"
python -m pytest -v
```

The tests cover password generation, output characteristics, input validation, and error handling when the NLTK corpus is missing.

## Learning Objectives

Through this project, I am practicing:

- Designing functions with clear responsibilities.
- Organizing code into reusable functions.
- Choosing appropriate function parameters and return values.
- Validating input and handling exceptions.
- Using Python's `secrets` module for secure random selection.
- Writing automated tests with `pytest`.
- Using parameterized tests to reduce repetition.
- Organizing source code, tests, and project dependencies.
- Comparing functional and object-oriented approaches.
- Following a structured software development workflow.

## Future Improvements

Possible next steps include:

- Comparing the object-oriented and functional implementations.
- Improving test coverage and project documentation.
- Exploring additional password generation strategies.
- Refactoring repeated validation logic where appropriate.

## Disclaimer

This is an educational project created for learning and practice. It is not intended to be a production-ready password management solution.