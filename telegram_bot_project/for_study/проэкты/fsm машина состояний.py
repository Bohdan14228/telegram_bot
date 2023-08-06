import uuid
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import *
import hashlib
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


def get_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Начать работу'))
    return kb


def get_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/cancel'))
    return kb


class Client(StatesGroup):
    photo = State()
    desc = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Добро пожаловать', reply_markup=get_keyboard())


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.reply("Отмена", reply_markup=get_keyboard())
    await state.finish()


@dp.message_handler(Text(equals='Начать работу', ignore_case=True), state=None)
async def start_work(message: types.Message) -> None:
    await Client.photo.set()
    await message.answer('Сначала отправь нам фотографию', reply_markup=get_cancel())


@dp.message_handler(lambda message: not message.photo, state=Client.photo)
async def check_photo(message: types.Message):
    return await message.reply('Это не фотография', reply_markup=get_cancel())


@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=Client.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await Client.next()
    await message.reply('А теперь отправь нам описание!')


@dp.message_handler(state=Client.desc)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text

    await message.reply('Ваша фотография сохранена')
    async with state.proxy() as data:
        await bot.send_photo(chat_id=message.from_user.id, photo=data['photo'], caption=data['desc'])
        
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)