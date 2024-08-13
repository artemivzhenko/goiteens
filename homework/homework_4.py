# Функція повинна приймати три аргументи: операція (строка/символ), значення1 (число), значення2 (число).
# Функція повинна повертати результат чисел після застосування обраної операції.
#
# Приклади (Оператор, значення1, значення2) –> результат
# +,4,7 –> 11
# -,15,18) –> -3
# *,5,5) –> 25
# /,49,7) –> 7


user_input = input("Put your string")
user_input_list = user_input.split(",")


operation = user_input_list[0]
number_1 = int(user_input_list[1])
number_2 = int(user_input_list[2])

print(user_input_list)
if operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
elif operation == "*":
    print(number_1 * number_2)
elif operation == "/":
    print(number_1 / number_2)
else:
    print("Incorrect operation")


match operation:
    case "+":
        print(number_1 + number_2)
    case "-":
        print(number_1 - number_2)
    case "/":
        print(number_1 / number_2)
    case "*":
        print(number_1 * number_2)
    case _:
        print("Incorrect operation")
