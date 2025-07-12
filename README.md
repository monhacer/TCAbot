# 🤖 Telegram Coding Assistant Bot

A smart Telegram bot designed to help developers by answering coding questions using the ChatGPT API.

---

## 🚀 Features

- 💬 Ask coding-related questions directly via Telegram  
- 🤖 Get intelligent responses powered by OpenAI  
- 🧠 Receive code examples, explanations, and bug fixes  
- 🔄 Easy to customize and expand using Python  

---

## 🛠 Installation Guide

### 1️⃣ Clone the repository
```
git clone https://github.com/monhacer/TCAbot.git  
cd coding-assistant-bot
```
### 2️⃣ Run the interactive setup script
```
python setup.py  
```
You’ll be prompted to enter:
- Your **Telegram Bot Token**
- Your **OpenAI API Key**

This script will automatically:
- Generate a `.env` file  
- Install required Python packages  
- Create a placeholder `bot.py` file if it doesn't exist

### 3️⃣ Add your bot logic

Open the `bot.py` file and paste your bot implementation. You can use the sample code provided in the repo or write your own.

### 4️⃣ Launch the bot
```
python bot.py  
```
---

## 📂 Project Structure

- bot.py → Main bot logic  
- setup.py → Interactive installer  
- .env → Stores your API keys (excluded from Git commits)  
- .gitignore → Prevents committing sensitive files  
- requirements.txt → Python dependency list  
- README.md → This documentation  

---

## 📦 Requirements

- Python 3.9+  
- Telegram bot token via [BotFather](https://t.me/BotFather)  
- OpenAI API key via [platform.openai.com](https://platform.openai.com)  
- Required pip packages:  
  - openai  
  - pyTelegramBotAPI  
  - python-dotenv  

---

## 🙌 Contributing

Feel free to fork, modify, and submit pull requests. Let’s build something cool together! 😎

---

## 📄 License

MIT — Free to use and modify with proper attribution. No warranty provided 😉
