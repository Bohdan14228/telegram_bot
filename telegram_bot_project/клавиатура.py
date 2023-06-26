from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '5993455599:AAF5T1T_U0Mgglb7aCMJLXQfnXRaW8Zt-_U'

# logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# kb = ReplyKeyboardMarkup(resize_keyboard=True)  # делает нормальный размер клавиатуры
# b1 = KeyboardButton('шо ты голова')
# b2 = KeyboardButton('hi')
# b3 = KeyboardButton('hi2')
# b4 = KeyboardButton('hi3')
# kb.add(b1).insert(b2).add(b3)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='b1', callback_data='like')
ib2 = InlineKeyboardButton(text='b2', callback_data='dislike')
ikb.add(ib1).add(ib2)


# @dp.message_handler(commands='start')
# async def send(message: types.Message):
#     await bot.send_message(message.from_user.id, 'hello', reply_markup=kb)


# @dp.message_handler(commands='stop')
# async def send(message: types.Message):
#     await message.answer('Options', reply_markup=ikb)


@dp.message_handler(commands='klava')
async def send(message: types.Message):
    await bot.send_photo(message.from_user.id, photo='https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Finspir'
                                                     'ationseek.com%2Fwp-content%2Fuploads%2F2016%2F02%2FCute-Dog-Imag'
                                                     'es.jpg&f=1&nofb=1&ipt=15378cd471f57ec3cfa23a602096c6834380d2c25de'
                                                     'eab6ef22b4e44388e3d64&ipo=images',
                         caption='How photo?',
                         reply_markup=ikb)


@dp.callback_query_handler()
async def vote_call_back(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='you answer like')
    else:
        await callback.answer(text='you answer dislike')

# @dp.message_handler(commands='stop')
# async def send(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id, text='ikb', reply_markup=ikb)
#
#
# @dp.message_handler(commands='site')
# async def send(message: types.Message):
#     await bot.send_message(message.from_user.id, 'hello', reply_markup=ReplyKeyboardRemove())
    # полностью убирает клавиатуру, её потом нельзя развернуть

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)