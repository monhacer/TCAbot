import os
import subprocess

print("Telegram Bot Setup Started")

telegram_token = input("Please enter your Telegram Bot token: ")
openai_key = input("Please enter your OpenAI API key: ")

with open(".env", "w") as env_file:
    env_file.write(f"TELEGRAM_TOKEN={telegram_token}\n")
    env_file.write(f"OPENAI_API_KEY={openai_key}\n")

print("Installing required Python packages...")
subprocess.call(['pip', 'install', '--upgrade', 'pip'])  # به‌روز کردن pip
subprocess.call(['pip', 'install', 'python-dotenv', 'openai', 'pyTelegramBotAPI'])

if not os.path.exists("bot.py"):
    with open("bot.py", "w") as f:
        f.write("# Insert your Telegram bot code here\n")

print("Setup complete! Now fill in 'bot.py' with your bot logic and run it using: python bot.py")
