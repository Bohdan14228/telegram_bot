from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import random


API_TOKEN = '5993455599:AAF5T1T_U0Mgglb7aCMJLXQfnXRaW8Zt-_U'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('BOT go')


@dp.message_handler(commands=['file'])
async def fist(message: types.Message):
    await message.answer('hi')


@dp.message_handler(commands=['start'])
async def fist(message: types.Message):
    await message.answer('hi')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)