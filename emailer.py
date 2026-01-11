import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


def send_email(subject: str, body: str):
    """
    Send an HTML email using Gmail SMTP.
    """

    if not EMAIL or not EMAIL_APP_PASSWORD:
        raise ValueError("Email credentials not found in .env")

    msg = MIMEText(body, "html", "utf-8")
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = EMAIL  # send to self

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, EMAIL_APP_PASSWORD)
        server.send_message(msg)

    print("✅ Email sent successfully")
