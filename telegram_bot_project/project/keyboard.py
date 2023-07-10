from aiogram.types import *
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
        [InlineKeyboardButton("Видалити 'Інструкцію'", callback_data='del')],
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
    for i in await for_ikb_instructions('show'):
        ikb.add(InlineKeyboardButton(text=f"{i[1]}", url=f"{await show_record(i[0])}"))
    ikb.add(InlineKeyboardButton('Закрити', callback_data='close'))
    return ikb
print(asyncio.get_event_loop().run_until_complete(ikb_instructions()))

# async def


async def add_records_ikb():
    ikb = InlineKeyboardMarkup(row_width=1)
    for i in await for_add_records_ikb():
        ikb.add(InlineKeyboardButton(text=f"{i[1]}", callback_data=f"add_records{i[0]}"))
    ikb.add(InlineKeyboardButton('Закрити', callback_data='close'))
    return ikb


async def del_instruction_step_1():
    ikb = InlineKeyboardMarkup(row_width=1)
    for i in await for_ikb_instructions('del'):
        ikb.add(InlineKeyboardButton(text=f"{i[1]}", callback_data=f"instruction_del_step_1{i[0] if not await show_record(i[0]) else await show_record(i[0])}"))
    ikb.add(InlineKeyboardButton('Закрити', callback_data='close'))
    return ikb
print(asyncio.get_event_loop().run_until_complete(del_instruction_step_1()))


async def del_instruction_step_2(record):
    add_text_ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Видалити тільки текст інструкції", callback_data=f'instruction_del_1{record}')],
        [InlineKeyboardButton("Видалити і заголовок і текст інструкції", callback_data=f'instruction_del_2{record}')],
        [InlineKeyboardButton("Назад", callback_data='back')],
    ]
    )
    return add_text_ikb
