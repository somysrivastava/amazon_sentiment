# Amazon Review Sentiment Analysis using Python and Beautiful Soup

This project involves scraping and analyzing Amazon product reviews to determine the sentiment of customers' opinions about a product. The code utilizes Python along with Beautiful Soup for web scraping, and NLTK's VADER sentiment analysis model for sentiment classification. The goal is to help users make informed decisions about products based on sentiment analysis of reviews.

## Features

- Scrapes Amazon product reviews using Beautiful Soup and Requests libraries.
- Extracts reviewer names, star ratings, review titles, dates, and descriptions.
- Stores scraped data in a CSV file ('reviews.csv').
- Analyzes sentiment using VADER sentiment analysis model from NLTK.
- Classifies sentiment as Positive, Negative, or Neutral based on sentiment scores.
- Determines overall product sentiment (Good, Bad, or Average) based on sentiment proportions.
- Visualizes sentiment distribution and thresholds using Matplotlib.

## Getting Started

1. Clone the repository: `git clone https://github.com/somysrivastava/amazon_sentiment.git`
2. Install required Python packages: `pip install requests beautifulsoup4 pandas nltk matplotlib`
3. Run the provided Jupyter Notebook file or the Python script.
4. Enter the Amazon product review page URL when prompted.
5. The script will scrape reviews, perform sentiment analysis, and provide the product sentiment classification.

## Results

The script will display a bar chart illustrating the sentiment distribution of the Amazon reviews. It also calculates the proportion of positive and negative reviews and determines the overall product sentiment based on predefined thresholds. The sentiment analysis can help users quickly gauge the general opinion about a product before making a purchase decision.

## Example Usage

1. Input Amazon review page URL.
2. The script scrapes reviews, performs sentiment analysis, and classifies product sentiment.
3. Visualize sentiment distribution and thresholds.
4. Receive a classification of the product sentiment: Good, Bad, or Average.

## Contribution

Contributions to this project are welcome! Feel free to fork the repository, make enhancements, and submit pull requests.
