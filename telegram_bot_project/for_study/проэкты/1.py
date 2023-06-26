from aiogram import Bot, Dispatcher, executor, types
from keyboard import *
from aiogram.dispatcher.filters import Text
import random

API_TOKEN = '5993455599:AAF5T1T_U0Mgglb7aCMJLXQfnXRaW8Zt-_U'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('BOT go')


async def send_random(message: types.Message):
    random_ph = random.choice(arr_photos)
    await bot.send_photo(message.chat.id,
                         photo=random_ph,
                         caption=dict_photo[random_ph],
                         reply_markup=ikb)  # caption описание фотографии

help_command = """
<b>/help</b> - <em>список команд</em>
<b>/description</b> - <em>опис бота</em>
<b>/start</b> - <em>запуск бота</em>
"""

arr_photos = ["https://jpeg.org/images/jpeg-home.jpg",
              "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/"
              "Eduard_Limonov_2016.jpg/1200px-Eduard_Limonov_2016.jpg",
              ""]
dict_photo = dict(zip(arr_photos, ['1', '2']))
random_p = random.choice(arr_photos)


@dp.message_handler(Text(equals='photo'))   # фильтр нужен, чтобы обрабатывать текст, а не команду
async def open_kb_photo(message: types.Message):
    await message.answer('Нажми Рандом чтобы отправить рандомную фотографию',
                         reply_markup=kb_photo)
    await message.delete()


@dp.message_handler(Text(equals='Рандом'))
async def random_photo(message: types.Message):
    await message.answer(text='Рандомная фотка', reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()


@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    global random_p
    if callback.data == 'like':
        await callback.answer('Вам понравилось')
        # await callback.message.answer('Вам понравилось')
    elif callback.data == 'dislike':
        await callback.answer('Вам не понравилось')
        # await callback.message.answer('Вам понравилось')
    elif callback.data == 'next':
        random_p = random.choice(list(filter(lambda x: x != random_p, arr_photos)))
        await callback.message.edit_media(types.InputMedia(media=random_p,
                                                           type='photo',
                                                           caption=dict_photo[random_p]),
                                          reply_markup=ikb)
        # await send_random(message=callback.message)
    else:
        await callback.message.answer(text='Добро пожаловать в главное меню', reply_markup=kb)
        await callback.message.delete()


@dp.message_handler(Text(equals='Главное меню'))   # фильтр нужен, чтобы обрабатывать текст, а не команду
async def open_kb_menu(message: types.Message):
    await message.answer('Добро пожаловать в главное меню',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.last_name is None:
        name = f"{message.from_user.first_name}"
    else:
        name = f"{message.from_user.first_name} {message.from_user.last_name}"
    mess = f'Привіт, {name}'
    await message.answer(text=mess, reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=help_command, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def cmd_help(message: types.Message):
    await message.answer(text='Наш бот вміє відправляти рандомні фото', parse_mode='HTML')
    await message.delete()


# @dp.message_handler(commands=['photo'])
# async def cmd_help(message: types.Message):
#     await bot.send_sticker(message.chat.id, )
#     await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)