from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import random
from keyboard import *
from admin_base import admin_base
from sqlite import *

API_TOKEN = '5993455599:AAF5T1T_U0Mgglb7aCMJLXQfnXRaW8Zt-_U'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('BOT go')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.last_name is None:
        name = f"{message.from_user.first_name}"
    else:
        name = f"{message.from_user.first_name} {message.from_user.last_name}"
    mess = f'Привіт, {name}'
    if str(message.from_user.id) in admin_base:
        await message.answer(text=mess, reply_markup=kb_admin)
    else:
        await message.answer(text=mess, reply_markup=kb1)
    await add_user(message.from_user.id, name)
    await message.delete()


@dp.message_handler()
async def send_user_id(message: types.Message):
    if message.text == 'Твій user_id':
        await message.answer(message.from_user.id)


# @dp.message_handler(Text(equals='Інструкція'))
# async def admin(message: types.Message):
#     await message.answer(, reply_markup=ikb1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
