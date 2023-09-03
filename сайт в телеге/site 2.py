import telebot
from token_tg import api_tg
from currency_converter import CurrencyConverter
from telebot.types import *

bot = telebot.TeleBot(api_tg)
currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start9(message):
    bot.send_message(message.chat.id, 'Send sum...')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Должно быть число, впишите сумму...')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        markup = InlineKeyboardMarkup(row_width=2)
        btn1 = InlineKeyboardButton('USD->EUR', callback_data='usd/eur')
        btn2 = InlineKeyboardButton('EUR->USD', callback_data='eur/usd')
        btn3 = InlineKeyboardButton('UAH->USD', callback_data='uah/usd')
        btn4 = InlineKeyboardButton('PLN->USD', callback_data='pln/usd')
        btn5 = InlineKeyboardButton('GBP->USD', callback_data='gbp/usd')
        btn6 = InlineKeyboardButton('Другая пара', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        bot.send_message(message.chat.id, 'Выберете пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше нуля, впишите сумму...')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'else':
        bot.send_message(call.message.chat.id, 'Введи пару с примера: USD/EUR')
        bot.register_next_step_handler(call.message, my_currency)
    else:
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f"{amount} {values[0]} -> {round(res, 2)} {values[1]}")
        bot.register_next_step_handler(call.message, summa)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f"{amount} {values[0]} -> {round(res, 2)} {values[1]}")
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Ввели неверный формат...')
        bot.register_next_step_handler(message, my_currency)


bot.polling(none_stop=True)