user_wallet = {
    "balances": {
    },
    "currencies": []
}
while True:
    message = """
Виберіть дію
    1.Додати гаманець
    2.Поповнити гаманець
    3.Обміняти валюту
    4.Вихід
->"""
    choise = int(input(message))
    match choise:
        case 1:
            currencies_message = """Виберіть валюту
    1.USD
    2.EUR
    3.UAH
    4.USD
"""
            new_currency = int(input(currencies_message))
        case 2:
            pass
        case 3:
            pass
        case 4:
            exit()
        case _:
            print("Такого значення не існує")
