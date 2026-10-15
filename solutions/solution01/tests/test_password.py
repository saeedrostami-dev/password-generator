import string

import nltk
import pytest

from src.main import (
    MemorablePasswordGenerator,
    PinPasswordGenerator,
    RandomPasswordGenerator,
)


# Shared test data

VOCABULARY = ["apple", "river", "cloud"]


# PinPasswordGenerator tests

def test_pin_has_expected_length():
    generator = PinPasswordGenerator(length=6)

    password = generator.generate()

    assert len(password) == 6


def test_pin_contains_only_digits():
    generator = PinPasswordGenerator(length=6)

    password = generator.generate()

    assert password.isdigit()


@pytest.mark.parametrize(
    ("length", "error", "message"),
    [
        (0, ValueError, "Length must be positive."),
        (-1, ValueError, "Length must be positive."),
        ("6", TypeError, "Length must be an integer."),
        (True, TypeError, "Length must be an integer."),
        (False, TypeError, "Length must be an integer."),
        (6.5, TypeError, "Length must be an integer."),
    ],
)
def test_pin_rejects_invalid_length(length, error, message):
    with pytest.raises(error, match=message):
        PinPasswordGenerator(length=length)


# RandomPasswordGenerator tests

def test_random_password_has_expected_length():
    generator = RandomPasswordGenerator(length=12)

    password = generator.generate()

    assert len(password) == 12


@pytest.mark.parametrize(
    ("include_numbers", "include_symbols"),
    [
        (True, False),
        (False, True),
        (True, True),
    ],
)
def test_random_password_includes_requested_character_types(
    include_numbers,
    include_symbols,
):
    generator = RandomPasswordGenerator(
        length=12,
        include_numbers=include_numbers,
        include_symbols=include_symbols,
    )

    password = generator.generate()

    if include_numbers:
        assert any(character.isdigit() for character in password)

    if include_symbols:
        assert any(
            character in string.punctuation
            for character in password
        )


@pytest.mark.parametrize(
    ("length", "error", "message"),
    [
        (0, ValueError, "Length must be positive."),
        (-1, ValueError, "Length must be positive."),
        ("12", TypeError, "Length must be an integer."),
        (True, TypeError, "Length must be an integer."),
        (False, TypeError, "Length must be an integer."),
        (12.5, TypeError, "Length must be an integer."),
    ],
)
def test_random_password_rejects_invalid_length(
    length,
    error,
    message,
):
    with pytest.raises(error, match=message):
        RandomPasswordGenerator(length=length)


@pytest.mark.parametrize(
    ("option", "value", "message"),
    [
        (
            "include_numbers",
            1,
            "include_numbers must be a boolean.",
        ),
        (
            "include_numbers",
            "yes",
            "include_numbers must be a boolean.",
        ),
        (
            "include_symbols",
            1,
            "include_symbols must be a boolean.",
        ),
        (
            "include_symbols",
            "yes",
            "include_symbols must be a boolean.",
        ),
    ],
)
def test_random_password_rejects_invalid_options(
    option,
    value,
    message,
):
    options = {
        "length": 12,
        option: value,
    }

    with pytest.raises(TypeError, match=message):
        RandomPasswordGenerator(**options)


@pytest.mark.parametrize(
    ("include_numbers", "include_symbols", "length"),
    [
        (True, True, 1),
        (True, True, 0),
        (True, False, 0),
        (False, True, 0),
    ],
)
def test_random_password_rejects_length_too_short_for_options(
    include_numbers,
    include_symbols,
    length,
):
    if length == 0:
        expected_message = "Length must be positive."
    else:
        expected_message = (
            "Password length is too short for the selected options."
        )

    with pytest.raises(ValueError, match=expected_message):
        RandomPasswordGenerator(
            length=length,
            include_numbers=include_numbers,
            include_symbols=include_symbols,
        ).generate()


# MemorablePasswordGenerator tests

def test_memorable_password_has_expected_word_count():
    generator = MemorablePasswordGenerator(
        number_of_words=3,
        separator="-",
        vocabulary=VOCABULARY,
    )

    password = generator.generate()

    assert len(password.split("-")) == 3


def test_memorable_password_uses_separator():
    generator = MemorablePasswordGenerator(
        number_of_words=3,
        separator="-",
        vocabulary=VOCABULARY,
    )

    password = generator.generate()

    assert password.count("-") == 2


@pytest.mark.parametrize(
    ("capitalization", "expected"),
    [
        (True, str.capitalize),
        (False, str.lower),
    ],
)
def test_memorable_password_capitalization(capitalization, expected):
    generator = MemorablePasswordGenerator(
        number_of_words=3,
        separator="-",
        capitalization=capitalization,
        vocabulary=VOCABULARY,
    )

    password = generator.generate()
    words = password.split("-")

    assert all(word == expected(word) for word in words)


@pytest.mark.parametrize(
    ("number_of_words", "error", "message"),
    [
        (0, ValueError, "number_of_words must be positive."),
        (-1, ValueError, "number_of_words must be positive."),
        ("3", TypeError, "number_of_words must be an integer."),
        (True, TypeError, "number_of_words must be an integer."),
        (3.5, TypeError, "number_of_words must be an integer."),
    ],
)
def test_memorable_password_rejects_invalid_word_count(
    number_of_words,
    error,
    message,
):
    with pytest.raises(error, match=message):
        MemorablePasswordGenerator(
            number_of_words=number_of_words,
            vocabulary=VOCABULARY,
        )


@pytest.mark.parametrize(
    ("parameter", "value", "error", "message"),
    [
        (
            "separator",
            1,
            TypeError,
            "separator must be a string.",
        ),
        (
            "capitalization",
            "yes",
            TypeError,
            "capitalization must be a boolean.",
        ),
        (
            "vocabulary",
            "apple",
            TypeError,
            "vocabulary must be a list of strings.",
        ),
        (
            "vocabulary",
            [],
            ValueError,
            "vocabulary must not be empty.",
        ),
        (
            "vocabulary",
            ["apple", 123, "cloud"],
            TypeError,
            "All vocabulary items must be strings.",
        ),
        (
            "vocabulary",
            ["apple", "", "cloud"],
            ValueError,
            "Vocabulary items must not be empty.",
        ),
        (
            "vocabulary",
            ["apple", "   ", "cloud"],
            ValueError,
            "Vocabulary items must not be empty.",
        ),
    ],
)
def test_memorable_password_rejects_invalid_arguments(
    parameter,
    value,
    error,
    message,
):
    options = {
        "number_of_words": 3,
        "vocabulary": VOCABULARY,
        parameter: value,
    }

    with pytest.raises(error, match=message):
        MemorablePasswordGenerator(**options)


def test_memorable_password_raises_error_when_nltk_corpus_is_missing(
    monkeypatch,
):
    def raise_lookup_error():
        raise LookupError("Corpus not found")

    monkeypatch.setattr(
        nltk.corpus.words,
        "words",
        raise_lookup_error,
    )

    with pytest.raises(
        LookupError,
        match="NLTK words corpus is missing",
    ):
        MemorablePasswordGenerator(number_of_words=3)
