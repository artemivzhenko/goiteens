wallets = {}

exchange_rates = {
    ("CRD", "GLM"): 0.5,
    ("CRD", "TRX"): 1.5,
    ("GLM", "CRD"): 2.0,
    ("GLM", "TRX"): 3.0,
    ("TRX", "CRD"): 0.67,
    ("TRX", "GLM"): 0.33,
}

valid_currencies = ["CRD", "GLM", "TRX"]

log = []


def create_wallet():
    name = input("Название кошелька: ").strip()
    if name in wallets:
        print("Ошибка: Такой кошелек уже есть.")
        return
    currency = input("Валюта кошелька (например, CRD): ").upper()
    if currency not in valid_currencies:
        print("Ошибка: Такой валюты нет.")
        return
    try:
        balance = float(input("Начальный баланс: "))
        if balance < 0:
            print("Ошибка: Баланс не может быть отрицательным.")
            return
        wallets[name] = {"currency": currency, "balance": balance}
        log.append(f"Создан кошелек {name}: {currency}, баланс {balance}")
        print(f"Кошелек {name} создан.")
    except ValueError:
        print("Ошибка: Введите число для баланса.")


def convert_currency():
    from_wallet = input("Из какого кошелька переводить: ").strip()
    to_wallet = input("В какой кошелек переводить: ").strip()
    if from_wallet not in wallets or to_wallet not in wallets:
        print("Ошибка: Кошелек не найден.")
        return
    try:
        amount = float(input("Сумма перевода: "))
        if amount < 0:
            print("Ошибка: Сумма не может быть отрицательной.")
            return
        if wallets[from_wallet]["balance"] < amount:
            print("Ошибка: Недостаточно денег.")
            return
        from_currency = wallets[from_wallet]["currency"]
        to_currency = wallets[to_wallet]["currency"]
        if (from_currency, to_currency) not in exchange_rates:
            print("Ошибка: Нет курса обмена между этими валютами.")
            return
        rate = exchange_rates[(from_currency, to_currency)]
        converted = amount * rate
        wallets[from_wallet]["balance"] -= amount
        wallets[to_wallet]["balance"] += converted
        log.append(
            f"Переведено {amount} {from_currency} из {from_wallet} в {converted:.2f} {to_currency} ({to_wallet})")
        print(f"Успех! {amount} {from_currency} -> {converted:.2f} {to_currency}")
    except ValueError:
        print("Ошибка: Введите число для суммы.")


def show_wallets():
    for name, data in wallets.items():
        print(f"{name}: {data['currency']}, баланс: {data['balance']:.2f}")
    log.append("Просмотрены кошельки.")


def show_exchange_rates():
    for (from_currency, to_currency), rate in exchange_rates.items():
        print(f"1 {from_currency} -> {rate} {to_currency}")


def show_log():
    print("История операций:")
    for record in log:
        print(record)

def show_credits():
    print("\nСпасибо за использование конвертера валют!")
    print("Создатели:")
    print("Директор: Ст. научный сотрудник")
    print("---------------------------------")
    print("Программист: Ст. научный сотрудник")
    print("---------------------------------")
    print("Помощь с кодом: Иконы")
    print("Помощь с кодом: Чай")
    print("---------------------------------")
    print("Помощь с валютами: ChatGPT-4o")
    print("---------------------------------")
    print("Тестеровщики: cw_tab_tab ")
    print("---------------------------------")
    print("СПАСИБО ВСЕМ!(хватит мне писать!)")
def reset_wallets():
    choice = input("Введите '0', чтобы обнулить баланс, или 'удалить', чтобы удалить все кошельки: ").strip().lower()
    if choice == "0":
        for wallet in wallets.values():
            wallet["balance"] = 0
        log.append("Все балансы обнулены.")
        print("Все балансы обнулены.")
    elif choice == "удалить":
        wallets.clear()
        log.append("Все кошельки удалены.")
        print("Все кошельки удалены.")
    else:
        print("Действие отменено.")


def main_menu():
    while True:
        print("\nМеню:")
        print("1. Создать кошелек")
        print("2. Перевести валюту")
        print("3. Показать кошельки")
        print("4. Показать курсы валют")
        print("5. Показать историю")
        print("6. Сбросить кошельки")
        print("7. Выйти (Титры)")
        choice = input("Ваш выбор: ")
        if choice == "1":
            create_wallet()
        elif choice == "2":
            convert_currency()
        elif choice == "3":
            show_wallets()
        elif choice == "4":
            show_exchange_rates()
        elif choice == "5":
            show_log()
        elif choice == "6":
            reset_wallets()
        elif choice == "7":
            show_credits()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()