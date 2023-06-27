from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *

API_TOKEN = '5993455599:AAF5T1T_U0Mgglb7aCMJLXQfnXRaW8Zt-_U'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
number = 0


async def on_startup(_):
    print('BOT go')


def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Increase', callback_data='btn_increase'),
         InlineKeyboardButton('Decrease', callback_data='btn_decrease')],
        # [InlineKeyboardButton('hyi', callback_data='sas')]],
        ]
    )
    return ikb


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    global number
    await message.answer(f'The current number is {number}',
                         reply_markup=get_inline_keyboard())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
# будут обрабатываться колл бек запросы, которые начинаются на btn
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    global number
    if callback.data == 'btn_increase':
        number += 1
        await callback.message.edit_text(f'The current number is {number}', reply_markup=get_inline_keyboard())
        # callback.message.edit_text данные обновляются без перезагрузки
    elif callback.data == 'btn_decrease':
        number -= 1
        await callback.message.edit_text(f'The current number is {number}', reply_markup=get_inline_keyboard())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)