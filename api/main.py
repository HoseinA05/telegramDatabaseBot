import os
import telebot
from fastapi import FastAPI, Request

BOT_TOKEN = os.environ["BOT_TOKEN"]

bot = telebot.TeleBot(BOT_TOKEN)
app = FastAPI()

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Welcome!")

@app.post("/telegram")
async def telegram_webhook(request: Request):
    data = await request.body()
    update = telebot.types.Update.de_json(data.decode("utf-8"))
    bot.process_new_updates([update])
    return {"ok": True}
