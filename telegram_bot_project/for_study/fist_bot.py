import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5993455599:AAF5T1T_U0Mgglb7aCMJLXQfnXRaW8Zt-_U'

# logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)    # диспетчер, анализ всех входящих апдейтов


async def on_startup(_):
    print('BOT go')


@dp.message_handler(content_types=['sticker'])  # отправляет id стикера на отправленный стикер
async def sticker(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler()
async def echo(message: types.Message):
    if '❤' in message.text:
        await message.answer('❤')
    # await message.delete()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")   # message.reply ответ на сообщение


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text.upper())  # message.answer обычный вывод текста
#     await message.delete()  # удаляет сообщения пользователя


@dp.message_handler(commands='html')
async def echo(message: types.Message):
    await message.answer('<em>курсив</em>,  <b>жирный</b>', parse_mode="HTML")


@dp.message_handler(commands='give')    # отправляет стикеры, можно взять id стикера в боте
async def echo(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEJVyRkjKd6LxcI9S3ZKRcH3VRMkz40AgACCQADBvWcKpcwuvmgAm8NLwQ")


@dp.message_handler(commands='sticker')
async def echo(message: types.Message):
    await message.answer('смотри какое сердечко ❤')


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == '❤ ':
        await message.answer('❤')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)