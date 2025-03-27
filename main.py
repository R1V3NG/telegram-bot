import telebot
import config
import random


jokes = ["Как называют человека, который продал свою печень? Обеспеченный"
,"Почему шутить можно над всеми, кроме безногих?\nШутки про них обычно не заходят", "Почему безногий боится гопников?\n"
"Не может постоять за себя." , "Почему толстых женщин не берут в стриптиз?\n"
"Они перегибают палку.","Почему в Африке так много болезней?\n Потому что таблетки нужно запивать водой.","Что сказал слепой, войдя в бар?\n"
"Всем привет, кого не видел"]
bot = telebot.TeleBot(config.TG_API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Как дела?")

@bot.message_handler(commands=['rnd'])
def random_number(message):
	bot.reply_to(message, str(random.randint(1,3)))

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "/start - Приветствие \n "
    "/rnd - Рандомное число от 1 до 3 \n "
    "/about - О создателе \n /math - Случайное уравнение \n "
    "/joke - Случайная шутка")

@bot.message_handler(commands=['about'])
def send_about(message):
	bot.reply_to(message, "Создатель: Хадиулин Дамир 2 курс ИСТ")

@bot.message_handler(commands=['joke'])
def send_joke(message):
	bot.reply_to(message, jokes[random.randint(0, len(jokes))])

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

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text.lower() == "Ё чё как?".lower():
		bot.send_message(message.chat.id, "Норм я")
	if message.text.lower() == "Что нового?".lower():
		bot.send_message(message.chat.id, "Да ничего, всё по старому")
	if message.text.lower() == "Что делаешь?".lower():
		bot.send_message(message.chat.id, "Да фигнёй маюсь")

bot.infinity_polling()