
from telebot import TeleBot, types
from classes import Book
from dotenv import load_dotenv, find_dotenv
from os import getenv

# Get token for Telegram bot from file '.env
load_dotenv(find_dotenv())
TOKEN = getenv("TOKEN")

CLASSES = types.InlineKeyboardMarkup()
CLASSES.keyboard = [
    [types.InlineKeyboardButton(str(i), callback_data=f"{i}_class") for i in range(1, 5)], 
    [types.InlineKeyboardButton(str(i), callback_data=f"{i}_class") for i in range(5, 9)],
    [types.InlineKeyboardButton(str(i), callback_data=f"{i}_class") for i in range(9, 12)]
]

SUBJECTS = types.InlineKeyboardMarkup()
SUBJECTS.keyboard =[
    types.InlineKeyboardButton("Математика", callback_data="math_subject"), 
    types.InlineKeyboardButton("Русский Язык", callback_data="russian_subject")
]

BACK = types.InlineKeyboardButton("Обратно", callback_data="back")

MATH = types.InlineKeyboardMarkup()
MATH.keyboard = [types.InlineKeyboardButton(text=book.author, callback_data=f"{book.bid}_math_textbook") 
        for book in [Book(1, "атасян"), Book(2, "атасян с углублением"), Book(3, "и т. д.")]
]

RUSSIAN = types.InlineKeyboardMarkup()
RUSSIAN.keyboard = [types.InlineKeyboardButton(text=book.author, callback_data=f"{book.bid}_russian_textbook") 
        for book in [Book(1, "ладыжская"), Book(2, "ладыжская с углублением"), Book(3, "и т. п.")]
]

DICT_SUBJECTS = {
    "8_math_subject": MATH,
    "8_russian_subject": RUSSIAN
}

new_keyboard = lambda menu, call: types.InlineKeyboardMarkup(keyboard=[[
    types.InlineKeyboardButton(text=button['text'], 
                                callback_data=f'{call.data.split("_")[0]}_' + button['callback_data']) 
    for button in map(lambda b: b.to_dict(), menu.keyboard)], [BACK]])