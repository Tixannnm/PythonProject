import telebot

bot = telebot.TeleBot("7702304027:AAHl2npakGzxVO5sN5iQJ13-rl6OwUYdAXU")

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Привіт!")
    sti = open('Hi.png', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Напиши команду /help щоб дізнатися про всі команди")

@bot.message_handler(commands=["help"])
def welcome(message):
    bot.send_message(message.chat.id, "/help - показує всі команди\n/lol - каже анекдот\n/BMWX5 - кидає картинку BMW X5\n/audio - кидає гімн України\n/film - кидає картинку залізної людини\n/music - кидає мою улюблену музику Skillet Monster\n/friends - пише ім'я усіх моїх друзів\n/sport - пише мі удюблений види спорту\n/book - кидає назву моїй улюблений книги")

@bot.message_handler(commands=["lol"])
def welcome(message):
    bot.send_message(message.chat.id, "знаешь почему не честно драться против беременной женщины? \nпотому-что 2 на 1 не честно")

@bot.message_handler(commands=['BMWX5'])
def stickers(message):
    sti = open('BMWX5.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands=['film'])
def stickers(message):
    bot.send_message(message.chat.id, "Мій улюблений фільм це Залізна людина")
    sti = open('ironman.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands=['music'])
def stickers(message):
    bot.send_message(message.chat.id, "Моя улюблена музика це Skillet Monster")
    music = open('Skillet _Monster.mp3', 'rb')
    bot.send_audio(message.chat.id, music)

@bot.message_handler(commands=['friends'])
def stickers(message):
    bot.send_message(message.chat.id, "Ось усі мої друзі - Микита, Анна, Максим, Іван, Данило, Олександр")

@bot.message_handler(commands=['sport'])
def stickers(message):
    bot.send_message(message.chat.id, "Мій улюблений спорт це футбол та баскетбол")
    sti = open('football.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
    sti = open('basktball.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands=['book'])
def stickers(message):
    bot.send_message(message.chat.id, "Моя улюблена книга це Гаррі Поттер та філософський камінь")
    sti = open('GariiPoter.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands=['audio'])
def stickers(message):
    music = open('rington.mp3', 'rb')
    bot.send_audio(message.chat.id, music)



bot.polling()