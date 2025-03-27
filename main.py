import telebot
import config
import random

math_eq = []
x = 0
def generate_equation():
    for a in range(1, 1000): 
        for b in range(1, 10000):  
            if b % a == 0:
                x = b // a
                math_eq.append(f'[{a}x = {b} | Ответ x = {x}')  
    return math_eq
math_eq = generate_equation()
equation = math_eq[random.randint(1, len(math_eq))][0]
print(equation)
jokes = ["Как называют человека, который продал свою печень? Обеспеченный"
,"Почему шутить можно над всеми, кроме безногих? Шутки про них обычно не заходят", "Почему безногий боится гопников?"
"Не может постоять за себя." , "Почему толстых женщин не берут в стриптиз?"
"Они перегибают палку.","Почему в Африке так много болезней? Потому что таблетки нужно запивать водой.","Что сказал слепой, войдя в бар?"
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
    bot.send_message(message.chat.id, f" {math_eq[random.randint(1, len(math_eq))[0]]} || {math_eq[random.randint(1, len(math_eq))[1]]} ||", parse_mode='MarkdownV2')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text.lower == "ЁУ чё как?".lower:
		bot.send_message(message.chat.id, "Норм я")
	if message.text.lower == "Что нового?".lower:
		bot.send_message(message.chat.id, "Да ничего, всё по старому")
	if message.text.lower == "Что делаешь?".lower:
		bot.send_message(message.chat.id, "Да фигнёй маюсь")

bot.infinity_polling()