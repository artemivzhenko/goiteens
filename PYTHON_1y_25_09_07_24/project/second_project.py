import telebot
from telebot.types import ReplyKeyboardMarkup
import json


API_token = ''
bot = telebot.TeleBot(API_token, parse_mode=None)
currency_list = ["USD", "EUR", "UAH"]
stages = {

}


@bot.message_handler(commands=['add_wallet'])
def add_wallet(message):
    wallet = wallets[str(message.chat.id)]
    user_currencies = wallet["currencies"]
    buttons = []
    for currency in currency_list:
        if currency not in user_currencies:
            buttons.append(currency)
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.keyboard = [buttons]
    bot.send_message(message.chat.id, "Виберіть гаманець який хочете додати ->", reply_markup=menu)


@bot.message_handler(func=lambda message: message.text in currency_list)
def set_new_wallet(message):
    wallet_id = str(message.chat.id)
    wallet = wallets[wallet_id]
    match stages[wallet_id]:
        case 0:
            if message.text not in wallet["currencies"]:
                wallets[str(message.chat.id)]["currencies"].append(message.text)
                wallets[str(message.chat.id)]["balances"][message.text] = 0.0
                bot.send_message(message.chat.id, f"Ви додали новий гаманець із валютою {message.text}")
                return
            bot.send_message(message.chat.id, f"У вас вже є гаманець із валютою {message.text}")
        case 1:
            if message.text not in wallet["currencies"]:
                bot.send_message(message.chat.id, f"Ви не можете додати цю валюту бо не маєте цього гаманця")



@bot.message_handler(commands=['dump'])
def dump_bot(message):
    with open("wallets.json", "w", encoding='utf-8') as wallet_json:
        json.dump(wallets, wallet_json, ensure_ascii=False, indent=4)
    bot.send_message(message.chat.id, "Бот вивантажив інформацію про гаманці")


@bot.message_handler(commands=['balance'])
def balance_bot(message):
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
і конвертувати суми між ними за заданими курсами.ʼ
"""
    bot.send_message(message.chat.id, start_message, reply_markup=menu)
    wallet_id = str(message.chat.id)
    stages[wallet_id] = 0
    user = message.from_user.full_name
    if wallet_id not in wallets.keys():
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


@bot.message_handler(func=lambda message: message.text == "Поповнити рахунок")
def add_money(message):
    stages[str(message.chat.id)] = 1


@bot.message_handler(func=lambda message: message.text.endwith(" USD"))
def echo_all(message):
    text = message.text
    if "to" in text:
        try:
            currencies = text.split(" ")[::2]
            currency_value = convert_dict[currencies[0]][currencies[1]]
            bot.send_message(message.chat.id, f"Ваш курс = {currencies[0]} -> {currencies[1]} = {currency_value}", reply_markup=menu)
        except Exception:
            bot.send_message(message.chat.id, "Помилка отримання курсу валюти. Неккоректне повідомлення", reply_markup=menu)
    elif "-" in text:
        try:
            number, currency = text.split(" ")
            currency_1, currency_2 = currency.split("-")
            convert_number = float(number) * convert_dict[currency_1][currency_2]
            current_currency = currency.split("-")[1]
            bot.reply_to(message, f"Результат\n{convert_number}{current_currency}")
            bot.send_message(message.chat.id, "Виберіть курс валюти із меню", reply_markup=menu)
        except Exception:
            bot.send_message(message.chat.id, "Помилка конвертації. Неккоректне повідомлення", reply_markup=menu)
    else:
        bot.send_message(message.chat.id, "Неккоректне повідомлення", reply_markup=menu)


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
    for key, value in convert_dict.items():
        button_list = []
        for currency, v in value.items():
            button_text = f"{key} to {currency}"
            button_list.append(button_text)
        buttons.append(button_list)
    menu.keyboard = buttons
    wallets = {}
    with open("wallets.json", "r", encoding='utf-8') as wallet_json:
        wallets = json.load(wallet_json)
    bot.polling()

