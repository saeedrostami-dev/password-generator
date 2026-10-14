# Password Generator

A Python project for generating secure and customizable passwords.

This repository explores different approaches to implementing the same project, with a focus on clean code, software design, and automated testing.

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
        └── (planned)
```

## Implementations

### Solution 01 — Object-Oriented Programming (OOP)

The first implementation uses object-oriented programming principles to organize password generation strategies.

- Different password generation strategies
- Class-based design and abstraction
- Automated tests with pytest

See [Solution 01 README](solutions/solution01/README.md) for details.

### Solution 02 — Functional Approach

Planned: a function-based implementation of the same project, allowing a comparison between object-oriented and functional styles.

## Getting Started

To run the first solution:

```bash
cd solutions/solution01
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -v
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Learning Goals

- Practice Python programming and project organization
- Explore object-oriented design and alternative implementation styles
- Write and run automated tests
- Use Git and GitHub to track project development

## Status

Solution 01 is implemented. Solution 02 is planned.
