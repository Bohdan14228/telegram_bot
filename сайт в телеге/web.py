from aiogram import Bot, Dispatcher, executor, types
from token_tg import api_tg
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(token=api_tg)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://itproger.com')))
    await message.answer('Hi my friend', reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)