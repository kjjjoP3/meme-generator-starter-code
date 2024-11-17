# Meme Generator CLI and Web App

## Project Overview
This project provides a simple Command-Line Interface (CLI) tool and a Flask web application for generating memes. 

### CLI Tool: `meme.py`
The CLI tool allows users to create memes directly from the terminal.

#### Usage
Run the tool using the following command:
```bash
python3 meme.py

#### Arguments
The script accepts three optional arguments:

```bash
--body: The text content of the quote (string).

```bash
--author: The author of the quote (string).

```bash
--path: The file path to an image (string).


#### If any argument is not provided, the script will randomly generate or select appropriate values.

#### Output
The tool returns the file path to the generated meme.