"""Define an abstract base class for data ingestion."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An abstract base class to define ingestion behavior."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Verify if the file type can be processed.

        :param path: The path to the file being checked.
        :return: True if the file extension is supported, otherwise False.
        """
        file_extension = path.split('.')[-1].lower()
        return file_extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Abstract method to parse a file and extract quotes.

        :param path: The file path to be processed.
        :return: A list of QuoteModel objects.
        """
        pass
