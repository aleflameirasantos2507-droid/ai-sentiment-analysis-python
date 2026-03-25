# AI Sentiment Analysis (Python)

This project performs sentiment analysis on text using Python and Natural Language Processing (NLP).

## Features
- Sentiment classification (Positive, Negative, Neutral)
- Sentiment score output
- Multilingual support using automatic translation
- Analysis of multiple sentences from .txt files
- Final statistics with percentage distribution

## Technologies
- Python
- TextBlob
- deep-translator

## Installation

Clone the repository:
git clone https://github.com/your-username/ai-sentiment-analysis-python.git

Install dependencies:
pip install -r requirements.txt

Download TextBlob data:
python -m textblob.download_corpora

## Usage

Run the program:
python main.py

Choose:
- [1] Enter sentences manually
- [2] Analyze a .txt file

## Example

Sentence: "I love this project" → Sentiment: Positive [score: 0.50]

Sentence: "This is terrible" → Sentiment: Negative [score: -0.60]

## Project Structure

ai-sentiment-analysis/
│
├── README.md
├── main.py
└── requirements.txt

## Author

Alef Santos
