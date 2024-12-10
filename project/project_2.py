import telebot
from telebot.types import ReplyKeyboardMarkup
import json
import time



API_token = '8171471516:AAEeYT9NTz-UsmhgRtSXcxjZ_FtTr_DoQGc'
bot = telebot.TeleBot(API_token, parse_mode=None)
currency_list = ["USD", "EUR", "UAH"]

@bot.message_handler(commands=['dump'])
def dump_bot(message):
    with open("wallets.json", "w", encoding='utf-8') as wallet_json:
        json.dump(wallets, wallet_json, ensure_ascii=False, indent=4)
    bot.send_message(message.chat.id, "Бот вивантажив інформацію про гаманці")


@bot.message_handler(commands=['balance'])
def stop_bot(message):
    wallet = wallets[str(message.chat.id)]
    if wallet["balances"] == {}:
        bot.send_message(message.chat.id, "У вас ще немає балансів у гаманці")
    else:
        for currency, value in wallet["balances"].items():
            bot.send_message(message.chat.id, f"Гаманець {currency} із рахунком {value}")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    start_message = """Вашій увазі представлено 
Бот для конвертера валют,
який дозволяє користувачам управляти
віртуальними гаманцями з різними валютами
і конвертувати суми між ними за заданими курсами.
Щоб переглянути список команд натисніть на /command
"""
    bot.send_message(message.chat.id, start_message, reply_markup=menu)
    wallet_id = message.chat.id
    user = message.from_user.full_name
    if str(wallet_id) not in wallets.keys():
        wallet_pattern = {
            "wallet_id": wallet_id,
            "balances": {
            },
            "user": user,
            "currencies": []
        }
        wallets[wallet_id] = wallet_pattern
        register_message = f"""Ми зареєстрували новий гаманець: {user} {wallet_id}"""
        bot.send_message(message.chat.id, register_message, reply_markup=menu)
    else:
        register_message = f"""Ваш гаманець вже був зареєстрований для цього аккаунта: {user} {wallet_id}"""
        bot.send_message(message.chat.id, register_message, reply_markup=menu)


@bot.message_handler(commands=['command'])
def commands(messsage):
    text_command="""Список команд:
    Запустити або переглянути опис бота - /start, /help
    Додати валюту в гаманець - /add
    Вивантажити інформацію про гаманці - /dump
    Переглянути баланси гаманців - /balance
    Оновити кількість валюти в гаманці - /update
    Переглянути список ваших валют - /currency
    """
    bot.send_message(messsage.chat.id, text_command)

@bot.message_handler(commands=['add'])
def add_currency(message):
    instructions = """Щоб додати валюту, напишіть у форматі:
валюта сума
Наприклад:
    USD 100
    UAH 2000
"""
    user_state[message.chat.id] = "adding"
    bot.send_message(message.chat.id, instructions)

@bot.message_handler(commands=['update'])
def update_currency(message):
    instructions = """Щоб оновити кількість валюти, напишіть у форматі:
валюта сума
Наприклад:
USD 50
UAH 1500
"""
    user_state[message.chat.id] = "updating"
    bot.send_message(message.chat.id, instructions, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text and len(message.text.split()) == 2)
def handle_currency_operations(message):
    user_action = user_state.get(message.chat.id)
    text = message.text.strip()
    try:
        currency, amount = text.split(" ")
        if currency in currency_list and int(amount) >= 0:
            if user_action == "adding":
                try:
                    text = message.text.strip()
                    currency, amount = text.split(" ")
                    wallet = wallets.setdefault(str(message.chat.id), {"balances": {}})
                    if currency not in wallet["balances"]:
                        wallet["balances"][currency] = float(amount)
                        wallet["currencies"]+=[currency]
                        bot.send_message(message.chat.id, f"Ви додали валюту {currency} з сумою {float(amount)}.")
                        dump_bot(message)
                    else:
                        bot.send_message(message.chat.id,f"Валюта {currency} вже існує. Введіть команду /update для оновлення балансу.")
                except Exception:
                    bot.send_message(message.chat.id, f"Виникла помилка")

            elif user_action == "updating":
                try:
                    text = message.text.strip()
                    currency, amount = text.split(" ")
                    wallet = wallets.setdefault(str(message.chat.id), {"balances": {}})
                    if currency in wallet["balances"]:
                        wallet["balances"][currency] += float(amount)
                        bot.send_message(message.chat.id, f"Баланс валюти {currency} оновлено. Додано суму: {float(amount)}.")
                        dump_bot(message)
                    else:
                        bot.send_message(message.chat.id,f"Валюта {currency} не знайдена. Введіть команду /add щоб додати нову валюту.")
                except Exception:
                    bot.send_message(message.chat.id, f"Виникла помилка")
            else:
                bot.send_message(message.chat.id,"Помилка")
        else:
            bot.send_message(message.chat.id, f"Помилка, неправильна валюта або сума. Спробуйте ввести: {currency_list} або суму більше ніж 0")
    except Exception:
        bot.send_message(message.chat.id, f"Виникла помилка")


