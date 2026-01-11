def clean_and_select_articles(articles, limit: int = 5):
    """
    Clean raw news articles and return top `limit` articles.
    Rules:
    - Must have title, description, and url
    - Remove duplicate titles
    """

    cleaned_articles = []
    seen_titles = set()

    for article in articles:
        title = article.get("title")
        description = article.get("description")
        url = article.get("url")

        if not title or not description or not url:
            continue

        if title in seen_titles:
            continue

        seen_titles.add(title)
        cleaned_articles.append(article)

        if len(cleaned_articles) == limit:
            break

    return cleaned_articles
