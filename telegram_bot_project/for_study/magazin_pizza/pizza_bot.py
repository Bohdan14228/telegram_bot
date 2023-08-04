from aiogram import Bot, Dispatcher, executor, types
import os, string, json

API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def mat(message: types.Message):
    cenz_set = set(json.load(open('cenz.json')))
    if any(word.lower().translate(str.maketrans('', '', string.punctuation)) in cenz_set for word in
           message.text.split()):
        await message.reply('Маты запрещены')
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
