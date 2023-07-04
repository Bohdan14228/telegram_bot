from aiogram.types import *
from admin_base import admin_base
import asyncio
from sqlite import *


async def func_kb1():
    kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
    kb1.add(KeyboardButton('Твій user_id'),
            KeyboardButton('Інструкція'))
    return kb1


async def func_kb_admin():
    kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_admin.add(KeyboardButton('Твій user_id'),
                 KeyboardButton('Інструкція')).add(KeyboardButton('Адмін-панель'))
    return kb_admin


async def func_admin_ikb():
    admin_ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Видалити 'Інструкцію'", callback_data='del_instruction')],
        [InlineKeyboardButton('Закрити', callback_data='close')]
        ]
        )
    return admin_ikb
# InlineKeyboardButton("Додати 'Інструкцію'", callback_data='add_instruction'),


async def func_add_text_ikb():
    add_text_ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Додати як заголовок 'Інструкції'", callback_data='add_header')],
        [InlineKeyboardButton("Додати як текст 'Інструкції'", callback_data='add_text')],
        [InlineKeyboardButton("Відмінити", callback_data='close')]
        ]
        )
    return add_text_ikb


async def ikb_instructions():
    ikb = InlineKeyboardMarkup(row_width=1)
    for i in await for_ikb_instructions():
        ikb.add(InlineKeyboardButton(text=f"{i[0]}", callback_data=f"{i[1]}"))
    ikb.add(InlineKeyboardButton('Закрити', callback_data='close'))
    return ikb


async def add_records(text):
    ikb = InlineKeyboardMarkup(row_width=1)
    for i in await for_ikb_instructions():
        ikb.add(InlineKeyboardButton(text=f"{i[0]}", callback_data=f"add_records {text}"))
    ikb.add(InlineKeyboardButton('Закрити', callback_data='close'))
    return ikb

# print(asyncio.get_event_loop().run_until_complete(ikb_instructions()))

# inst_ikb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton("Зробити заголовк")]])
# admin_ikb.add(KeyboardButton("Додати 'Інструкцію'"),
#              KeyboardButton("Видалити 'Інструкцію'")).add(KeyboardButton("Назад"))


# ikb1 = InlineKeyboardMarkup(row_width=2)
# ib1 = InlineKeyboardButton(text='❤️', callback_data='like')
# ib2 = InlineKeyboardButton(text='👎️', callback_data='dislike')
# ib3 = InlineKeyboardButton(text='Следующая фотка', callback_data='next')
# ib4 = InlineKeyboardButton(text='Главное меню', callback_data='main')
# ikb1.add(ib1, ib2, ib3).add(ib4)


# @dp.message_handler()
# async def fist(message: types.Message):
#     if message.text == 'Твій user_id':
#         await bot.send_message(chat_id=message.from_user.id, text=f"{message.from_user.id}")