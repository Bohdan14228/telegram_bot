import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
import random
from aiogram.utils.exceptions import BotBlocked
from aiogram.utils.callback_data import CallbackData
import hashlib

API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

cb = CallbackData('ikb', 'action')


def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Button_1', callback_data=cb.new('push_1'))],
        [InlineKeyboardButton('Button_2', callback_data=cb.new('push_2'))],
                                                ])
    return ikb


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('What?', reply_markup=get_ikb())


@dp.callback_query_handler(cb.filter(action='push_1'))
async def push_filter_cb_handler(callback: types.CallbackQuery) -> None:
    await callback.answer('Hello')


@dp.callback_query_handler(cb.filter(action='push_2'))
async def push_filter_cb_handler(callback: types.CallbackQuery) -> None:
    await callback.answer('World')


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo'

    if inline_query.query == 'photo':
        text = 'This is a photo'    # получили текст от пользователя
    # or
    # if text == 'photo':
    #     input_content = InputTextMessageContent('This is a photo')

    input_content = InputTextMessageContent(text)   # формируем контент ответного сообщения
    result_id: str = hashlib.md5(text.encode()).hexdigest()  # сделали уникальный ID

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title=text
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)