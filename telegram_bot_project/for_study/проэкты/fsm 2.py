from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup


API_TOKEN = '6697261370:AAFTRKjt8yQ_axSHBkqADo5PfZeQfg-0u8k'
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


def get_create() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/create'))
    return kb


def get_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/cancel'))
    return kb


class ProfileStatesGroup(StatesGroup):
    photo = State()
    name = State()
    age = State()
    description = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Добро пожаловать, введите команду /create', reply_markup=get_create())


@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message) -> None:
    await message.reply('Давай сделаем твой профиль, отправь мне свое фото', reply_markup=get_cancel())
    await ProfileStatesGroup.photo.set()


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_create(message: types.Message, state: FSMContext) -> None:
    if state is None:
        return
    else:
        await state.finish()
        await message.answer('Вы прервали создание анкеты', reply_markup=get_create())


@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.reply('Это не фото😡', reply_markup=get_cancel())


@dp.message_handler(content_types=['photo'], state=ProfileStatesGroup.photo)    # обрабатывает только фото
async def load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await message.answer('А теперь отправь свое имя!', reply_markup=get_cancel())
    await ProfileStatesGroup.name.set()


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    if not message.text.isalpha():
        await message.reply('Это не имя😡', reply_markup=get_cancel())
    else:
        async with state.proxy() as data:
            data['name'] = message.text

        await message.answer('Сколько тебе лет?', reply_markup=get_cancel())
        await ProfileStatesGroup.age.set()


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext) -> None:
    if not message.text.isdigit():
        await message.reply('Это не возраст😡', reply_markup=get_cancel())
    else:
        async with state.proxy() as data:
            data['age'] = message.text

        await message.answer('Теперь расскажи немного о себе!', reply_markup=get_cancel())
        await ProfileStatesGroup.description.set()


@dp.message_handler(state=ProfileStatesGroup.description)
async def load_description(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['description'] = message.text
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"Имя: <i>{data['name']}</i>\n"
                                     f"Возраст: <i>{data['age']}</i>\n"
                                     f"Описание: <i>{data['description']}</i>",
                             parse_mode='html')

    await message.answer('Ваша анкета успешно создана!')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)