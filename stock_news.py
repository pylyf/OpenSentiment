import yfinance as yf

def get_ticker_news(ticker):
    # Fetch financial news from Yahoo Finance using the yfinance library and return them
    # input: string
    # output: list
    ticker_obj = yf.Ticker(ticker) 
    company_news = ticker_obj.news
    return company_news

def get_news_titles(news):
    # Loop through the news and seperate the titles that will later on be passed to the OpenAI prompt
    # input: list
    # output: list
    news_titles = []
    for article in news:
        news_titles.append(article["title"])
    return news_titles

if __name__ == "__main__":
    # This part of code gets executed only if the file gets run as a standalone script, not when it is imported as a library
    print("[OpenSentiment Library]")
    print("-------------------------")
    print("[!] Please run only as an imported library in the main.py file [!]")
    print("Exiting...")
    exit()