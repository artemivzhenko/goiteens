def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка! Нельзя делить на ноль."
    return x / y

def calculator():
    print("Выберете операцию:")
    print("1.Прибавление (+)")
    print("2.Отнимание (-)")
    print("3.Умножение (*)")
    print("4.Деление (/)")

    while True:
        choice = input("Введите номер (1/2/3/4): ")

        if choice in ('1', '2', '3', '4','+','-','*','/'):
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка, попробуйте заново.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif choice == '/':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            next_calculator_operacion = input("Хотите выполнить еще один расчет? (да/нет): ")
            if  next_calculator_operacion.lower() != 'да':
                break
        else:
            print("Ошибка, пробуйте заново.")

    else: __name__ == "____"
calculator()

# Функція повинна приймати три аргументи: операція (строка/символ), значення1 (число), значення2 (число).
# Функція повинна повертати результат чисел після застосування обраної операції.