from aiogram.types import *

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('photo')
kb.add(b1, b2).add(b3)


kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton('Рандом')
bp2 = KeyboardButton('Главное меню')
kb_photo.add(bp1, bp2)


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤️', callback_data='like')
ib2 = InlineKeyboardButton(text='👎️', callback_data='dislike')
ib3 = InlineKeyboardButton(text='Следующая фотка', callback_data='next')
ib4 = InlineKeyboardButton(text='Главное меню', callback_data='main')
ikb.add(ib1, ib2, ib3).add(ib4)
