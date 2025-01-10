import telebot
from logic import get_class

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7944235498:AAHfZu9NNwSQ-ymT3AQrPPeohQxGNEK5Ep8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(content_types=['photo'])
def photo_fun(message):
    if not message.photo:
        return bot.send_message(message.chat.id,"Вы забыли загрузить картинку")
    
    file_info = bot.get_file(message.photo[-1].file_id) 
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    result = get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=file_name)
    if result == 1 :
        result = "Cиница"
    elif result == 0 :
        result = "голуби"
    elif result == 2 :
        result = "попугаи"
    else:
        result = "это что ?(проверьте правильный ли у вас формат картинки)"
    bot.send_message(message.chat.id,result)


# Запускаем бота
bot.polling("7944235498:AAHfZu9NNwSQ-ymT3AQrPPeohQxGNEK5Ep8")