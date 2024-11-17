"""MemeEngine module."""

from PIL import Image, ImageDraw
import random


class MemeEngine:
    """A class responsible for generating memes with added text."""

    def __init__(self, output_dir: str):
        """
        Initialize the MemeEngine with the output directory.

        :param output_dir: Directory where generated memes will be stored.
        """
        self.output_dir = output_dir

    def make_meme(self, 
                  img_path: str, 
                  text: str, 
                  author: str, 
                  width: int = 500) -> str:
        """
        Create a meme by overlaying text onto an image.

        :param img_path: Path to the input image.
        :param text: Quote text to overlay.
        :param author: Author of the quote.
        :param width: Desired width for resizing the image.
        :return: Path to the saved meme image.
        """
        try:
            # Load the image from the given path
            image = Image.open(img_path)
        except Exception as error:
            print(f"Error loading image from {img_path}: {error}")
            return ""

        # Calculate the new height maintaining the aspect ratio
        aspect_ratio = width / float(image.size[0])
        height = int(aspect_ratio * float(image.size[1]))
        image = image.resize((width, height), Image.NEAREST)

        # Replace unwanted characters in text and author
        text = text.replace("\u2019", "")
        author = author.replace("\u2019", "")

        # Randomize position for text placement
        x_pos = random.randint(0, int(width / 2))
        y_pos = random.randint(0, int(height / 2))

        # Draw the text on the image
        draw = ImageDraw.Draw(image)
        draw.text((x_pos, y_pos), text, fill='white')
        draw.text((x_pos, y_pos + 20), f"   - {author}", fill='white')

        # Save the modified image
        try:
            output_filename = f"{self.output_dir}/{random.randint(0, 1000)}.jpg"
            image.save(output_filename, "JPEG")
        except Exception as error:
            print(f"Error saving the image to {output_filename}: {error}")
            return ""

        return output_filename
