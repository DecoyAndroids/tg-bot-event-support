import telebot
from telebot import types


bot = telebot.TeleBot('6790289233:AAEYF-avnqb1aAukBo8C4veHZa1P1kEWet8')


@bot.message_handler(commands=['start'])
def start(message):
    mass = f"👋 Привет {message.from_user.first_name}! Я бот который поможет тебе в обратной связи с организаторами мероприятия."
    bot.send_message(message.from_user.id, mass , parse_mode='html')
    photo1 = open('stas.jpg','rb')
    mass = f"Напиши номер своего стола и проблему, с которой столкнулась твоя команда. Так же, возможно, мы уже знаем ответ на твой вопрос, посмотри пункты в меню"
    bot.send_photo(message.from_user.id, photo=photo1 , caption=mass)
    photo1.close()

@bot.message_handler(content_types=(['text']))
def primer(message):
    if message.text != 'Отправь рассписание' and message.text != 'Отправь Вк' and message.text != 'Отправь Tg' and message.text != 'Отправить организаторам' and message.text != 'Отправь Вк чат':
        f = open('C:/Users/Дмитрий/PycharmProjects/telegabot_a/files/'+ str(message.chat.id) +'.txt', 'w')
        f.write(message.text)
        f.close()
        raspis = types.KeyboardButton('Отправь рассписание')
        vk = types.KeyboardButton('Отправь Вк')
        vk_chat = types.KeyboardButton('Отправь Вк чат')
        tg = types.KeyboardButton('Отправь Tg')
        snd = types.KeyboardButton('Отправить организаторам')
        markup = types.ReplyKeyboardMarkup()
        markup.add(raspis, vk,vk_chat , tg, snd)
        mass = "отправить организатором? Не спамь, пожалуйста, не нагружай организаторов ненужными вопросами"
        bot.send_message(message.from_user.id, mass, parse_mode='html', reply_markup=markup)
        mass1 = message.text
    if message.text == 'Отправь рассписание':
        print(message.text)
        raspis = types.KeyboardButton('Отправь рассписание')
        vk = types.KeyboardButton('Отправь Вк')
        vk_chat = types.KeyboardButton('Отправь Вк чат')
        tg = types.KeyboardButton('Отправь Tg')
        markup = types.ReplyKeyboardMarkup()
        markup.add(raspis, vk,vk_chat , tg)
        photo2 = open('stas_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo=photo2 ,parse_mode='html', reply_markup=markup)
        photo2.close()
    elif message.text == 'Отправь Вк':
        raspis = types.KeyboardButton('Отправь рассписание')
        vk = types.KeyboardButton('Отправь Вк')
        vk_chat = types.KeyboardButton('Отправь Вк чат')
        tg = types.KeyboardButton('Отправь Tg')
        markup = types.ReplyKeyboardMarkup()
        markup.add(raspis, vk,vk_chat , tg)
        bot.send_message(message.from_user.id, 'Вот ссылка: https://vk.com/cityheroes.hackathon')
    elif message.text == 'Отправь Вк чат':
        raspis = types.KeyboardButton('Отправь рассписание')
        vk = types.KeyboardButton('Отправь Вк')
        vk_chat = types.KeyboardButton('Отправь Вк чат')
        tg = types.KeyboardButton('Отправь Tg')
        markup = types.ReplyKeyboardMarkup()
        markup.add(raspis, vk,vk_chat , tg)
        bot.send_message(message.from_user.id, 'Вот ссылка: https://vk.me/join/w7LwKZMDrgeV/mmoyP38aXQ2TJjvRarB/a8=')
    elif message.text == 'Отправь Tg':
        raspis = types.KeyboardButton('Отправь рассписание')
        vk = types.KeyboardButton('Отправь Вк')
        vk_chat = types.KeyboardButton('Отправь Вк чат')
        tg = types.KeyboardButton('Отправь Tg')
        markup = types.ReplyKeyboardMarkup()
        markup.add(raspis, vk, vk_chat, tg)
        bot.send_message(message.from_user.id, 'Вот ссылка: https://t.me/city_heroes')
    elif message.text == 'Отправить организаторам':
        f = open('C:/Users/Дмитрий/PycharmProjects/telegabot_a/files/' + str(message.chat.id) + '.txt', 'r')
        text = f.read()
        f.close()
        raspis = types.KeyboardButton('Отправь рассписание')
        vk = types.KeyboardButton('Отправь Вк')
        vk_chat = types.KeyboardButton('Отправь Вк чат')
        tg = types.KeyboardButton('Отправь Tg')
        markup = types.ReplyKeyboardMarkup()
        markup.add(raspis, vk, vk_chat, tg)
        bot.send_message(message.from_user.id, 'сообщение отправленно')
        mass1 = 'Организатор, тебе тут сообщениее' + text
        chat_id = '1019790287'
        bot.send_message(chat_id, mass1)






#@bot.message_handler(content_types=(['photo']))
#def get_user_photo(message):
    #bot.send_message(message.from_user.id,'Крутое фото, щас жмыхну!', parse_mode='html')
    #file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    #downloaded_file = bot.download_file(file_info.file_path)
    #src = 'C:/Users/Дмитрий/PycharmProjects/telegabot_a/files/' + file_info.file_path
    #markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    #blur = types.KeyboardButton('Заблюрить')
    #contur = types.KeyboardButton('Выделить контуры')
    #detail = types.KeyboardButton('Улучшить качество')
    #edge = types.KeyboardButton('Четкость границ')
    #edge_more = types.KeyboardButton('Больше четкости границ')
    #emboss = types.KeyboardButton('Тиснение')
    #find_edges = types.KeyboardButton('Обводка краёв')
    #sharpen = types.KeyboardButton('Улучшение резкости')
    #smooth =types.KeyboardButton('Сглаживание артефактов')
    #smooth_more = types.KeyboardButton('Улучшенное сглаживание артефактов')
    #markup.add(blur, contur, detail, edge, edge_more, emboss, find_edges, sharpen, smooth, smooth_more)
    #with open(src, 'wb') as new_file:
        #new_file.write(downloaded_file)
    #original = Image.open('C:/Users/Дмитрий/PycharmProjects/telegabot_a/files/' + file_info.file_path)
    #filtred = original.filter(ImageFilter.FIND_EDGES)
    #f = open('C:/Users/Дмитрий/PycharmProjects/telegabot_a/files/'+ str(message.chat.id) +'.txt', 'w')
    #f.write(src)
    #f.close()
    #bot.send_message(message.chat.id, 'Что сделать с фоткой?',parse_mode='html', reply_markup=markup)
    #return src

bot.polling(none_stop=True)