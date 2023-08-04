from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
import random

API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
number = 0


async def on_startup(_):
    print('BOT go')


def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Increase', callback_data='btn_increase'),
         InlineKeyboardButton('Decrease', callback_data='btn_decrease')],
        [InlineKeyboardButton('Random', callback_data='btn_random')]
    ]
    )
    return ikb


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    global number
    await message.answer(f'The current number is {number}',
                         reply_markup=get_inline_keyboard())


async def an_us(callback, num):
    return await callback.message.edit_text(f'The current number is {num}', reply_markup=get_inline_keyboard())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
# будут обрабатываться колл бек запросы, которые начинаются на btn
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    global number
    if callback.data == 'btn_increase':
        number += 1
        await an_us(callback, number)
        # callback.message.edit_text данные обновляются без перезагрузки
    elif callback.data == 'btn_decrease':
        number -= 1
        await an_us(callback, number)
    elif callback.data == 'btn_random':
        number = random.randint(1, 59)
        await an_us(callback, number)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
