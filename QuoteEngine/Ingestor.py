"""Determine the appropriate class to parse the contents of a file."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .TextIngestor import TextIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Class to manage the ingestion of various file formats."""

    importers = [DocxIngestor, TextIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given file and extract quotes.

        :param path: The file path to be processed.
        :return: A list of QuoteModel objects.
        """
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
        
        # Raise an exception if no valid parser is found
        raise ValueError(f"No suitable parser found for the file: {path}")
