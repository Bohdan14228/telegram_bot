from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, current_handler


API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


def set_key(key: str = None):
    def decorator(func):
        setattr(func, 'key', key)
        return func

    return decorator


class ClassMid(BaseMiddleware):
    async def on_process_callback_query(self, query: types.CallbackQuery, data: dict):
        callback_id = query.data.split('_')[1]
        if callback_id != str(query.from_user.id):
            raise CancelHandler


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Test Button', callback_data=f'check_{message.from_user.id}')]
    ])
    await message.answer('Добро пожаловать', reply_markup=ikb)


@dp.callback_query_handler(lambda callback: callback.data.startswith('check_'))
async def cb_check(callback: types.CallbackQuery):
    await callback.message.answer('Вы нажали кнопку')


if __name__ == '__main__':
    dp.middleware.setup(ClassMid())
    executor.start_polling(dp, skip_updates=True)