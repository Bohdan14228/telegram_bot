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
    # async def on_process_message(self, message: types.Message, data: dict):
    # if message.from_user.id != 428392590:
    #     raise CancelHandler()
    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        if handler:
            key = getattr(handler, 'key', 'Такого атрибута нет')
            print(key)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Добро пожаловать')


@dp.message_handler(lambda message: message.text.lower() == 'привет')
@set_key()
async def cmd_start(message: types.Message) -> None:
    await message.answer('Hi')


if __name__ == '__main__':
    dp.middleware.setup(ClassMid())
    executor.start_polling(dp, skip_updates=True)