import telebot
from telebot import types

bot = telebot.TeleBot('6195968446:AAG3_rkpC-BhfFJ4lwLZv8Z9GNchJGT0hDc')

@bot.message_handler(commands=['start'])
def start(message):
    ms = f'Здравствуйте, <b>{message.from_user.first_name}</b>, выберите тематику <u>сайта</u>.'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    video = types.KeyboardButton ('Кино')
    game = types.KeyboardButton ('Игры')
    book = types.KeyboardButton ('Книги')
    markup.add (video, game, book)
    bot.send_message(message.chat.id, ms, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def content(message):
    if message.text == 'Кино':
        markup_video = types.InlineKeyboardMarkup()
        markup_video.add(types.InlineKeyboardButton('Кинопоиск', url = 'www.kinopoisk.ru'))
        bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup_video)
    elif message.text == 'Игры':
        markup_game = types.InlineKeyboardMarkup()
        markup_game.add(types.InlineKeyboardButton('Steam', url = 'store.steampowered.com'))
        bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup_game)
    elif message.text == 'Книги':
        markup_book = types.InlineKeyboardMarkup()
        markup_book.add (types.InlineKeyboardButton('Литрес', url = 'https://www.litres.ru/'))
        bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup_book)


@bot.message_handler(commands=['video'])
def video (message):
    markup_video = types.InlineKeyboardMarkup()
    markup_video.add (types.InlineKeyboardButton('Кинопоиск', url='www.kinopoisk.ru'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup_video)



bot.polling(none_stop=True)