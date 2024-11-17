"""Extract and parse contents from a PDF file."""

from typing import List
from pathlib import Path
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess
import random


class PDFIngestor(IngestorInterface):
    """Class responsible for processing PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a PDF file and extract quotes.

        :param path: Path to the PDF file.
        :return: A list of QuoteModel objects.
        """
        try:
            if not cls.can_ingest(path):
                raise ValueError(f"The file at {path} cannot be ingested.")

            # Generate a temporary file for text extraction
            tmp_file = Path(f'./tmp/pdf_{random.randint(0, 1000000)}.txt')

            # Convert PDF to text using an external utility
            subprocess.run(['pdftotext', path, str(tmp_file)], check=True)

            extracted_quotes = []
            with open(tmp_file, "r", encoding='utf8') as file:
                for line in file:
                    content = line.strip().split('-')
                    if len(content) == 2:  # Ensure the line contains both body and author
                        body, author = map(str.strip, content)
                        extracted_quotes.append(QuoteModel(body, author))

            return extracted_quotes
        except Exception as error:
            print(f"Error during PDF parsing: {error}")
            return []
