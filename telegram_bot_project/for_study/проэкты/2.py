from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
import asyncio

API_TOKEN = '5993455599:AAF5T1T_U0Mgglb7aCMJLXQfnXRaW8Zt-_U'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

is_voted = False

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('like', callback_data='like'), InlineKeyboardButton('dislike', callback_data='dislike')],
    [InlineKeyboardButton('close keyboard', callback_data='close')]
])


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://jpeg.org/images/jpeg-home.jpg',
                         caption='how photo?',
                         reply_markup=ikb)
    await asyncio.sleep(10)
    await message.delete()


@dp.callback_query_handler(text='close')
async def ikb_close(callback: types.CallbackQuery) -> None:
    await callback.message.delete()


@dp.callback_query_handler()
async def ikb_close(callback: types.CallbackQuery) -> None:
    global is_voted
    if not is_voted:
        if callback.data == 'like':
            await callback.answer('You like')
            is_voted = True
        await callback.answer('You dislike')
        is_voted = True
    await callback.answer(show_alert=True,
                          text='You voted')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)