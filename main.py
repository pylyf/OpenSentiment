import stock_news as finnews
import ai_sentiment
from tabulate import tabulate
import pyfiglet


print(pyfiglet.figlet_format("OpenSentiment"))
print("Get sentiment rating for stock articles using OpenAI API")

# Ask user to input the ticker that we will use to fetch the news
print("Input the ticker of the stock you wish to rate.")
ticker = input("Ticker: ")

# Call our stock_news library that uses yfinance library to fetch news from Yahoo Finance
ticker_news = finnews.get_ticker_news(ticker) 

# 1) Seperate article titles from the whole list
news_titles = finnews.get_news_titles(ticker_news)
# 2) Pass the article titles to an OpenAI ChatGPT prompt to analyse their sentiment
sentiment_rated_titles = ai_sentiment.openai_analyse_news(news_titles)

# Prepare a nice visualisation of the data, put them in a table using the tabulate library
table_data = zip(news_titles, sentiment_rated_titles) # set table data
headers = ["Article", "Sentiment Rating"] # set table headers
print(tabulate(table_data, headers=headers))
exit()