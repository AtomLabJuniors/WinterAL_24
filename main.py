from telebot import TeleBot, types
from dotenv import load_dotenv, find_dotenv
from os import getenv

# Get token for Telegram bot from file '.env
load_dotenv(find_dotenv())
TOKEN = getenv("TOKEN")


# Initilaze Telegram Bot
bot = TeleBot(TOKEN, 'markdown')


@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    bot.reply_to(message, f"Привет, *{message.from_user.full_name}*! Как дела?")


if __name__ == '__main__':
    bot.infinity_polling()
