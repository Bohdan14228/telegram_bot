from aiogram.types import *
from admin_base import admin_base

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb1.add(KeyboardButton('Твій user_id'),
        KeyboardButton('Інструкція'))


kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(KeyboardButton('Твій user_id'),
             KeyboardButton('Інструкція')).add(KeyboardButton('Адмін-панель'))


admin_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Додати 'Інструкцію'", callback_data='add_instruction'),
     InlineKeyboardButton("Видалити 'Інструкцію'", callback_data='del_instruction')],
    [InlineKeyboardButton('Закрити', callback_data='close')]
    ]
    )


add_text_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Додати як заголовок 'Інструкції'", callback_data='add_header')],
    [InlineKeyboardButton("Додати як текст 'Інструкції'", callback_data='add_text')],
    [InlineKeyboardButton("Відмінити", callback_data='close')]
    ]
    )


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