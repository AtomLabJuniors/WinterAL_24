from constans import *


# Initilaze Telegram Bot
bot = TeleBot(TOKEN, 'markdown')


# start command handler
@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    bot.reply_to(message, f"Привет, *{message.from_user.full_name}*! Выбери свой класс:", reply_markup=CLASSES)


@bot.callback_query_handler(func=lambda callback: callback.data.endswith("class"))
def class_choice(call: types.CallbackQuery):
    cid = (message := call.message).chat.id
    [print(button) for button in SUBJECTS.keyboard]
    bot.edit_message_text("Выбери предмет:", cid, message.id, reply_markup=new_keyboard(SUBJECTS, call))


@bot.callback_query_handler(func=lambda callback: callback.data.endswith("subject"))
def subject_choice(call: types.CallbackQuery):
    cid = (message := call.message).chat.id
    try:
        bot.edit_message_text("Выбери учебник:", cid, message.id, reply_markup=new_keyboard(DICT_SUBJECTS[call.data], call))
    except KeyError:
        bot.edit_message_text("Учебника на такой класс нет", cid, message.id, reply_markup=types.InlineKeyboardMarkup(keyboard=[[BACK]]))


@bot.callback_query_handler(func=lambda callback: callback.data.endswith("textbook"))
def number_choice(call: types.CallbackQuery):
    cid = (message := call.message).chat.id
    bot.edit_message_text("Введите номер:", cid, message.id)
    bot.register_next_step_handler_by_chat_id(cid, lambda message: number_get(message, call))


def number_get(message: types.Message, callback: types.CallbackQuery):
    try:
        float(message.text.replace(",", "."))
    except ValueError:
        bot.reply_to(message, "Неверный номер!\nВведите еще раз: ")
        return bot.register_next_step_handler_by_chat_id(message.chat.id, lambda message: number_get(message, callback))
    number, [subject_class, bookid, subject] = float(message.text), callback.data.split('_')[:-1]
    print(f"get_textbook(subject=\"{subject}\", bookid=\"{bookid}\", number=\"{number}\", class=\"{subject_class}\")")
    bot.reply_to(message, "Успешно!")

@bot.callback_query_handler(func=lambda callback: callback.data.endswith("back"))
def back(call: types.CallbackQuery):
    cid = (message := call.message).chat.id
    bot.edit_message_text(f"Привет, *{message.from_user.full_name}*! Выбери свой класс:", cid, message.id, reply_markup=CLASSES)


if __name__ == '__main__':
    bot.infinity_polling()
