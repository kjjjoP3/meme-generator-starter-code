"""Extracting quotes from a text file."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """TextIngestor class for handling text file quote extraction."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Extract quotes from a text file."""
        if not cls.can_ingest(path):
            raise ValueError("The file type is not supported")

        """List empty"""
        quotes = []

        try:
            with open(path, 'r', encoding='utf8') as file:
                for line in file:
                    parts = line.strip().split('-')
                    if len(parts) == 2:  # Ensures the line is in correct format
                        body, author = parts
                        quote = QuoteModel(body.strip(), author.strip())
                        quotes.append(quote)
        except FileNotFoundError:
            print(f"Error: The file '{path}' could not be found.")

        return quotes
