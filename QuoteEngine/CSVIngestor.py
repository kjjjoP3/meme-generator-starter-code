"""Handles the parsing of CSV files."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas as pd


class CSVIngestor(IngestorInterface):
    """Class for ingesting quotes from CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a CSV file and extract quotes.

        :param path: The file path of the CSV file.
        :return: A list of QuoteModel objects.
        """
        # Verify if the file can be ingested
        if not cls.can_ingest(path):
            raise ValueError(f"Unsupported file type at: {path}")

        quotes = []

        try:
            # Read the CSV file into a DataFrame
            data_frame = pd.read_csv(path, header=0)
        except pd.errors.EmptyDataError:
            # Handle cases where the file has no content
            print(f"The CSV file at {path} is empty.")
            return quotes
        except pd.errors.ParserError:
            # Handle cases where the CSV file has formatting issues
            print(f"Parsing error encountered in the CSV file at {path}.")
            return quotes

        # Process each row and create QuoteModel instances
        for _, row in data_frame.iterrows():
            if 'body' in row and 'author' in row:
                quote = QuoteModel(row['body'], row['author'])
                quotes.append(quote)

        return quotes
