from aiogram import Bot, Dispatcher, executor, types
from token_tg import api_tg
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot(token=api_tg)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(types.InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://bohdan14228.github.io/wep_telegram/')))
    await message.answer('Hi my friend', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f"{res['name']} {res['email']} {res['phone']}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)