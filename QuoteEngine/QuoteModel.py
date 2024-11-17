"""Represents a quote with its body and author."""

class QuoteModel:
    """Model representing a quote with two parts: body and author."""

    def __init__(self, body: str, author: str) -> None:
        """
        Initialize the QuoteModel instance.

        :param body: The main text of the quote.
        :param author: The person who authored the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """
        Return a string representation of the quote.

        :return: A string formatted as 'body - author'
        """
        return f"{self.body} - {self.author}"
