import uuid
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
import hashlib

API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
user_data = ''


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Введите число')


@dp.message_handler()
async def digit(message: types.Message):
    global user_data
    if message.text.isdigit():
        user_data = message.text
        await message.reply('Ваши данные сохранены')


# @dp.inline_handler()
# async def inline_echo(inline_query: types.InlineQuery) -> None:
#     text = inline_query.query or 'Echo'
#     result_id: str = hashlib.md5(text.encode()).hexdigest()
#     input_content = InputTextMessageContent(f"<b>{text} - {user_data}</b>", parse_mode='html')
#
#     item = InlineQueryResultArticle(
#         input_message_content=input_content,
#         id=result_id,
#         title='Echo Bot!',
#         description='Привет, я не простой Эхо Бот!'
#     )
#
#     await bot.answer_inline_query(inline_query_id=inline_query.id,
#                                   results=[item],
#                                   cache_time=1)


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo'

    item1 = InlineQueryResultArticle(
        input_message_content=InputTextMessageContent(message_text=f"*{text}*", parse_mode='markdown'),
        id=str(uuid.uuid4()),
        title='Bold',
        description=text
    )

    item2 = InlineQueryResultArticle(
        input_message_content=InputTextMessageContent(message_text=f"_{text}_", parse_mode='markdown'),
        id=str(uuid.uuid4()),
        title='Italic',
        description=text
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item1, item2],
                                  cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)