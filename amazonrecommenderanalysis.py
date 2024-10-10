# -*- coding: utf-8 -*-
"""AmazonRecommenderAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RBoP9onBDCIUtw0H4hrEJ-GuMCHyKSyZ
"""

pip install vaderSentiment

"""Amazon Recommender System

Welcome to our Amazon Review Sentiment Analysis tool! Designed to simplify the process of understanding Amazon product reviews, our software utilizes advanced natural language processing techniques to extract key information and assess sentiment. By categorizing reviews as positive, negative, or neutral, we provide valuable insights for informed decision-making. Our user-friendly interface offers clear visualizations of sentiment distribution, enabling quick comprehension of product sentiment trends. Whether you're a consumer seeking purchasing insights or a seller aiming to understand customer satisfaction, our tool is tailored to meet your needs. Input the Amazon product review page URL to initiate the analysis process and make confident purchasing decisions.
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import random
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

headers = {
    'authority': 'www.amazon.in',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

def reviewsHtml(url, len_page):
    soups = []
    for page_no in range(1, len_page + 1):
        params = {
            'ie': 'UTF8',
            'reviewerType': 'all_reviews',
            'filterByStar': 'critical',
            'pageNumber': page_no,
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        soups.append(soup)
    return soups

def getReviews(html_data):
    data_dicts = []
    boxes = html_data.select('div[data-hook="review"]')
    for box in boxes:
        try:
            name = box.select_one('[class="a-profile-name"]').text.strip()
        except Exception as e:
            name = 'N/A'
        try:
            stars = box.select_one('[data-hook="review-star-rating"]').text.strip().split(' out')[0]
        except Exception as e:
            stars = 'N/A'
        try:
            title = box.select_one('[data-hook="review-title"]').text.strip()
        except Exception as e:
            title = 'N/A'
        try:
            datetime_str = box.select_one('[data-hook="review-date"]').text.strip().split(' on ')[-1]
            date = datetime.strptime(datetime_str, '%B %d, %Y').strftime("%d/%m/%Y")
        except Exception as e:
            date = 'N/A'
        try:
            description = box.select_one('[data-hook="review-body"]').text.strip()
        except Exception as e:
            description = 'N/A'
        data_dict = {
            'Name' : name,
            'Stars' : stars,
            'Title' : title,
            'Date' : date,
            'Description' : description
        }
        data_dicts.append(data_dict)
    return data_dicts

print("Before proceeding, ensure you have the URL of the Amazon product review page ready. Once prompted, input the URL to initiate the analysis process")
print("***"*50)
print('\n')

reviews_url = input("Enter the Amazon product review page URL: ")
# reviews url 1=Earphones: "https://www.amazon.in/Amazon-Earphones-Drivers-Controller-Oneplus/product-reviews/B0BZCFJBS1/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
#reviews url 2=boat max smart watch: "https://www.amazon.in/boAt-Wave-Ultima-Max-Monitoring/product-reviews/B0BGGSGG35/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
#reviews ur 3=Bata Mens Shoe  "https://www.amazon.in/Bata-Sail-remo-aw19-m3-Black-Uniform-Dress/product-reviews/B0B59TPTDL/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
len_page = 10

html_datas = reviewsHtml(reviews_url, len_page)

reviews = []
for html_data in html_datas:
    review = getReviews(html_data)
    reviews += review
df = pd.DataFrame(reviews)

print(reviews)

df.to_csv('reviews.csv', index=False)

df.head(50)

reviews = df[['Name', 'Description']].copy()

analyzer = SentimentIntensityAnalyzer()

def classify_sentiment(text):
    sentiment_score = analyzer.polarity_scores(text)['compound']
    if sentiment_score >= 0.05:
        return 'Positive'
    elif sentiment_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

reviews['sentiment'] = reviews['Description'].apply(classify_sentiment)
sentiment_counts = reviews['sentiment'].value_counts()

total_reviews = sentiment_counts.sum()
proportion_positive = sentiment_counts.get('Positive',0) / total_reviews
proportion_negative = sentiment_counts.get('Negative',0) / total_reviews

good_threshold = 0.6
bad_threshold = 0.4

if proportion_positive >= good_threshold:
    product_sentiment = 'A Good Product, \n This product shows promise, garnering positive sentiment and feedback, \n suggesting it may be a worthwhile choice for consumers consideration.'
elif proportion_negative >= bad_threshold:
    product_sentiment = 'A Bad Product, \n While this product may not meet expectations, indicating potential concerns, \n its prudent to explore alternatives for a more satisfying experience'
else:
    product_sentiment = 'An Average Product \n This product demonstrates middling performance,\n suggesting a neutral stance, which may warrant further evaluation to determine its suitability.'

print("Total number of reviews collected= ",total_reviews)
print("Good Threshold: ",good_threshold)
print("Bad Threshold:",bad_threshold)
print("Calculated proposition positive:", proportion_positive)
print("Calculated proposition negative:", proportion_negative)
print("Product Sentiment:", product_sentiment)

print("\n"*5)
print("***"*100)
print("Welcome to our Amazon Review Sentiment Analysis tool! \nDesigned to simplify the process of understanding Amazon product reviews, \nour software utilizes advanced natural language processing techniques to extract key information and assess sentiment. \nBy categorizing reviews as positive, negative, or neutral, we provide valuable insights for informed decision-making. \nOur user-friendly interface offers clear visualizations of sentiment distribution, enabling quick comprehension of product sentiment trends. \nWhether you're a consumer seeking purchasing insights or a seller aiming to understand customer satisfaction, our tool is tailored to meet your needs. \n\nInput the Amazon product review page URL to initiate the analysis process and make confident purchasing decisions.")
print("\n")
print("***"*100)
print("\n")
print("\n")
print("Entered URL of Amazon Poduct:",reviews_url)
print("\n")
print("\n")
print("\n")
print("OUTPUT")
print("\n")
print("\n")
plt.bar(sentiment_counts.index, sentiment_counts.values, color=['green', 'red', 'blue'], label='Sentiment')
plt.axhline(y=total_reviews * good_threshold, color='g', linestyle='--', label='Good Threshold')
plt.axhline(y=total_reviews * bad_threshold, color='r', linestyle='--', label='Bad Threshold')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.title('Sentiment Distribution of Amazon Reviews')
plt.xticks(rotation=45)
plt.legend()
plt.show()
print("\n")

print(f" Product Sentiment analysis: {product_sentiment}")

from sklearn.metrics import accuracy_score

# Example true sentiments (manually labeled)
# Replace these with your actual labeled data
y_true = ['Negative', 'Negative', 'Negative', 'Positive', 'Negative','Negative','Negative','Negative','Negative','Negative']  # Manually labeled sentiments

# Predicted sentiments using VADER
y_pred = reviews['sentiment'][:len(y_true)]  # Assuming y_pred comes from VADER predictions for the same reviews

# Calculate accuracy
accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy of VADER Model: {accuracy * 100:.2f}%")