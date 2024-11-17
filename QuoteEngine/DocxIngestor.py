"""Handles the parsing of DOCX files."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """Class for ingesting quotes from DOCX files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a DOCX file and extract quotes.

        :param path: The file path of the DOCX file.
        :return: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise ValueError(f"File format not supported: {path}")

        quotes = []
        try:
            # Open the document using docx
            doc = docx.Document(path)

            for para in doc.paragraphs:
                content = para.text.strip()
                if content:
                    # Extract author and body by splitting on '-'
                    try:
                        author, body = map(
                            str.strip, content.split("-", maxsplit=1)
                        )
                        quotes.append(QuoteModel(body, author))
                    except ValueError:
                        print(f"Skipping malformed line: {content}")
        except Exception as error:
            raise Exception(f"Failed to parse DOCX file at {path}: {error}")

        return quotes
