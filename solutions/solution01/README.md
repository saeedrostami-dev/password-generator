# Password Generator — Object-Oriented Approach

A Python project for learning object-oriented programming (OOP), software design, input validation, exception handling, and automated testing.

## About the Project

Password Generator is an educational project developed as part of my Python learning journey.

The main goal is to practice designing, implementing, testing, and organizing a Python project. This implementation uses object-oriented programming (OOP), with different classes responsible for generating different types of passwords.

This is Solution 01 of the repository. Solution 02 implements the same core functionality using a functional approach, making it possible to compare both programming styles.

## Features

- **PIN Generator:** Generates numeric passwords of a specified length.
- **Random Password Generator:** Generates random passwords with optional numbers and symbols.
- **Memorable Password Generator:** Generates passwords using randomly selected words, with configurable word counts, separators, and capitalization.
- **Input Validation:** Validates constructor arguments and raises appropriate exceptions for invalid inputs.
- **Exception Handling:** Provides an informative error when the required NLTK words corpus is unavailable.
- **Automated Testing:** Uses `pytest` to test functionality, output characteristics, and invalid inputs.
- **Secure Randomness:** Uses Python's `secrets` module for random password generation.

## Technologies

- Python
- Object-oriented programming (OOP)
- Abstract base classes and inheritance
- `secrets`
- `string`
- NLTK
- `pytest`

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
git clone https://github.com/saeedrostami-dev/Password_Generator.git
```

### 2. Navigate to Solution 01

```bash
cd Password_Generator/solutions/solution01
```

### 3. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment using PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Download the NLTK words corpus

The memorable password generator uses the NLTK English words corpus when a custom vocabulary is not provided.

```bash
python -m nltk.downloader words
```

This download is normally required only once for the relevant Python environment. If the corpus is missing, the generator raises an informative `LookupError`.

## Usage

The following examples assume that the commands are run from the `solutions/solution01` directory.

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

Run the following command from the `solutions/solution01` directory:

```bash
python -m pytest -v
```

The tests cover password generation, output characteristics, input validation, and error handling when the NLTK corpus is missing.

## Learning Objectives

Through this project, I am practicing:

- Designing classes with clear responsibilities.
- Using inheritance and abstract base classes.
- Working with constructors, instance attributes, and methods.
- Validating input and handling exceptions.
- Using Python's `secrets` module for secure random selection.
- Writing automated tests with `pytest`.
- Using parameterized tests to reduce repetition.
- Organizing source code, tests, and project dependencies.
- Comparing object-oriented and functional programming approaches.
- Following a structured software development workflow.

## Future Improvements

Possible next steps include:

- Comparing the object-oriented and functional implementations.
- Improving test coverage and project documentation.
- Exploring additional password generation strategies.
- Adding more configurable password generation options.

## Disclaimer

This is an educational project created for learning and practice. It is not intended to be a production-ready password management solution.