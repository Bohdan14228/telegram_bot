from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
import random
from aiogram.utils.callback_data import CallbackData

API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

cb = CallbackData('ikb', 'action')


async def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=
                               [InlineKeyboardButton('Increase', callback_data='btn_increase')]
                               )
    return ikb


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Text', reply_markup=await get_inline_keyboard())


@dp.callback_query_handler()
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    await callback.answer('Something')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
