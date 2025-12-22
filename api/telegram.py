import os
import telebot
from fastapi import FastAPI, Request

BOT_TOKEN = os.environ["BOT_TOKEN"]

bot = telebot.TeleBot(BOT_TOKEN)
app = FastAPI()

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Welcome!")

@app.post("/")
async def telegram_webhook(request: Request):
    json_data = await request.json()
    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])
    return {"ok": True}