import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


def fetch_news(page_size: int = 50):
    """
    Fetch news articles from the News API.
    """

    if not NEWS_API_KEY:
        raise ValueError("NEWS_API_KEY not found in .env")

    params = {
        "apiKey": NEWS_API_KEY,
        "country": "us",        # REQUIRED
        "category": "general",  # Optional but recommended
        "pageSize": page_size,
    }

    response = requests.get(NEWS_API_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data.get("articles", [])
