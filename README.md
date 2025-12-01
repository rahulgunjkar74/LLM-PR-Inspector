# 🤖 LLM-PR-Inspector  
### *AI-powered GitHub Pull Request Reviewer using Groq Llama Models*

LLM-PR-Inspector is an intelligent GitHub Pull Request review bot built using **Python**, **Groq Llama 3 models**, and the **GitHub REST API**.  
It automatically analyzes code changes in a PR and posts:

- 📝 Full AI-generated review  
- 💬 Inline comments on specific changed lines  
- 📊 PR summary (files changed, lines added/removed)  
- 🛡️ Risk assessment score  
- ⚡ Ultra-fast analysis using Groq  

This project mimics real-world GitHub AI reviewers like **DeepSource**, **CodeQL**, **SonarCloud**, and **GitHub Copilot PR Review**.

---

## 🚀 Features

### 🔍 Automated Full Review
AI analyzes the entire file patch for:
- Bugs  
- Code smells  
- Logical errors  
- Optimization improvement  
- Readability fixes  
- Security issues  
- Final decision (Approve / Request Changes / Needs Discussion)  
- Risk Score (0–10)

---

### 💬 Inline Review Comments
For every added line (`+` in patch), the AI posts a **short (1–2 line) suggestion**.  
If a line is fine, it skips commenting.

---

### 📊 Pull Request Summary
Automatically posts:
- Total number of changed files  
- Lines added  
- Lines removed  
- Overall impact  
- Risk level  

---

### ⚡ Powered by Groq Llama 3
Groq provides extremely fast inference, making reviews almost instant.

---

## 🗂️ Project Structure
LLM-PR-Inspector/
│
├── main.py # Entry point
├── ai_reviewer.py # Full + inline review logic using Groq
├── github_client.py # GitHub API wrapper (PyGithub)
├── diff_utils.py # Extract changed lines from unified diff
├── review_formatter.py # Formatting: risk score, markdown, summaries
├── config.py # Loads secrets from .env
├── requirements.txt
└── README.md


---

## 🔧 Installation & Setup

### Clone the repository
```bash
git clone https://github.com/<your-username>/LLM-PR-Inspector.git
cd LLM-PR-Inspector
### Create a virtual environment
python -m venv venv
venv\Scripts\activate         # Windows
# or
source venv/bin/activate     # Mac/Linux
### Install dependencies
pip install -r requirements.txt

### Create a .env file

Why This Project Is Special

This project demonstrates:

LLM integration (Groq Llama 3)

GitHub API usage

Automated code review

Diff parsing

Real-world development automation

Clean modular Python structure

Developer

Rahul Gunjkar
Built with ❤️ using Python, Groq, and GitHub API.
