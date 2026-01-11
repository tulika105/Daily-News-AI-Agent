import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def summarize_article(article: dict) -> str:
    """
    Summarize a single news article in 2–3 lines.
    """

    prompt = f"""
You are a professional news editor.

Summarize the following news article in **2 to 3 concise sentences**.

Rules:
- Be factual and neutral
- Do NOT add opinions or assumptions
- Do NOT repeat the headline
- Focus on what happened and why it matters
- Keep it clear and readable for a general audience

Article details:

Title: {article['title']}
Description: {article['description']}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.,
    )

    return response.choices[0].message.content.strip()
