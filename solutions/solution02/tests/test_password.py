
import string

import pytest

from src.main import (
    generate_memorable_password,
    generate_pin,
    generate_random_password,
)


# PIN password tests

def test_pin_has_expected_length():
    password = generate_pin(length=6)

    assert len(password) == 6


def test_pin_contains_only_digits():
    password = generate_pin(length=6)

    assert password.isdigit()


@pytest.mark.parametrize("length", [0, -1])
def test_pin_rejects_non_positive_length(length):
    with pytest.raises(
        ValueError,
        match="Length must be positive.",
    ):
        generate_pin(length=length)


@pytest.mark.parametrize("length", ["6", True, False, 6.5])
def test_pin_rejects_non_integer_length(length):
    with pytest.raises(
        TypeError,
        match="Length must be an integer.",
    ):
        generate_pin(length=length)


# Random password tests

def test_random_password_has_expected_length():
    password = generate_random_password(length=12)

    assert len(password) == 12


def test_random_password_contains_only_letters_by_default():
    password = generate_random_password(length=12)

    assert password.isalpha()


def test_random_password_includes_numbers_when_requested():
    password = generate_random_password(
        length=12,
        include_numbers=True,
    )

    assert any(char.isdigit() for char in password)


def test_random_password_includes_symbols_when_requested():
    password = generate_random_password(
        length=12,
        include_symbols=True,
    )

    assert any(char in string.punctuation for char in password)


def test_random_password_includes_numbers_and_symbols():
    password = generate_random_password(
        length=12,
        include_numbers=True,
        include_symbols=True,
    )

    assert any(char.isdigit() for char in password)
    assert any(char in string.punctuation for char in password)


def test_random_password_rejects_too_short_length():
    with pytest.raises(
        ValueError,
        match="Password length is too short",
    ):
        generate_random_password(
            length=1,
            include_numbers=True,
            include_symbols=True,
        )


# Memorable password tests

def test_memorable_password_has_expected_word_count():
    password = generate_memorable_password(word_count=4)

    assert len(password.split("-")) == 4


def test_memorable_password_uses_custom_separator():
    password = generate_memorable_password(
        word_count=3,
        separator="_",
    )

    assert len(password.split("_")) == 3


def test_memorable_password_rejects_non_integer_word_count():
    with pytest.raises(
        TypeError,
        match="Word count must be an integer.",
    ):
        generate_memorable_password(word_count="4")


@pytest.mark.parametrize("word_count", [0, -1])
def test_memorable_password_rejects_non_positive_word_count(word_count):
    with pytest.raises(
        ValueError,
        match="Word count must be positive.",
    ):
        generate_memorable_password(word_count=word_count)


@pytest.mark.parametrize("separator", [1, None, True])
def test_memorable_password_rejects_non_string_separator(separator):
    with pytest.raises(
        TypeError,
        match="Separator must be a string.",
    ):
        generate_memorable_password(separator=separator)
