# 🌍 Daily News AI Agent

An autonomous AI-powered news intelligence agent that operates end-to-end without human intervention. The agent’s purpose is to collect, reason over, and deliver curated information in a timely and reliable manner.

## 🚀 Features
- Fetches real-time global news using NewsAPI  
- Cleans and selects the top 5 important articles  
- Generates concise summaries using LLaMA via Groq  
- Sends HTML emails with clickable article links  
- Runs automatically every day morning using GitHub Actions

<img width="1155" height="290" alt="Screenshot 2026-01-18 142619" src="https://github.com/user-attachments/assets/54cd4e31-c394-470a-95c7-c7b98a4394b3" />

## 🧠 Tech Stack
- Python 3.10  
- NewsAPI  
- Groq (LLaMA 3)  
- Gmail SMTP  
- GitHub Actions

## 🧩 AI Agent Architecture (Model–Tool–Orchestration)

This project follows a standard AI agent architecture composed of three core layers: **Model**, **Tools**, and **Orchestration**. The agent is implemented without relying on any frameworks.

### 1️⃣ Model Layer (Reasoning & Intelligence)
The model layer provides the reasoning capability of the agent.

- **Model Used:** LLaMA (via Groq API)
- **Responsibilities:**
  - Summarizes news articles into concise, factual insights
  - Extracts key information while maintaining neutrality
  - Controls output quality using prompt constraints and temperature tuning

This layer represents the **cognitive intelligence** of the agent.

---

### 2️⃣ Tool Layer (External Capabilities)
The tool layer enables the agent to interact with the external world.

- **NewsAPI:** Fetches real-time global news data  
- **Gmail SMTP:** Sends the final summarized content via email  
- **GitHub Actions:** Provides scheduled, serverless execution  
- **HTTP & Email Protocols:** Support data retrieval and message delivery  

These tools allow the agent to **sense information and act on it**.

---

### 3️⃣ Orchestration Layer (Control & Execution)
The orchestration layer coordinates all components and controls execution flow.

- **app.py:** Acts as the central orchestrator
- **Workflow:**
  1. Fetch news using external tools  
  2. Clean and select top articles  
  3. Summarize articles using the LLM  
  4. Send formatted email to the user  

- **Automation:** GitHub Actions triggers this orchestration daily at a fixed schedule

This layer defines **when, how, and in what order** the agent operates.

---

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
- Runs daily **at morning**
- Cron schedule used: `30 2 * * *`
> **Note:** The cron workflow ran successfully for 30+ consecutive daily executions and is currently disabled to optimize API usage and control operational costs.

## 📬 Email Output
Each daily email contains:
- Top 5 global news headlines  
- 2–3 line AI-generated summaries  
- Clickable links to full articles  
- Clean, readable HTML formatting
  
## 📧 Sample Email 
<img width="1524" height="613" alt="Screenshot 2026-02-08 180311" src="https://github.com/user-attachments/assets/a428c909-e03b-4c81-a2ca-6283277599f3" />
