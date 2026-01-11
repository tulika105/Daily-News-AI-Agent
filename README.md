# 🌍 Daily News AI Agent

An autonomous AI-powered agent that fetches the latest global news, summarizes the most important articles using LLaMA model (via Groq), and delivers a clean daily news digest to email — fully automated using GitHub Actions.

## 🚀 Features
- Fetches real-time global news using NewsAPI  
- Cleans and selects the top 5 important articles  
- Generates concise summaries using LLaMA via Groq  
- Sends HTML emails with clickable article links  
- Runs automatically every day at 8:00 AM IST using GitHub Actions  
- Secure handling of secrets with GitHub Secrets  

## 🧠 Tech Stack
- Python 3.10  
- NewsAPI  
- Groq (LLaMA 3)  
- Gmail SMTP  
- GitHub Actions

## 🏗️ Project Structure
- app.py 
- news_fetcher.py  
- utils.py 
- summarizer.py 
- emailer.py 
- requirements.txt
- README.md
- .github/workflows/daily_news.yml

## ⚙️ Local Setup
1. Clone the repository  
   `git clone https://github.com/<your-username>/Daily-News-AI-Agent.git`

2. Create and activate a virtual environment  
   `python -m venv venv`  
   `source venv/bin/activate`  
   *(Windows: `venv\Scripts\activate`)*

3. Install dependencies  
   `pip install -r requirements.txt`

4. Create a `.env` file
- NEWS_API_KEY=your_newsapi_key
- GROQ_API_KEY=your_groq_api_key
- EMAIL=your_email@gmail.com
- EMAIL_APP_PASSWORD=your_gmail_app_password

  
5. Run the agent locally  
`python app.py`

## ⏰ Automation
- Automated using **GitHub Actions**
- Runs daily at **8:00 AM IST**
- Cron schedule used: `30 2 * * *`

## 📬 Email Output
Each daily email contains:
- Top 5 global news headlines
- 2-3 line AI-generated summaries
- Clickable links to full articles
- Clean, readable HTML formatting


