import requests
from google.generativeai import GenerativeModel
from os import getenv
from dotenv import load_dotenv

load_dotenv()

api_key = getenv("ALPHA_VANTAGE_API_KEY")

def get_recent_developments(ticker, api_key):
    # Alpha Vantage News API URL
    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={api_key}'.format(ticker=ticker, api_key=api_key)
    # Fetch news data
    response = requests.get(url)
    data = response.json()
    print(data)

    # Extract top 3 news headlines
    if "feed" in data:
        top_news = [article["title"] for article in data["feed"][:3]]  # First 3 articles
    else:
        return f"No recent news found for {ticker}."

    # Summarize with Gemini AI
    model = GenerativeModel('gemini-2.0-flash')
    prompt = f"Summarize the recent developments for {ticker} based on these headlines: {top_news}"
    summary = model.generate_content(prompt)
    print(summary)
    return summary.text

ticker = 'AAPL'
get_recent_developments(ticker)