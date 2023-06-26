import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5993455599:AAF5T1T_U0Mgglb7aCMJLXQfnXRaW8Zt-_U'

# logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler()
# async def echo(message: types.Message):
    # await message.answer(message.text)


# @dp.message_handler()
# async def echo(message: types.Message):
#     await bot.send_message(message.chat.id, 'hello')
# это равносильно message.answer, в группе бот должен быть админом


# @dp.message_handler()
# async def echo(message: types.Message):
#     await bot.send_message(message.from_user.id, 'hello')
    # здесь даже если мы будем писать в группу то бот нам будет отвечать только в личку


@dp.message_handler(commands='photo')
async def send(message: types.Message):
    await bot.send_photo(message.from_user.id, photo='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Ml6bjheFvxYYr_BjaxNfKQHaFQ%26pid%3DApi&f=1&ipt=0c26fcbf7bdf6c9948aa70398106360b5a4e161fe0b5d4e3654bf86d068d9add&ipo=images')


@dp.message_handler(commands='location')
async def send(message: types.Message):
    await bot.send_location(message.from_user.id, latitude=55, longitude=74)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)