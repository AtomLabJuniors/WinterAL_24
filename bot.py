from telebot import TeleBot, types
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

TOKEN = "TOKEN"


# Initilaze Telegram Bot
bot = TeleBot(TOKEN, 'markdown')


@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Разработчики")
    markup.add(btn1)
    bot.reply_to(message, f"Привет, *{message.from_user.full_name}*! Как дела?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Разработчики":
        bot.send_message(message.chat.id, text="@PaulBaranas, @Usmoni03, @MrFriot, @plushkkkk")

if __name__ == '__main__':
    bot.infinity_polling()
