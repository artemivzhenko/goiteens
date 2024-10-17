#Оголосити змінні х та у (числа).
# За допомогою умовного оператора перевірити яке число більше.

def Prac1():
    x = 10
    y = 20

    result = f"{x} більше за {y}" if x > y  else f"{y} більше за {x}"

    print(result)

def Prac2():
    number = 5

    result = number + 1 if number > 0 else number - 2

    print(result)


def Prac3():
    user_input = int(input("Введіть число від 1 до 999 -->\n"))

    if 1 <= user_input <= 999:
        user_input_lang = len(str(user_input))

        if user_input % 2 == 0:
            parity = "парне"
        else:
            parity = "непарне"

        if user_input_lang == 1:
            print(f"{parity} однозначне число")
        elif user_input_lang == 2:
            print("{parity} двозначне число")
        elif user_input_lang == 3:
            print(f"{parity} тризначне число")

    else:
        print("Число повинно бути від 1 до 999")

#Написати програму, яка приймає на вхід:
#прізвище студента (рядок)
#кількість балів (ціле число).
#Якщо кількість балів студента більше 80, то вивести повідомлення, що студент «Прізвище» здав іспит.

#В протилежному випадку написати, що іспит не складено.

def Prac4():
    user_last_name = input("Введіть своє прізвище -->\n")
    user_score = int(input("Введіть вашу кількість балів -->\n"))

    result = f"Студент {user_last_name} здав іспит" if user_score >= 80 else user_last_name + " не здав іспит"
    print(result)


Prac4()