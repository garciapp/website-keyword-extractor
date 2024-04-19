# Website Keyword Extractor

## Introduction
This Python application allows users to extract keywords from the text content of a website. It utilizes web scraping techniques and natural language processing (NLP) to analyze the textual data and identify the most relevant words.

## Features
- Extract keywords from any website by providing its URL.
- Specify the number of keywords to extract.
- Option to include or exclude short words from the analysis.
- User-friendly graphical interface built with Tkinter.

## Requirements
- Python 3.x
- Tkinter
- Requests
- Beautiful Soup 4
- NLTK (Natural Language Toolkit)
    ### Installation
    To install the required dependencies, run the following command in your command prompt (cmd):

        pip install -r requirements.txt

    Ensure that you have Python and pip installed on your system.




## How to Use
1. Run the script.
2. Enter the URL of the website you want to analyze.
3. Specify the number of keywords to extract.
4. Choose whether to include short words (less than 3 letters) in the analysis.
5. Click "Extract Keywords" to start the process.
6. The extracted keywords and their frequencies will be displayed.

## Notes
- Ensure that all required Python packages are installed.
- The accuracy of keyword extraction may vary depending on the quality and structure of the website's content.
