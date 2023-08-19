from pymessenger import Bot
from dotenv import load_dotenv
import os
load_dotenv("./.env")

bot = Bot(os.getenv("PAGE_ACCESS_TOKEN"))

def send_message(recipient_id, message_text):
    bot.send_text_message(recipient_id, message_text)