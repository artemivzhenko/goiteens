number1 = int(input("Введіть число 1: "))
number2 = int(input("Введіть число 2: "))
number3 = int(input("Введіть число 3: "))

def number_analyze(number):
    if number % 2 == 0:
        print("Число парне")
    elif number ** 2 > 100:
        print("Число у квадраті більше 100")
    else:
        print("Я не знаю що це за число")

number_analyze(number1)
number_analyze(number2)
number_analyze(number3)