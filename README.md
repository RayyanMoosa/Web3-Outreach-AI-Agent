# Web3-Outreach-AI-Agent
# Web3 Outreach Agent 🤖📩

An AI-powered outreach system that finds early-stage Web3 founders, writes personalized emails for them, and sends the messages automatically — all hands-free.

## 🚀 What It Does

This system automates the entire cold outreach process:

1. **Lead Generation** – Uses SerpAPI to find Web3 founders and their websites, LinkedIn profiles, and more.
2. **Message Personalization** – Generates custom, friendly outreach messages tailored to each lead using OpenAI.
3. **Email Automation** – Sends emails using Gmail's API and logs sent messages.

## 💡 Why This Matters

- Saves hours of manual outreach work  
Web3 Outrach AI Agent

- Scales lead generation and messaging instantly  
- Makes cold emails feel personal and relevant  
- Easy to customize and expand (add sources, change message style, etc.)

## 🧠 How It Works

### 1. `serpapi_search.py`
Uses SerpAPI to search Google for Web3 startups/founders and extracts their name, title, website, LinkedIn, and more.  
👉 Output: `web3_leads.csv`

### 2. `generate_messages.py`
Reads `web3_leads.csv` and writes a unique, personalized email message for each lead.  
👉 Output: `outreach_with_messages.csv`

### 3. `combine_leads.py`
(Optional) Combines leads from different sources and removes duplicates.  
👉 Output: `final_leads.csv`

### 4. `send_outreach_emails.py`
Sends outreach emails via Gmail API using the final CSV with messages. Logs sent emails in a local file.

## 🔧 Setup

### 1. Clone the repo  
```bash
git clone https://github.com/yourusername/web3-outreach-agent.git
cd web3-outreach-agent
