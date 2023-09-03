import telebot
import requests
import json
from token_tg import api_tg


bot = telebot.TeleBot(api_tg)
API_weather = 'a33f1ccc604ae4a2a760576fdbfeedc6'


@bot.message_handler(content_types=['text'])
def send_temp(message):
    city = message.text.strip().lower()
    req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_weather}&units=metric')
    if req.status_code == 200:
        data = json.loads(req.text)
        bot.send_message(message.chat.id, f"{round(float(data['main']['temp']))}")
    else:
        bot.send_message(message.chat.id, 'Город указан не верно')


bot.polling(none_stop=True)