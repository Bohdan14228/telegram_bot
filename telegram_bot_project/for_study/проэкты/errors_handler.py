import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
import random
from aiogram.utils.exceptions import BotBlocked

API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await asyncio.sleep(10)
    await message.answer('Text')


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked_handler(update: types.Update, exception: BotBlocked) -> bool:
    print('Нас заблокировали, нельзя отправить сообщение')
    return True

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)