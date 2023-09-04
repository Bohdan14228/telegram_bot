from aiogram import Bot, Dispatcher, executor, types
from token_tg import api_tg

bot = Bot(token=api_tg)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def keyb(message: types.Message):
    # one_time_keyboard после нажатия на клаве кнопку убираются
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton('site'))
    markup.add(types.KeyboardButton('website'))
    await message.answer('button', reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)