import telebot
import torch
from telebot import types
from simpletransformers.classification import ClassificationModel, ClassificationArgs

bot = telebot.TeleBot('5587548573:AAEcIvCllm1AZGPH9iI30NhImYOaTPnKaSI')

model1 = ClassificationModel(
    "bert", "model/0", use_cuda=False
)
model2 = ClassificationModel(
    "bert", "model/1", use_cuda=False
)
model3 = ClassificationModel(
    "bert", "model/2", use_cuda=False
)
model4 = ClassificationModel(
    "bert", "model/3", use_cuda=False
)
model5 = ClassificationModel(
    "bert", "model/4", use_cuda=False
)
model6 = ClassificationModel(
    "bert", "model/5", use_cuda=False
)
model7 = ClassificationModel(
    "bert", "model/6", use_cuda=False
)
model8 = ClassificationModel(
    "bert", "model/7", use_cuda=False
)
model9 = ClassificationModel(
    "bert", "model/8", use_cuda=False
)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("О проекте")
    btn3 = types.KeyboardButton('Команда проекта')
    markup.add(btn1, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот для проекта Зелёный Мир. Если ты хочешь проанализировать свой текст на наличие экологических практик, вставь свой текст и отправь его!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "О проекте"):
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton('Читать до конца', url='https://bmm2022.mca.nsu.ru/project/35'))
        bot.send_message(message.chat.id,
                         'Ученые считают, что рост потребления — это главная причина современных экологических проблем и изменения климата. Поэтому для преодоления экологического кризиса нам требуется изменить наше поведение и привычки. Однако не все зеленые инициативы и практики, которые направлены на гармонизацию наших отношений с окружающей средой, направлены на сокращение потребления.',
                         reply_markup=markup)


    elif (message.text == 'Команда проекта'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Студенты")
        b2 = types.KeyboardButton("Кураторы")
        b3 = types.KeyboardButton("Заказчик")
        back = types.KeyboardButton("В главное меню")
        markup.add(b1, b2, b3, back)
        bot.send_message(message.chat.id, text="Кто тебя интересует?", reply_markup=markup)

    elif (message.text == 'Студенты'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Тимур Еникеев")
        b2 = types.KeyboardButton("Арсений Ходырев")
        b3 = types.KeyboardButton("Всеволод Боровинский")
        back = types.KeyboardButton("Назад к выбору")
        markup.add(b1, b2, b3, back)
        bot.send_message(message.chat.id, text="Кто из студентов тебя интересует?", reply_markup=markup)

    elif (message.text == 'Кураторы'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Глазкова Анна")
        b2 = types.KeyboardButton("Захаров Антон")
        b3 = types.KeyboardButton("Москвина Наталья")
        back = types.KeyboardButton("Назад к выбору")
        markup.add(b1, b2, b3, back)
        bot.send_message(message.chat.id, text="Кто из кураторов тебя интересует?", reply_markup=markup)

    elif (message.text == 'Заказчик'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Захарова Ольга")
        back = types.KeyboardButton("Назад к выбору")
        markup.add(b1, back)
        bot.send_message(message.chat.id, text="Захарова Ольга", reply_markup=markup)

    elif (message.text == 'Глазкова Анна'):
        markup = types.InlineKeyboardMarkup(row_width=2)
        b1 = types.InlineKeyboardButton('Ссылка на Telegram', url='https://t.me/anglaz')
        markup.add(b1)
        bot.send_message(message.chat.id, 'Ссылки на соцсети', reply_markup=markup)

    elif (message.text == 'Тимур Еникеев'):
        markup = types.InlineKeyboardMarkup(row_width=2)
        b1 = types.InlineKeyboardButton('Ссылка на VK', url='vk.com/tenikeev')
        b2 = types.InlineKeyboardButton('Ссылка на Telegram', url='https://t.me/enikeyy')
        markup.add(b1, b2)
        bot.send_message(message.chat.id, 'Соцсети Тимура', reply_markup=markup)

    elif (message.text == 'Захаров Антон'):
        markup = types.InlineKeyboardMarkup(row_width=2)
        b1 = types.InlineKeyboardButton('Ссылка на Telegram', url='https://t.me/enikeyy')
        markup.add(b1)
        bot.send_message(message.chat.id, 'Ссылки на соцсети', reply_markup=markup)

    elif (message.text == 'Арсений Ходырев'):
        markup = types.InlineKeyboardMarkup(row_width=2)
        b1 = types.InlineKeyboardButton('Ссылка на Telegram', url='https://t.me/seninoseno')
        markup.add(b1)
        bot.send_message(message.chat.id, 'Ссылки на соцсети', reply_markup=markup)

    elif (message.text == 'Москвина Наталья'):
        markup = types.InlineKeyboardMarkup(row_width=2)
        b1 = types.InlineKeyboardButton('Ссылка на Telegram', url='https://t.me/Moskvina_Natalia')
        markup.add(b1)
        bot.send_message(message.chat.id, 'Ссылки на соцсети', reply_markup=markup)

    elif (message.text == 'Всеволод Боровинский'):
        markup = types.InlineKeyboardMarkup(row_width=2)
        b1 = types.InlineKeyboardButton('Ссылка на Telegram', url='https://t.me/enikeyy')
        markup.add(b1)
        bot.send_message(message.chat.id, 'Ссылки на соцсети', reply_markup=markup)

    elif (message.text == 'Захарова Ольга'):
        markup = types.InlineKeyboardMarkup(row_width=2)
        b1 = types.InlineKeyboardButton('Ссылка на Telegram', url='https://t.me/enikeyy')
        markup.add(b1)
        bot.send_message(message.chat.id, 'Ссылки на соцсети', reply_markup=markup)

    elif (message.text == 'Назад к выбору'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("Студенты")
        b2 = types.KeyboardButton("Кураторы")
        b3 = types.KeyboardButton("Заказчик")
        back = types.KeyboardButton("В главное меню")
        markup.add(b1, b2, b3, back)
        bot.send_message(message.chat.id, text="Кто тебя интересует?", reply_markup=markup)

    elif (message.text == 'Остальные'):
        bot.send_message(message.chat.id, 'В разработке')

    elif (message.text == 'В главное меню'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("О проекте")
        btn3 = types.KeyboardButton('Команда проекта')
        markup.add(btn1, btn3)
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Я начал анализ', reply_markup=markup)
        arr_ = []
        ans = ''
        predictions, raw_outputs = model1.predict([message.text])
        if predictions[0] == 1:
            ans += 'Сортировка отходов(1), '
        predictions, raw_outputs = model2.predict([message.text])
        if predictions[0] == 1:
            ans += 'Изучение маркировки упаковки(2), '
        predictions, raw_outputs = model3.predict([message.text])
        if predictions[0] == 1:
            ans += 'Переработка отходов(3), '
        predictions, raw_outputs = model4.predict([message.text])
        if predictions[0] == 1:
            ans += 'Петиции(4), '
        predictions, raw_outputs = model5.predict([message.text])
        if predictions[0] == 1:
            ans += 'Отказ от покупок(5), '
        predictions, raw_outputs = model6.predict([message.text])
        if predictions[0] == 1:
            ans += 'Обмен(6),'
        predictions, raw_outputs = model7.predict([message.text])
        if predictions[0] == 1:
            ans += 'Совместное использование(7), '
        predictions, raw_outputs = model8.predict([message.text])
        if predictions[0] == 1:
            ans += 'Продвижение ответственного потребления(8), '
        predictions, raw_outputs = model9.predict([message.text])
        if predictions[0] == 1:
            ans += 'Ремонт(9)'
        bot.send_message(message.chat.id, f'В вашем тексте найдены следующие практики: {ans} практики !')


bot.polling(none_stop=True)
