import os
import random
import argparse
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor


def generate_meme(path: str = None, body: str = None, author: str = None) -> str:
    """
    Generate a meme using an image and a quote.

    :param path: Path to an image file (optional).
    :param body: The body of the quote (optional).
    :param author: The author of the quote (required if body is provided).
    :return: The file path to the generated meme.
    """
    # Select a random image if no path is provided
    if not path:
        images_folder = os.path.join("_data", "photos", "dog")
        image_files = [
            os.path.join(images_folder, img)
            for img in os.listdir(images_folder)
        ]
        path = random.choice(image_files)

    # Generate a random quote if no body is provided
    if not body:
        quote_sources = [
            './_data/DogQuotes/DogQuotesTXT.txt',
            './_data/DogQuotes/DogQuotesDOCX.docx',
            './_data/DogQuotes/DogQuotesPDF.pdf',
            './_data/DogQuotes/DogQuotesCSV.csv'
        ]
        quotes = []
        for source in quote_sources:
            quotes.extend(Ingestor.parse(source))
        selected_quote = random.choice(quotes)
    else:
        # Validate that both body and author are provided
        if not author:
            raise ValueError("Author is required when body is provided.")
        selected_quote = QuoteModel(body, author)

    # Create the meme
    meme_generator = MemeEngine.MemeEngine('./tmp')
    result_path = meme_generator.make_meme(
        path, selected_quote.body, selected_quote.author
    )
    print("Generated Meme Path: ", result_path)
    return result_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Meme Generator")
    parser.add_argument(
        '--path', type=str,
        default='./_data/photos/dog/xander_1.jpg',
        help='Path to an image file.'
    )
    parser.add_argument(
        '--body', type=str, default=None,
        help='Quote body.'
    )
    parser.add_argument(
        '--author', type=str, default=None,
        help='Quote author.'
    )
    args = parser.parse_args()

    try:
        meme_path = generate_meme(args.path, args.body, args.author)
        print(f"Meme successfully created: {meme_path}")
    except Exception as error:
        print(f"Failed to generate meme: {error}")
