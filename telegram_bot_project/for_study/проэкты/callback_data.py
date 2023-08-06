from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
import random
from aiogram.utils.callback_data import CallbackData

API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

cb = CallbackData('ikb', 'action')

ikb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('Button', callback_data=cb.new('push'))]
                                            ])
print(ikb)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Text', reply_markup=ikb)


# @dp.callback_query_handler(lambda callback_query: callback_query.data == 'hello')
@dp.callback_query_handler(cb.filter())
async def ikb_cb_handler(callback: types.CallbackQuery, callback_data: dict) -> None:
    print(callback_data)
    if callback_data['action'] == 'push':
        await callback.answer('Something')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
