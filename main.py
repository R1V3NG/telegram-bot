import telebot
from telebot import types
import config
import random


jokes = ["Как называют человека, который продал свою печень? Обеспеченный"
,"Почему шутить можно над всеми, кроме безногих?\nШутки про них обычно не заходят", "Почему безногий боится гопников?\n"
"Не может постоять за себя." , "Почему толстых женщин не берут в стриптиз?\n"
"Они перегибают палку.","Почему в Африке так много болезней?\n Потому что таблетки нужно запивать водой.","Что сказал слепой, войдя в бар?\n"
"Всем привет, кого не видел", "Чего общего у некрофила и владельца строительной кампании?\nОни оба имеют недвижимость.", "Почему цыган не отправляют на олимпиаду?\nОни заберут все золото."]
bot = telebot.TeleBot(config.TG_API_TOKEN)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.reply_to(message, "Как дела?")
	
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сайт болота", url='https://nti.urfu.ru/')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на моё болото)".format(message.from_user), reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поприветствовать")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2) 

@bot.message_handler(commands=['rnd'])
def random_number(message):
	bot.reply_to(message, str(random.randint(1,3)))

@bot.message_handler(commands=['help'])
def send_help(message):
    markup = types.InlineKeyboardMarkup()
    btn_start = types.InlineKeyboardButton("/start", callback_data='show_start')
    btn_rnd = types.InlineKeyboardButton("/rnd", callback_data='show_rnd')
    btn_math = types.InlineKeyboardButton("/math", callback_data='show_math')
    btn_joke = types.InlineKeyboardButton("/joke", callback_data='show_joke')
    btn_about = types.InlineKeyboardButton("/about", callback_data='show_about')
    markup.add(btn_start, btn_rnd, btn_math, btn_joke, btn_about)
    bot.send_message(message.chat.id, "Выберите нужную команду, чтобы вывести описание", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'show_start':
        bot.send_message(call.message.chat.id, "/start — Команда для приветствия")
    elif call.data == 'show_rnd':
        bot.send_message(call.message.chat.id, "/rnd — Команда для вывода случайного числа в диапазоне от 1 до 3 включительно")
    elif call.data == 'show_math':
        bot.send_message(call.message.chat.id, "/math — Команда для вывода случайного уравнения")
    elif call.data == 'show_joke':
        bot.send_message(call.message.chat.id, "/joke — Команда для вывода случайной шутки")
    elif call.data == 'show_about':
        bot.send_message(call.message.chat.id, "/about — Команда для вывода информации об разработчике")


@bot.message_handler(commands=['about'])
def send_about(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Моя страничка в гите)", url='https://github.com/R1V3NG')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, Я создатель этого бота! Нажми на кнопку и перейди на мою страницу)".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['joke'])
def send_joke(message):
    bot.reply_to(message, jokes[random.randint(0, len(jokes) - 1)])

@bot.message_handler(commands=['math'])
def math(message):
    a = random.randint(1, 1000)  
    x = random.randint(1, 1000)  
    operation = random.choice(['+', '-', '*'])
    c = random.randint(1, 1000)  
    if operation == '+':
        b = a * x + c
        equation = f"{a}x + {c} = {b}"
        solution = (b - c) // a  
    elif operation == '-':
        b = a * x - c
        equation = f"{a}x - {c} = {b}"
        solution = (b + c) // a 
    elif operation == '*':
        b = a * x * c
        equation = f"{a}x * {c} = {b}"
        solution = b // (a * c)  # Решение для x
    bot.send_message(message.chat.id, f"{equation} <tg-spoiler>  Ответ x = {solution} </tg-spoiler>", parse_mode='HTML')

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поприветствовать"):
        bot.send_message(message.chat.id, text="Ну привет, как делишки?")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        btn3 = types.KeyboardButton("Как я?")
        btn4 = types.KeyboardButton("Что нового?")
        btn5 = types.KeyboardButton("Что делаешь?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5,  back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "Меня обычно не зовут, я сам прихожу. Ну а если серьёзно, я Шрек")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Я много что могу, например рассказать тебе шутку")
    elif message.text == "Как ты?":
        bot.send_message(message.chat.id, text="Заебумба")
    elif message.text == "Что нового?":
        bot.send_message(message.chat.id, text="Да ничего прям такого, не считая моей женитьбы")
    elif message.text == "Что делаешь?":
        bot.send_message(message.chat.id, text="С детишками вожусь")  
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поприветствовать")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Я тебя не понял, попробуй нажать кнопки")

bot.infinity_polling()
