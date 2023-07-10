from aiogram import Bot, Dispatcher, executor, types
from keyboard import *
from admin_base import admin_base
from sqlite import *
import aiosqlite

API_TOKEN = '5993455599:AAF5T1T_U0Mgglb7aCMJLXQfnXRaW8Zt-_U'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


text_record = ''


async def on_startup(_):
    print('BOT go')


async def examination_in_base(user_id):
    return str(user_id) in admin_base


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.last_name is None:
        name = f"{message.from_user.first_name}"
    else:
        name = f"{message.from_user.first_name} {message.from_user.last_name}"
    mess = f'Привіт, {name}'
    if await examination_in_base(message.from_user.id):
        await message.answer(text=mess, reply_markup=await func_kb_admin())
    else:
        await message.answer(text=mess, reply_markup=await func_kb1())
    await add_user(message.from_user.id, name, message.from_user.username)
    await message.delete()


@dp.message_handler()
async def send_user_id(message: types.Message):
    if message.text == 'Твій user_id':
        await message.reply(message.from_user.id)
    elif message.text == 'Адмін-панель':
        if await examination_in_base(message.from_user.id):
            await message.answer(text='Адмін-панель', reply_markup=await func_admin_ikb())
        else:
            await message.answer('У вас недостатньо прав', reply_markup=await func_kb1())
        await message.delete()
    elif message.text == 'Інструкція':
        await message.answer('Інструкції', reply_markup=await ikb_instructions())
        await message.delete()
    else:
        if await examination_in_base(message.from_user.id):
            await message.delete()
            await message.answer(text=message.text, reply_markup=await func_add_text_ikb())
        else:
            await message.delete()
            await message.answer('У вас недостатньо прав щоб додавати інструкції', reply_markup=await func_kb1())


@dp.callback_query_handler()
async def ikb_close(callback: types.CallbackQuery):
    global text_record
    if callback.data == 'close':
        await callback.message.delete()
    elif callback.data == 'add_header':
        try:
            await add_instruction(callback.message.text)
            await callback.answer('Додано новий заголовок')
        except aiosqlite.IntegrityError as ex:
            await callback.message.answer('Такий заголовок вже існує')
        await callback.message.delete()
    elif callback.data == 'add_text':
        text_record = callback.message.text
        await callback.message.edit_text(f'''Виберіть заголовок для цього тексту:<b>{callback.message.text}</b>''',
                                         parse_mode='HTML',
                                         reply_markup=await add_records_ikb())
    elif callback.data.startswith('add_records'):
        text = callback.data.replace('add_records', '')
        await add_records(text, text_record)
        await callback.answer('Додано новий текст інструкції')
        await callback.message.delete()
    elif callback.data.startswith('show_instruction'):
        text = callback.data.replace('show_instruction', '')
        await callback.message.answer(await show_records(text))
    elif callback.data.startswith('del') or callback.data == 'back':
        await callback.message.edit_text('Виберіть інструкцію яку хочете видалити',
                                         reply_markup=await del_instruction_step_1())
    elif callback.data.startswith('instruction_del_step_1'):
        text = callback.data.replace('instruction_del_step_1', '')
        if text.isdigit():
            # await callback.message.answer(text)
            await del_problems(text)
            await callback.answer('Видалено')
            await callback.message.delete()
        else:
            await callback.message.edit_text('Виберіть що саме хочете видалити',
                                             reply_markup=await del_instruction_step_2(text))
    elif callback.data.startswith('instruction_del_1'):
        await callback.answer('Видалено')
        text = callback.data.replace('instruction_del_1', '')
        await del_records_problems(text, 1)
        await callback.message.delete()
    elif callback.data.startswith('instruction_del_2'):
        await callback.answer('Видалено')
        text = callback.data.replace('instruction_del_2', '')
        await del_records_problems(text, 2)
        await callback.message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
