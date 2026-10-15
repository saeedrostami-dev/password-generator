import secrets
import string
from abc import ABC, abstractmethod

import nltk


class PasswordGenerator(ABC):
    """Abstract base class for password generators."""

    @abstractmethod
    def generate(self) -> str:
        """Generate and return a password."""
        pass


class PinPasswordGenerator(PasswordGenerator):
    """Generate a numeric PIN of a specified length."""

    def __init__(self, length: int) -> None:
        """
        Initialize the PIN generator.

        Args:
            length: Number of digits in the PIN.

        Raises:
            TypeError: If length is not an integer.
            ValueError: If length is not positive.
        """
        if isinstance(length, bool) or not isinstance(length, int):
            raise TypeError("Length must be an integer.")

        if length <= 0:
            raise ValueError("Length must be positive.")

        self.length = length

    def generate(self) -> str:
        """Generate a PIN containing only digits."""
        return "".join(
            secrets.choice(string.digits)
            for _ in range(self.length)
        )


class RandomPasswordGenerator(PasswordGenerator):
    """Generate a random password from configurable character sets."""

    def __init__(
        self,
        length: int,
        include_numbers: bool = False,
        include_symbols: bool = False,
    ) -> None:
        """
        Initialize the random password generator.

        Args:
            length: Number of characters in the password.
            include_numbers: Whether to include at least one digit.
            include_symbols: Whether to include at least one symbol.

        Raises:
            TypeError: If an argument has an invalid type.
            ValueError: If length is not positive.
        """
        if isinstance(length, bool) or not isinstance(length, int):
            raise TypeError("Length must be an integer.")

        if length <= 0:
            raise ValueError("Length must be positive.")

        if not isinstance(include_numbers, bool):
            raise TypeError("include_numbers must be a boolean.")

        if not isinstance(include_symbols, bool):
            raise TypeError("include_symbols must be a boolean.")

        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols

        self.characters = string.ascii_letters

        if self.include_numbers:
            self.characters += string.digits

        if self.include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        """Generate a password that satisfies the selected options."""
        required_characters: list[str] = []

        if self.include_numbers:
            required_characters.append(
                secrets.choice(string.digits)
            )

        if self.include_symbols:
            required_characters.append(
                secrets.choice(string.punctuation)
            )

        if self.length < len(required_characters):
            raise ValueError(
                "Password length is too short for the selected options."
            )

        password_characters = required_characters.copy()

        for _ in range(self.length - len(password_characters)):
            password_characters.append(
                secrets.choice(self.characters)
            )

        secrets.SystemRandom().shuffle(password_characters)

        return "".join(password_characters)


class MemorablePasswordGenerator(PasswordGenerator):
    """Generate a password by combining randomly selected words."""

    def __init__(
        self,
        number_of_words: int,
        separator: str = ",",
        capitalization: bool = False,
        vocabulary: list[str] | None = None,
    ) -> None:
        """
        Initialize the memorable password generator.

        Args:
            number_of_words: Number of words in the password.
            separator: String used to join the selected words.
            capitalization: Whether to capitalize each word.
            vocabulary: List of words to choose from. If None, use NLTK's
                English words corpus.

        Raises:
            TypeError: If an argument has an invalid type.
            ValueError: If number_of_words is not positive or the
                vocabulary is empty or contains empty strings.
            LookupError: If the required NLTK corpus is unavailable.
        """
        if (
            isinstance(number_of_words, bool)
            or not isinstance(number_of_words, int)
        ):
            raise TypeError("number_of_words must be an integer.")

        if number_of_words <= 0:
            raise ValueError("number_of_words must be positive.")

        if not isinstance(separator, str):
            raise TypeError("separator must be a string.")

        if not isinstance(capitalization, bool):
            raise TypeError("capitalization must be a boolean.")

        if vocabulary is None:
            try:
                vocabulary = nltk.corpus.words.words()
            except LookupError as exc:
                raise LookupError(
                    "NLTK words corpus is missing. "
                    "Download it using "
                    "'python -m nltk.downloader words'."
                ) from exc
        else:
            if not isinstance(vocabulary, list):
                raise TypeError("vocabulary must be a list of strings.")

            if not vocabulary:
                raise ValueError("vocabulary must not be empty.")

            if not all(isinstance(word, str) for word in vocabulary):
                raise TypeError("All vocabulary items must be strings.")

            if not all(word.strip() for word in vocabulary):
                raise ValueError("Vocabulary items must not be empty.")

        self.vocabulary = vocabulary
        self.number_of_words = number_of_words
        self.separator = separator
        self.capitalization = capitalization

    def generate(self) -> str:
        """Generate a password by joining randomly selected words."""
        words = [
            secrets.choice(self.vocabulary)
            for _ in range(self.number_of_words)
        ]

        if self.capitalization:
            words = [word.capitalize() for word in words]

        return self.separator.join(words)


def main() -> None:
    """Demonstrate the available password generators."""

    pin_generator = PinPasswordGenerator(length=6)
    print(f"PIN: {pin_generator.generate()}")

    random_generator = RandomPasswordGenerator(
        length=8,
        include_numbers=True,
        include_symbols=True,
    )
    print(f"Random: {random_generator.generate()}")

    memorable_generator = MemorablePasswordGenerator(
        number_of_words=3,
        separator="-",
        capitalization=True,
    )
    print(f"Memorable: {memorable_generator.generate()}")


if __name__ == "__main__":
    main()
