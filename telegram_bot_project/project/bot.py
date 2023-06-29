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


def examination_in_base(user_id):
    return str(user_id) in admin_base


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.last_name is None:
        name = f"{message.from_user.first_name}"
    else:
        name = f"{message.from_user.first_name} {message.from_user.last_name}"
    mess = f'Привіт, {name}'
    if examination_in_base(message.from_user.id):
        await message.answer(text=mess, reply_markup=kb_admin)
    else:
        await message.answer(text=mess, reply_markup=kb1)
    await add_user(message.from_user.id, name, message.from_user.username)
    await message.delete()


@dp.message_handler()
async def send_user_id(message: types.Message):
    if message.text == 'Твій user_id':
        await message.reply(message.from_user.id)
        print(message)
    elif message.text == 'Адмін-панель':
        if examination_in_base(message.from_user.id):
            await message.answer(text='Адмін-панель', reply_markup=admin_ikb)
        await message.delete()
    elif message.text == 'Інструкція':
        await message.answer()
    else:
        await message.delete()
        await message.answer(text=message.text, reply_markup=add_text_ikb)


@dp.callback_query_handler()
async def ikb_close(callback: types.CallbackQuery):
    if callback.data == 'close':
        await callback.message.delete()
    elif callback.data == 'add_instruction':
        await callback.message.delete()
        await callback.message.answer('Напишіть заголовок для інструкції')
    elif callback.data == 'add_header':
        await callback.answer('Додано новий заголовок')
        # await add_instruction(callback.message.text)
        try:
            await add_instruction(callback.message.text)
        except sqlite3.IntegrityError as ex:
            await callback.message.answer('Такий заголовок вже існує')
        await callback.message.delete()
        # print(callback.message.text)


# @dp.message_handler(Text(equals='Інструкція'))
# async def admin(message: types.Message):
#     await message.answer(, reply_markup=ikb1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
