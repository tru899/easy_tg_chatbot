import telebot
import json

bot = telebot.TeleBot('8101189070:AAGbCFL7Ab3NX56w5B-qkfZvdIi4ziBarVI')
channel_id = -1002380948949
saved_messages = []

# def save_message(message):
#     data = {
#         'chat id': message.chat.id,
#         'user': message.from_user.username or message.from_user.first_name,
#         'text': message.text
#     }
#
#     saved_messages.append(data)
#
#     with open('saved_messages.json', 'w') as file_in:
#         json.dump(saved_messages, file_in, indent=4)
#     bot.reply_to(message, f"Ваше сообщение сохранено: {message.text}")

commands = [
    telebot.types.BotCommand('start', 'Начать'),
    # telebot.types.BotCommand('send', 'Отправить сообщение')
]
bot.set_my_commands(commands)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '''<i>Привет! Здесь ты можешь поделиться своими мыслями, идеями и переживаниями. 
Если хочешь пообщаться лично, то оставь свои контакты для связи. \n\n\nС уважением, Ваш qwerty\n\n🌙</i>''', parse_mode='HTML')

# @bot.message_handler(commands=['send'])
# def send_message(message):
#     bot.send_message(message.chat.id, '<i>Можешь написать что-то снова\n\n🌙</i>', parse_mode='HTML')

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, '<i>Можешь написать что-то снова\n\n🌙</i>', parse_mode='HTML')

    try:
        bot.forward_message(channel_id, message.chat.id, message.message_id)
    except Exception as e:
        print(f'error: {e}')

bot.polling(non_stop=True)