@bot.message_handler(commands=['currency'])
def currency(message):
    wallet = wallets.setdefault(str(message.chat.id), {"currencies": []})
    currencies= wallet["currencies"]
    bot.send_message(message.chat.id, "Ваші валюти:")
    for i in currencies:
        bot.send_message(message.chat.id, i)

user={}

@bot.message_handler(commands=['convert'])
def start_conversion(message):
    user[message.chat.id] = "activ"
    bot.send_message(message.chat.id, "Щоб конвертувати валюту вам потрібно ввести:\n Валюта Сума Валюта\nНаприклад: USD 1000 UAH")



@bot.message_handler(func=lambda message: user.get(message.chat.id) == "activ")
def convert(message):
    wallet = wallets.setdefault(str(message.chat.id), {"balances": {}})
    user_id = message.chat.id
    try:
        currency_1, amount, currency_2 = message.text.strip().split(" ")
        if currency_1 in currency_list and currency_2 in currency_list:
            if currency_1 in wallet["balances"] and currency_2 in wallet["balances"]:
                if float(amount) > 0:
                    if wallet["balances"][currency_1] >= float(amount):
                        amount = float(amount)
                        user[user_id] = None
                        conversion = convert_dict[currency_1][currency_2]
                        converted_amount = amount * conversion
                        wallet["balances"][currency_1] -= amount
                        wallet["balances"][currency_2] = wallet["balances"].get(currency_2, 0) + converted_amount
                        bot.send_message(message.chat.id, f"Ви конвертували {amount} {currency_1} в {converted_amount} {currency_2}")
                        dump_bot(message)
                    else:
                        bot.send_message(message.chat.id, f"Баланс валюти {currency_1} меньший ніж ви хочете конвертувати."
                                                          f"Щоб переглянути ваш баланс виконайте команду /balance")
                else:
                    bot.send_message(message.chat.id, "Введіть суму більшу за нуль")
            else:
                bot.send_message(message.chat.id, f"Валюти {currency_1} або {currency_2} не має в вашому гаманці."
                                                  f"Виконайте команду /add щоб додати валюту")
        else:
            bot.send_message(message.chat.id, "Помилка.Неправильна валюта")

    except Exception:
        bot.send_message(message.chat.id, "Помилка")

@bot.message_handler(commands=['delete'])
def delete(message):
    user_1[message.chat.id] = "active"
    bot.send_message(message.chat.id, "Щоб видалити гаманець напишіть валюту:")

user_1={}
@bot.message_handler(func=lambda message: user_1.get(message.chat.id) == "active")
def deleter(message):
    text= message.text
    wallet = wallets.setdefault(str(message.chat.id), {"balances": {}, "currencies": []})
    try:
        if text in currency_list:
            if text in wallet["balances"]:
                del wallet["balances"][text]
                wallet["currencies"].remove(text)
                bot.send_message(message.chat.id,f"Гаманець для валюти {text} видалено.")
                dump_bot(message)
            else:
                bot.send_message(message.chat.id, f"У вас ще немає гаманця з валютою {text}.\n"
                                                  f"Виконайте команду /add щоб додати гаманець\n")
        else:
            bot.send_message(message.chat.id, f"Спробуйте ввести {currency_list}")
    except Exception:
        bot.send_message(message.chat.id, "Помилка")



user_state = {}

if __name__ == "__main__":

    convert_dict = {
        "UAH": {
            "USD": 0.024,
            "EUR": 0.023
        },
        "EUR": {
            "USD": 1.05,
            "UAH": 43.5,
        },
        "USD": {
            "UAH": 41,
            "EUR": 0.95,
        }
    }
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []



    wallets = {}
    with open("wallets.json", "r", encoding='utf-8') as wallet_json:
        wallets = json.load(wallet_json)
    bot.polling()