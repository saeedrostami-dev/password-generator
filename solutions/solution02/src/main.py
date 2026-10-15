import secrets
import string

import nltk


def generate_pin(length: int) -> str:
    """Generate a numeric PIN of a specified length."""

    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("Length must be an integer.")

    if length <= 0:
        raise ValueError("Length must be positive.")

    return "".join(
        secrets.choice(string.digits)
        for _ in range(length)
    )


def generate_random_password(
    length: int,
    include_numbers: bool = False,
    include_symbols: bool = False,
) -> str:
    """Generate a random password from configurable character sets."""

    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("Length must be an integer.")

    if length <= 0:
        raise ValueError("Length must be positive.")

    if not isinstance(include_numbers, bool):
        raise TypeError("include_numbers must be a boolean.")

    if not isinstance(include_symbols, bool):
        raise TypeError("include_symbols must be a boolean.")

    characters = string.ascii_letters

    if include_numbers:
        characters += string.digits

    if include_symbols:
        characters += string.punctuation

    required_characters = []

    if include_numbers:
        required_characters.append(secrets.choice(string.digits))

    if include_symbols:
        required_characters.append(secrets.choice(string.punctuation))

    if length < len(required_characters):
        raise ValueError(
            "Password length is too short for the selected options."
        )

    password_characters = required_characters.copy()

    for _ in range(length - len(password_characters)):
        password_characters.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


def generate_memorable_password(
    word_count: int = 4,
    separator: str = "-",
) -> str:
    """Generate a memorable password using randomly selected words."""

    if isinstance(word_count, bool) or not isinstance(word_count, int):
        raise TypeError("Word count must be an integer.")

    if word_count <= 0:
        raise ValueError("Word count must be positive.")

    if not isinstance(separator, str):
        raise TypeError("Separator must be a string.")

    try:
        words = nltk.corpus.words.words()
    except LookupError as exc:
        raise LookupError(
            "NLTK words corpus is missing. "
            "Download it using nltk.download('words')."
        ) from exc

    if not words:
        raise ValueError("The word list must not be empty.")

    selected_words = [
        secrets.choice(words).lower()
        for _ in range(word_count)
    ]

    return separator.join(selected_words)


if __name__ == "__main__":
    print("PIN:", generate_pin(6))
    print(
        "Random password:",
        generate_random_password(
            12,
            include_numbers=True,
            include_symbols=True,
        ),
    )
    print("Memorable password:", generate_memorable_password())
