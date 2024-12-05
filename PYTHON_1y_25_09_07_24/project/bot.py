import telebot
from telebot.types import ReplyKeyboardMarkup
import json


API_token = ''
bot = telebot.TeleBot(API_token, parse_mode=None)

currency_list = ["USD", "EUR", "UAH"]

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
stages = {

}

wallets = {}


@bot.message_handler(commands=['dump'])
def dump_bot(message):
    with open("wallets.json", "w", encoding='utf-8') as wallet_json:
        json.dump(wallets, wallet_json, ensure_ascii=False, indent=4)
    bot.send_message(message.chat.id, "Бот вивантажив інформацію про гаманці")


@bot.message_handler(commands=['balance'])
def balance_bot(message):
    wallet = wallets[str(message.chat.id)]
    if wallet["balances"] == {}:
        bot.send_message(message.chat.id, "У вас ще немає балансів у гаманці \n Щоб додати гаманець, введіть /add_wallet")
    else:
        for currency, value in wallet["balances"].items():
            bot.send_message(message.chat.id, f"Гаманець {currency} із рахунком {value}")


@bot.message_handler(commands=['help'])
def help(message):
    Help = """/help - допомога \n
    /balance - Вивести всі гаманці і гроші на них \n
    /add_wallet - Зробити гаманець \n
    /dump - Зберегти зміни в гаманцях \n
    Щоб конвертувати валюту треба писати по формі \n
    <сума> <валюта_1> <валюта_2> convert"""
    bot.send_message(message.chat.id, f"{Help}")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    start_message = """Вашій увазі представлено 
Бот для конвертера валют,
який дозволяє користувачам управляти
віртуальними гаманцями з різними валютами
і конвертувати суми між ними за заданими курсами.ʼ
"""
    bot.send_message(message.chat.id, start_message, reply_markup=menu)
    wallet_id = str(message.chat.id)
    stages[wallet_id] = {
        "current_stage": 0,
        "current_wallet": None
    }
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
    dump_bot(message)


@bot.message_handler(commands=['add_wallet'])
def choose_wallet_bot(message):
    menu = []
    wallet_id = str(message.chat.id)
    wallet = wallets[wallet_id]['currencies']
    stages[wallet_id] = {
        "current_stage": 0,
        "current_wallet": None
    }
    for i in currency_list:
        if i not in wallet:
            menu.append(i)
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons.keyboard = [menu]
    if menu != []:
        bot.send_message(message.chat.id, "Виберіть один із гаманців:", reply_markup=buttons)
    elif menu == []:
        bot.send_message(message.chat.id, "Ви вже створили максимум гаманців")


@bot.message_handler(func=lambda message: message.text in currency_list)
def make_wallet_bot(message):
    global wallets
    wallet_id = str(message.chat.id)
    match stages[wallet_id]["current_stage"]:
        case 0:
            if (message.text not in wallets[wallet_id]['currencies']) or message.text not in ("USD", "UAH", "EUR"):
                wallets[wallet_id]['currencies'].append(message.text)
                wallets[wallet_id]['balances'][message.text] = 0
                print(wallets[wallet_id]['balances'][message.text])
                stages[wallet_id] = {
                    "current_stage": 1,
                    "current_wallet": message.text
                }
                bot.send_message(message.chat.id, f"Ви вибрали: {message.text}")
                bot.send_message(message.chat.id, f"Тепер введіть кількість {message.text} і в кінці допишіть {message.text}")
                dump_bot(message)
            else:
                bot.send_message(message.chat.id, f"У вас вже є цей гаманець")
        case 1:
            if (message.text not in wallets[str(message.chat.id)]['currencies']) == ("USD" or "UAH" or "EUR"):
                bot.send_message(message.chat.id, f"У вас немає такого гаманця {message.text}")
                return
            stages[wallet_id] = {
                "current_stage": 1,
                "current_wallet": message.text
            }
            bot.send_message(message.chat.id, f"Введіть суму для поповнення")


@bot.message_handler(func=lambda message: message.text.endswith("convert"))
def convert(message):
    text = message.text.strip()
    try:
        # Розділяємо текст на компоненти
        parts = text.split(" ")
        if len(parts) != 4 or parts[3] != "convert":
            bot.send_message(message.chat.id, "Неправильний формат. Використовуйте: <сума> <валюта_1> <валюта_2> convert.")
            return

        # Отримуємо дані
        amount_1 = float(parts[0])  # Сума для конвертації
        curr_1 = parts[1].strip().upper()  # Валюта для зняття
        curr_2 = parts[2].strip().upper()  # Валюта для поповнення

        # Перевірка наявності гаманця
        user_wallet = wallets.get(str(message.chat.id))
        if not user_wallet:
            bot.send_message(message.chat.id, "Ваш гаманець не знайдено.")
            return

        # Перевірка наявності достатнього балансу
        if curr_1 not in user_wallet['balances'] or float(user_wallet['balances'][curr_1]) < amount_1:
            bot.send_message(message.chat.id, f"Недостатньо коштів на рахунку {curr_1}.")
            return

        # Перевірка наявності курсу обміну
        if curr_2 not in convert_dict[curr_1]:
            bot.send_message(message.chat.id, f"Конвертація з {curr_1} у {curr_2} недоступна.")
            return

        # Отримуємо курс обміну
        conversion_rate = convert_dict[curr_1][curr_2]
        converted_amount = amount_1 * conversion_rate

        # Оновлюємо баланси
        user_wallet['balances'][curr_1] = str(float(user_wallet['balances'][curr_1]) - amount_1)
        user_wallet['balances'][curr_2] = str(float(user_wallet['balances'][curr_2]) + converted_amount)

        # Виводимо результат
        bot.send_message(
            message.chat.id,
            f"Ви перевели {amount_1:.2f} {curr_1} в {curr_2}.\n"
            f"Ваш поточний баланс в {curr_1}: {user_wallet['balances'][curr_1]} {curr_1}\n"
            f"Ваш поточний баланс в {curr_2}: {user_wallet['balances'][curr_2]} {curr_2}"
        )
    except Exception as e:
        bot.send_message(message.chat.id, f"Сталася помилка: {e}")


@bot.message_handler(func=lambda message: message.text.isdigit())
def update_wallet(message):
    wallet_id = str(message.chat.id)
    summary = float(message.text)
    if summary > 0 and summary <= 10000000:
        wallets[wallet_id]["balances"][stages[wallet_id]["current_wallet"]] += summary
        bot.send_message(message.chat.id, f"Ви поповнили гаманець {stages[wallet_id]['current_wallet']} на суму {summary}", reply_markup=menu)
        return
    bot.send_message(message.chat.id, f"Ви не можете поповнили гаманець {stages[wallet_id]['current_wallet']} на суму {summary}", reply_markup=menu)
    dump_bot(message)


@bot.message_handler(func=lambda message: True)
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
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    with open("wallets.json", "r", encoding='utf-8') as wallet_json:
        wallets = json.load(wallet_json)
    bot.polling()
