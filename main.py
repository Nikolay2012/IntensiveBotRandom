import telebot

#Підключаю бота до телеграму
bot = telebot.TeleBot('5660951250:AAGP1q1REgAG2ViX4TNM4Q_lntqf61mtdpA')

@bot.message_handler(commands=['start'])

def bot_start(message):

    bot.send_message(message.chat.id, "Hello, User!")


bot.polling()
