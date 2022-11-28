from aiogram import Bot, Dispatcher, executor, types
from rate import get_rate
import logging


API_TOKEN = '5868396915:AAGo1vqT4lC_P6n6q1_9FOKXH8lYHOL-_hE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start',])
async def send_welcome(message: types.Message):
    await message.reply("Salom!\nMen orqali kursni bilib oling!\nPowered by github.com/bekzodbek2006.")

@dp.message_handler(commands=['rate_uzs',])
async def get_conversion_rate(message: types.Message):
    r_sum = get_rate('USD')
    response_reply = f"1 USD kursi {r_sum} UZS\n10 USD: {r_sum * 10} UZS\n100 USD: {r_sum * 100} UZS"
    await message.reply(response_reply)

# @dp.message_handler()
# async def result(message: types.Message):
#     response_rate = f"{get_rate(message.text)} so'm"
#     await message.answer(response_rate)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)