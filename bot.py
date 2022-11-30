from aiogram.utils.deep_linking import decode_payload
from aiogram import Bot, Dispatcher, executor, types
from rate import get_rate
from aiogram.dispatcher.filters import Filter
import logging
import json
import pathlib
import requests

with open("app.json", "r") as f:
    config = json.load(f)


# API_TOKEN = '5868396915:AAGo1vqT4lC_P6n6q1_9FOKXH8lYHOL-_hE'
API_TOKEN = config['env']['SECRET_TOKEN']['token']

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

admins = set()
users = set()


@dp.message_handler(commands=['start',])
async def send_welcome(message: types.Message):
    users.add(message.from_user.username)
    await message.reply(f"Salom\nMen orqali kursni bilib oling!\nPowered Bekzodbek")


class IsAdmin(Filter):
    key = "is_admin"
    async def check(self, message: types.Message):
        return message.from_user.id in admins

@dp.message_handler(IsAdmin(), commands=['users'])
async def only_for_admins(message: types.Message):
        user_result = f'{len(users)}ta users\n{users}'
        await message.answer(user_result)


@dp.message_handler(commands="make")
async def add_to_admins(message: types.Message):
    admins.add(message.from_user.id)
    await message.reply(f"New admins list: {admins}")


@dp.message_handler(commands=['rate_uzs',])
async def get_conversion_rate(message: types.Message):
    r_sum = get_rate('USD')
    response_reply = f"1 USD kursi {r_sum} UZS\n10 USD: {r_sum * 10} UZS\n100 USD: {r_sum * 100} UZS"
    await message.reply(response_reply)

# @dp.message_handler()
# async def result(message: types.Message):
#     await message.answer("response_rate")

@dp.message_handler(content_types='photo')
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def content_type_example(msg: types.Message):
    await msg.answer('Bu Rasmmi?')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)