import random
import telebot
import urllib.request
import urllib.error

bot = telebot.TeleBot('')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
keyboard1.row('Привет', 'Пока')
keyboard1.row('Случайную картинку!')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?', reply_markup=keyboard1)

    elif message.text.lower() == 'пока':
        bot.send_message(message.from_user.id, 'Досвидания?', reply_markup=keyboard1)

    elif message.text.lower() == 'да':
        bot.send_message(message.from_user.id, 'Нет?', reply_markup=keyboard1)

    elif message.text.lower() == 'нет':
        bot.send_message(message.from_user.id, 'Да?', reply_markup=keyboard1)

    elif message.text.lower() in ['/help', 'хелп', 'help']:
        bot.send_message(message.from_user.id, '...', reply_markup=keyboard1)

    elif message.text.lower() == '/start':
        bot.send_message(message.from_user.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

    elif message.text.lower() == 'случайную картинку!':
        bot.send_message(message.from_user.id, 'Один момент...', reply_markup=keyboard1)
        bot.send_photo(message.from_user.id, send_photo(message), reply_markup=keyboard1)

    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.', reply_markup=keyboard1)


def send_photo(message):
    rand = str(random.randint(1, 1000))
    pic = 'https://picsum.photos/id/' + rand + '/800'

    try:
        urllib.request.urlopen(pic)
    except urllib.error.HTTPError:  # если картинка не открывается, ищем другую
        pic = send_photo(message)

    return pic


if __name__ == '__main__':
    while True:
        bot.polling()
