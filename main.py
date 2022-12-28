# Підключаємо модуля для створення ботів
import telebot
# ідентифікатори
# message.from_user.first_name - отримуємо перше ім'я користувача з повідомлення до бота
# message.from_user.username - отримуємо псевдонім користувача з повідомлення до бота
# message.from_user.last_name - отримуємо друге ім'я (прізвище) користувача з повідомлення до бота
# message.chat.id - отримує id чата відправника
# message.text - 

# Підключаю бота до телеграму
bot = telebot.TeleBot('5660951250:AAGP1q1REgAG2ViX4TNM4Q_lntqf61mtdpA')
# задаємо обробку повідомлень
@bot.message_handler(commands=['start'])
# Фукнція що обробляє команду "/start"
def bot_start(message):
    print(message)
    # бот відправляє повідомлення користувачу, що відправив команду "/start"
    bot.send_message(message.chat.id, "Hello, User!")
    bot.register_next_step_handler(message, all_messages)

#
def all_messages(message):
    if message.text.lower() == "play":
        bot.send_message(message.chat.id, "Starting the game")
    if message.text.lower() == "/hi":
        bot.send_message(message.chat.id, f"Nice to meet you! {message.from_user.username}!")
    #
    bot.register_next_step_handler(message, all_messages)
# опитує команди
bot.polling()
