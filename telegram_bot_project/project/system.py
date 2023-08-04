from aiogram import Bot, Dispatcher, executor, types
import os
from keyboard import *
from admin_base import admin_base
from sqlite import *
import aiosqlite

API_TOKEN = '5993455599:AAF5T1T_U0Mgglb7aCMJLXQfnXRaW8Zt-_U'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def func_kb1():
    kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
    kb1.add(KeyboardButton('выключить'))
    return kb1


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.last_name is None:
        name = f"{message.from_user.first_name}"
    else:
        name = f"{message.from_user.first_name} {message.from_user.last_name}"
    mess = f'Привіт, {name}'
    await message.answer(text=mess, reply_markup=await func_kb1())
    await message.delete()


@dp.message_handler()
async def send_user_id(message: types.Message):
    if message.text == 'выключить':
        os.system('shutdown -s -t 0')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)