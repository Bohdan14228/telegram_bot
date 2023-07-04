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


async def examination_in_base(user_id):
    return str(user_id) in admin_base


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.last_name is None:
        name = f"{message.from_user.first_name}"
    else:
        name = f"{message.from_user.first_name} {message.from_user.last_name}"
    mess = f'Привіт, {name}'
    if await examination_in_base(message.from_user.id):
        await message.answer(text=mess, reply_markup=await func_kb_admin())
    else:
        await message.answer(text=mess, reply_markup=await func_kb1())
    await add_user(message.from_user.id, name, message.from_user.username)
    await message.delete()


@dp.message_handler()
async def send_user_id(message: types.Message):
    if message.text == 'Твій user_id':
        await message.reply(message.from_user.id)
    elif message.text == 'Адмін-панель':
        if await examination_in_base(message.from_user.id):
            await message.answer(text='Адмін-панель', reply_markup=await func_admin_ikb())
        else:
            await message.answer('У вас недостатньо прав', reply_markup=await func_kb1())
        await message.delete()
    elif message.text == 'Інструкція':
        await message.answer('Інструкції', reply_markup=await ikb_instructions())
    else:
        if await examination_in_base(message.from_user.id):
            await message.delete()
            await message.answer(text=message.text, reply_markup=await func_add_text_ikb())
        else:
            await message.delete()
            await message.answer('У вас недостатньо прав щоб додавати інструкції', reply_markup=await func_kb1())


@dp.callback_query_handler()
async def ikb_close(callback: types.CallbackQuery):
    if callback.data == 'close':
        await callback.message.delete()
    elif callback.data == 'add_instruction':
        await callback.message.delete()
        await callback.message.answer('Напишіть заголовок для інструкції')
    elif callback.data == 'add_header':
        try:
            await add_instruction(callback.message.text)
            await callback.answer('Додано новий заголовок')
        except sqlite3.IntegrityError as ex:
            await callback.message.answer('Такий заголовок вже існує')
        await callback.message.delete()
    elif callback.data == 'add_text':
        await callback.message.delete()
        await callback.message.answer(f'''Виберіть заголовок для цього тексту:
<b>{callback.message.text}</b>''', parse_mode='HTML', reply_markup=await add_records(text=callback.message.text))
    elif callback.data.startswith('add_records'):
        await callback.message.delete()
        await callback.message.answer(callback.message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
