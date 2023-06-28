from aiogram.types import *
from admin_base import admin_base

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Твій user_id')
b2 = KeyboardButton('Інструкція')
kb1.add(b1, b2)

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Твій user_id')
b2 = KeyboardButton('Інструкція')
b3 = KeyboardButton('Адмін-панель')
kb_admin.add(b1, b2).add(b3)

# kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
# bp1 = KeyboardButton('Рандом')
# bp2 = KeyboardButton('Главное меню')
# kb_photo.add(bp1, bp2)


ikb1 = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤️', callback_data='like')
ib2 = InlineKeyboardButton(text='👎️', callback_data='dislike')
ib3 = InlineKeyboardButton(text='Следующая фотка', callback_data='next')
ib4 = InlineKeyboardButton(text='Главное меню', callback_data='main')
ikb1.add(ib1, ib2, ib3).add(ib4)


# @dp.message_handler()
# async def fist(message: types.Message):
#     if message.text == 'Твій user_id':
#         await bot.send_message(chat_id=message.from_user.id, text=f"{message.from_user.id}")