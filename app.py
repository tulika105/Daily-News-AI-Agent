from news_fetcher import fetch_news
from utils import clean_and_select_articles
from summarizer import summarize_article
from emailer import send_email


def main():
    print("🚀 Running News AI Agent...\n")

    # 1. Fetch latest news
    articles = fetch_news()
    print(f"📰 Fetched {len(articles)} articles")

    # 2. Select top 5 clean articles
    top_articles = clean_and_select_articles(articles, limit=5)
    print(f"✅ Selected {len(top_articles)} articles\n")

    # 3. Build HTML email body
    email_body = """
    <h2>News for you</h2>
    """

    for idx, article in enumerate(top_articles, start=1):
        summary = summarize_article(article)

        email_body += f"""
        <p>
            <b>{idx}. {article['title']}</b><br>
            {summary}<br>
            <a href="{article['url']}" target="_blank">Read full article</a>
        </p>
        <hr>
        """

    # 4. Send email
    send_email(
        subject="Top News",
        body=email_body
    )


if __name__ == "__main__":
    main()
