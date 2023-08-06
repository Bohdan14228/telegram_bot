from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.middlewares import BaseMiddleware


API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


class ClassMid(BaseMiddleware):
    async def on_process_update(self, update: types.Update, data: dict):
        print('sdadada')

    async def on_pre_process_update(self, update: types.Update, data: dict):
        print('Hello')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Добро пожаловать')
    print('World!')


if __name__ == '__main__':
    dp.middleware.setup(ClassMid())
    executor.start_polling(dp, skip_updates=True)