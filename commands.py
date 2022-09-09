import telebot
import quotebot
import random
import api

API_KEY = api.API_
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    message_ = "You can control me by using these commands\n/sendquote - To get quote"
    bot.send_message(message.chat.id, message_)

@bot.message_handler(commands=['sendquote'])
def send_quote(message):
    rand_num = random.choice(range(0, 100, 2))
    quote = quotebot.msg(rand_num)
    bot.send_message(message.chat.id, quote)

bot.polling()

def send_quote():
    rand_num = random.choice(range(0, 100, 2))
    quote = quotebot.msg(rand_num)
    bot.send_message(quote)

print(send_quote())