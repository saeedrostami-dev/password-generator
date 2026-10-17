# Password Generator

An educational Python project exploring different approaches to password generation, software design, input validation, automated testing, and building a simple web interface.

This repository implements the same core password generation features using two different programming styles: object-oriented programming and a functional approach. It also includes a Streamlit web app that provides a graphical interface for generating passwords.

## Implementations

### Solution 01 — Object-Oriented Programming (OOP)

The first implementation uses classes, inheritance, and abstraction to organize password generation strategies.

Features include:

- PIN password generation
- Random password generation with optional numbers and symbols
- Memorable password generation using randomly selected words
- Input validation and exception handling
- Automated tests with `pytest`

See the [Solution 01 README](solutions/solution01/README.md) for installation instructions, examples, and details.

### Solution 02 — Functional Approach

The second implementation uses standalone functions to provide the same core password generation features.

Features include:

- PIN password generation
- Random password generation with optional numbers and symbols
- Memorable password generation using randomly selected words
- Input validation and exception handling
- Automated tests with `pytest`

See the [Solution 02 README](solutions/solution02/README.md) for installation instructions, examples, and details.

### Streamlit App — Web Interface

The Streamlit app provides a simple graphical interface for using the password generators from Solution 02.

Features include:

- Select between PIN, random, and memorable passwords
- Customize password length and generation options
- Generate passwords through an interactive interface
- Display and copy generated passwords
- Clear generated passwords manually or when changing password types

The app reuses the password generation functions from Solution 02 rather than duplicating the core logic.

## Project Structure

```text
Password_Generator/
├── README.md
├── solutions/
│   ├── solution01/
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── src/
│   │   │   └── main.py
│   │   └── tests/
│   │       └── test_password.py
│   └── solution02/
│       ├── README.md
│       ├── requirements.txt
│       ├── src/
│       │   └── main.py
│       └── tests/
│           └── test_password.py
└── apps/
    └── streamlit_app/
        ├── app.py
        └── requirements.txt
```

## Getting Started

### Solution 01

Navigate to the solution directory, create a virtual environment, install dependencies, download the required NLTK corpus, and run the tests.

```bash
cd solutions/solution01
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m nltk.downloader words
python -m pytest -v
```

### Solution 02

```bash
cd solutions/solution02
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m nltk.downloader words
python -m pytest -v
```

### Run the Streamlit App

First, install the app's dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r apps/streamlit_app/requirements.txt
```

Then launch the app from the repository root:

```bash
python -m streamlit run apps/streamlit_app/app.py
```

Streamlit will provide a local URL that you can open in your browser.

On Windows, activate a virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

The NLTK `words` corpus is needed for memorable password generation when the default vocabulary is used. Downloading it is a one-time setup step for the relevant Python environment:

```bash
python -m nltk.downloader words
```

## Learning Goals

- Practice Python programming and project organization.
- Explore object-oriented and functional programming styles.
- Design reusable classes and functions.
- Validate inputs and handle exceptions.
- Write automated tests using `pytest`.
- Manage dependencies and virtual environments.
- Build a simple web interface using Streamlit.
- Reuse existing Python modules in a separate application.
- Use Git and GitHub to track project development.

## Project Status

- Solution 01: Implemented with automated tests.
- Solution 02: Implemented with automated tests.
- Streamlit app: Implemented with interactive password generation and display controls.

## Disclaimer

This is an educational project created for learning and practice. It is not intended to be a production-ready password management solution.
