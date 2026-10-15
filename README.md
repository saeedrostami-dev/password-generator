# Password Generator

An educational Python project exploring different approaches to password generation, software design, input validation, and automated testing.

This repository implements the same core password generation features using two different programming styles: object-oriented programming and a functional approach.

## Implementations

### Solution 01 — Object-Oriented Programming (OOP)

The first implementation uses classes, inheritance, and abstraction to organize password generation strategies.

Features include:
- PIN password generation
- Random password generation with optional numbers and symbols
- Memorable password generation using randomly selected words
- Input validation and exception handling
- Automated tests with `pytest`

See [Solution 01 README](solutions/solution01/README.md) for installation instructions, examples, and details.

### Solution 02 — Functional Approach

The second implementation uses standalone functions to provide the same core password generation features.

Features include:
- PIN password generation
- Random password generation with optional numbers and symbols
- Memorable password generation using randomly selected words
- Input validation and exception handling
- Automated tests with `pytest`

See [Solution 02 README](solutions/solution02/README.md) for installation instructions, examples, and details.

## Project Structure

```text
Password_Generator/
├── README.md
└── solutions/
    ├── solution01/
    │   ├── README.md
    │   ├── requirements.txt
    │   ├── src/
    │   │   └── main.py
    │   └── tests/
    │       └── test_password.py
    └── solution02/
        ├── README.md
        ├── requirements.txt
        ├── src/
        │   └── main.py
        └── tests/
            └── test_password.py
```

## Getting Started

Choose the implementation you want to explore and navigate to its directory.

For example, to run Solution 01:

```bash
cd solutions/solution01
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m nltk.downloader words
python -m pytest -v
```

To run Solution 02, use the corresponding directory:

```bash
cd solutions/solution02
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m nltk.downloader words
python -m pytest -v
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

The NLTK words corpus is needed for memorable password generation when the default vocabulary is used. Downloading it is a one-time setup step for the relevant Python environment.

## Learning Goals

- Practice Python programming and project organization.
- Explore object-oriented and functional programming styles.
- Design reusable classes and functions.
- Validate inputs and handle exceptions.
- Write automated tests using `pytest`.
- Manage dependencies and virtual environments.
- Use Git and GitHub to track project development.

## Project Status

Both Solution 01 and Solution 02 are implemented. Each solution has its own source code, dependencies, tests, and README.

## Disclaimer

This is an educational project created for learning and practice. It is not intended to be a production-ready password management solution.