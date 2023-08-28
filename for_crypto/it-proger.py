import telebot
import webbrowser

bot = telebot.TeleBot('6446700278:AAG2luQ6hJINIcWphrMSIyTHPok1zflQrd4')


@bot.message_handler(commands=['start'])
def site(message):
    bot.send_message(message.chat.id, 'hi')
    file = open('./photo.png', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'hi':
        bot.send_message(message.chat.id, 'gg')


@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://rezka.ag/series/drama/1929-ostrye-kozyrki-2013.html#t:6-s:5-e:3')


bot.infinity_polling()