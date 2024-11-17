import os
import random
import requests
from flask import Flask, render_template, request, abort
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor


app = Flask(__name__)
meme_engine = MemeEngine.MemeEngine('./static')


def load_resources():
    """
    Load all quotes and images.

    This function gathers quote data from multiple file formats and collects
    all image paths from the specified directory.
    """
    # Load quotes from various sources
    quote_sources = [
        './_data/DogQuotes/DogQuotesTXT.txt',
        './_data/DogQuotes/DogQuotesDOCX.docx',
        './_data/DogQuotes/DogQuotesPDF.pdf',
        './_data/DogQuotes/DogQuotesCSV.csv'
    ]
    quotes = []
    for source in quote_sources:
        quotes.extend(Ingestor.parse(source))

    # Collect all image file paths
    images_directory = "./_data/photos/dog/"
    image_paths = [os.path.join(root, file) for root, _, files in os.walk(images_directory) for file in files]

    return quotes, image_paths


QUOTES, IMAGES = load_resources()


@app.route('/')
def meme_rand():
    """
    Generate a random meme.

    This route selects a random image and quote and creates a meme.
    """
    selected_image = random.choice(IMAGES)
    selected_quote = random.choice(QUOTES)

    meme_path = meme_engine.make_meme(selected_image, selected_quote.body, selected_quote.author)
    return render_template('meme.html', path=meme_path)


@app.route('/create', methods=['GET'])
def meme_form():
    """
    Render the form for user input.

    This route serves an HTML form to collect user input for creating a meme.
    """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """
    Generate a meme based on user input.

    This route processes form data submitted by the user to create a custom meme.
    """
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    try:
        # Download the image from the provided URL
        response = requests.get(image_url, allow_redirects=True)
        if response.status_code != 200:
            raise ValueError("Failed to download the image. Check the URL.")
        temp_image_name = f"{random.randint(0, 100000000)}.jpg"
        temp_image_path = os.path.join('./tmp', temp_image_name)

        with open(temp_image_path, 'wb') as image_file:
            image_file.write(response.content)

        # Create the meme using the downloaded image
        meme_path = meme_engine.make_meme(temp_image_path, body, author)
        return render_template('meme.html', path=meme_path)

    except Exception as error:
        abort(400, f"An error occurred: {error}")


if __name__ == "__main__":
    app.run()
