import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5868396915:AAGo1vqT4lC_P6n6q1_9FOKXH8lYHOL-_hE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom!\nMen orqali kursni bilib oling!\nPowered by github.com/bekzodbek2006.")


@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)