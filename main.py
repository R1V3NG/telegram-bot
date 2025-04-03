import telebot
from telebot import types
import config
import random


jokes = ["Как называют человека, который продал свою печень? Обеспеченный"
,"Почему шутить можно над всеми, кроме безногих?\nШутки про них обычно не заходят", "Почему безногий боится гопников?\n"
"Не может постоять за себя." , "Почему толстых женщин не берут в стриптиз?\n"
"Они перегибают палку.","Почему в Африке так много болезней?\n Потому что таблетки нужно запивать водой.","Что сказал слепой, войдя в бар?\n"
"Всем привет, кого не видел", "Чего общего у некрофила и владельца строительной кампании?\nОни оба имеют недвижимость.", "Почему цыган не отправляют на олимпиаду?\nОни заберут все золото.", "—Врач приходит к пациенту в палату и говорит:\n— Больной, у меня для вас две новости — хорошая и плохая. С какой начать?\n— Доктор, давайте с хорошей.\n— Эту болезнь назовут вашим именем.",
"— Не знаю, что делать. Тараканы замучали. Всюду шастают — покоя нет.\n— А ты купи мелок для тараканов.\n— А что, помогает?\n— Конечно. Видишь — сидят в углу, рисуют…",
"В Чечню привезли шоу с крокодилами. Было ну очень страшно...\nНо, переборов страх, ... крокодилы все-таки выступили.", "Москва. Две узбечки ведут детей в школу.\nОдна спрашивает у другой:\n— Ну как вам новая школа?\n— Очень хорошая, только русских много.",
"Программист жене по телефону:\n— Дорогая, мне посуду мыть или ты вернёшься и сама помоешь?\n— Хорошо мой любимый.\nПрограммист впал в ступор т. к. не смог выбрать из «хорошо, мой любимый», «хорошо, мой, любимый» и «хорошо мой, любимый»."]
bot = telebot.TeleBot(config.TG_API_TOKEN)

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
    bot.send_message(message.chat.id, "Выберите что вы хотите сделать", reply_markup=markup)

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
@bot.callback_query_handler(func=lambda call: call.data in ['show_start', 'show_rnd', 'show_math', 'show_joke', 'show_about'])
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
    joke = jokes[random.randint(0, len(jokes) - 1)]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_repeat = types.KeyboardButton("Скажи другую шутку")
    markup.add(btn_repeat)
    bot.send_message(message.chat.id, joke, reply_markup=markup)

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
    options = [solution, solution + random.randint(1, 10), solution - random.randint(1, 10), solution + random.randint(11, 20)]
    random.shuffle(options) 
    markup = types.InlineKeyboardMarkup()
    for option in options:
        markup.add(types.InlineKeyboardButton(str(option), callback_data=f'answer_{option}_{solution}'))
    bot.send_message(message.chat.id, f"{equation} <tg-spoiler>  Ответ x = {solution} </tg-spoiler>", parse_mode='HTML', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('answer_'))
def check_answer(call):
    try:
        _, user_answer, correct_answer = call.data.split('_')
        user_answer = int(user_answer)
        correct_answer = int(correct_answer)
        if user_answer == correct_answer:
            bot.answer_callback_query(call.id, "Правильно! ✅")
        else:
            bot.answer_callback_query(call.id, "Неправильно. Попробуйте снова! ❌")
    except (IndexError, ValueError):
        bot.answer_callback_query(call.id, "Ошибка обработки ответа")


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Скажи другую шутку":
        send_joke(message)  # Вызов функции send_joke для повторного показа шутки
    elif(message.text == "👋 Поприветствовать"):
        bot.send_message(message.chat.id, text="Ну привет, как делишки?")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        btn3 = types.KeyboardButton("Как ты?")
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
