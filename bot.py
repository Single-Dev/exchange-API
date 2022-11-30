from aiogram.utils.deep_linking import decode_payload
from aiogram import Bot, Dispatcher, executor, types
from rate import get_rate
import logging
import json
import pathlib
import requests

with open("app.json", "r") as f:
    config = json.load(f)

generator = config['env']['SECRET_TOKEN']['generator']

print(generator)

API_TOKEN = '5868396915:AAGo1vqT4lC_P6n6q1_9FOKXH8lYHOL-_hE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start',])
async def send_welcome(message: types.Message):
    def link(url: str):
        return f"<a href='{url}'>itt</a>"
    link_test = link("https://github.com/bekzodbek2006")
    await message.reply(f"Salom\nMen orqali kursni bilib oling!\nPowered by {link_test}")

@dp.message_handler(commands=['rate_uzs',])
async def get_conversion_rate(message: types.Message):
    r_sum = get_rate('USD')
    response_reply = f"1 USD kursi {r_sum} UZS\n10 USD: {r_sum * 10} UZS\n100 USD: {r_sum * 100} UZS"
    await message.reply(response_reply)

@dp.message_handler()
async def result(message="cat"):
    await message.answer("response_rate")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)