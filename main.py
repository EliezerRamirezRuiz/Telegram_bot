# SECRET TOKEN
from decouple import config
# LIBRARY
import telebot 
import threading

""" CODE FOR TELEGRAM BOT """
# INSTANCE ABOUT BOT WITH TOKEN FROM .ENV
tb = telebot.TeleBot(config('TELEGRAM_TOKEN'), parse_mode=None)

""" COMMANDS"""
# SEND MESSAGE TO KNOW THE BOT
@tb.message_handler(commands=["start"])
def cmd_start(message):
    tb.reply_to(message, "Welcome Coder, enjoy the chat. IF you need help, type or write /help")


# SEND MESSAGE FOR HELP
@tb.message_handler(commands=["help"])
def cmd_help(message):
    tb.reply_to(message, "to see schedule about duoc, type /DAY_NAME.")


# SEND PHOTO 
@tb.message_handler(commands=["monday_duoc"])
def cmd_help(message):
    tb.send_chat_action(message.chat.id, "upload_photo")
    photo = open("img/monday.jpg", "rb")
    tb.send_photo(message.chat.id, photo, "Schedule monday")


# SEND PHOTO 
@tb.message_handler(commands=["tuesday_duoc"])
def cmd_help(message):
    tb.send_chat_action(message.chat.id, "upload_photo")
    photo = open("img/tuesday.jpg", "rb")
    tb.send_photo(message.chat.id, photo, "Schedule tuesday")


# SEND PHOTO 
@tb.message_handler(commands=["wednesday_duoc"])
def cmd_help(message):
    tb.send_chat_action(message.chat.id, "upload_photo")
    photo = open("img/wednesday.jpg", "rb")
    tb.send_photo(message.chat.id, photo, "Schedule wednesday")


# SEND PHOTO 
@tb.message_handler(commands=["thursday_duoc"])
def cmd_help(message):
    tb.send_chat_action(message.chat.id, "upload_photo")
    photo = open("img/thursday.jpg", "rb")
    tb.send_photo(message.chat.id, photo,"Here is your timetable about thursday")


# SEND PHOTO 
@tb.message_handler(commands=["friday_duoc"])
def cmd_help(message):
    tb.send_chat_action(message.chat.id, "upload_photo")
    photo = open("img/friday.jpg", "rb")
    tb.send_photo(message.chat.id, photo,"Here is your timetable about friday")


# SEND PHOTO 
@tb.message_handler(commands=["saturday_duoc"])
def cmd_help(message):
    tb.send_chat_action(message.chat.id, "upload_photo")
    photo = open("img/saturday.jpg", "rb")
    tb.send_photo(message.chat.id, photo,"Schedule saturday")


# LOOP INFINITY
def check_message():
    tb.infinity_polling(interval=0,timeout=20)


if __name__ == '__main__':
    print("Bot starting")
    init_thread = threading.Thread(name='first_thread', target=check_message)
    init_thread.start()
    print("the bot will be working")
