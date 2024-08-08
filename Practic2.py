##13. Напишіть програму,
##яка просить користувача ввести місто, у якому він живе.
##Виведіть назву міста разом із фразою «is a wonderful place!».
##Наприклад: Kyiv is a wonderful place!

##14. Напишіть програму, яка запитує у користувача ( якщо має домашню тварину ) —
##спочатку назву тварини, а потім її ім’я. Вивести повідомлення у форматі:
##“My … is a beautiful animal. Its name is … .” (Вписати назву тварини та ім’я). Наприклад:
##My cat is a beautiful animal. Its name is Barsik.


def Ex13():
    user_live = input("Введіть де ви живете -->\n")
    print(user_live + " is a wonderful place!")



def Ex14():
    user_animal = input("Введіть назву вашої тваринки -->\n")

    user_animal_name = input("Введіть ім'я тваринки -->\n")

    print("My " + user_animal + " is a beautiful animal." + " Its name is " + user_animal_name + ".")


# Написати программу яка запитує у ко
# ристувача число і якщо це число меньше 100 то просить ввести його ще раз

def Practic():
    while True:
        number = int(input("Введіть число: \n"))
        if number >= 100:
            break
        else:
            print("Ви ввели число " + number)


#Завершіть функцію, яка повертає день тижня відповідно до вхідного номера:

#1 повертає “Неділя”
#2 повертає “Понеділок”
#3 повертає “Вівторок”
#4 повертає “Середа”
#5 повертає “Четвер”
#6 повертає “П’ятниця”
#7 повертає “Субота”
#Інакше повертає “Неправильно, будь ласка, введіть число від 1 до 7”.

def Practic2():
    number = 0;
    list_week = ["Неділя", "Понеділок", "Вівторок", "Середа", "Четвер", "П’ятниця", "Субота"]
    while number <= 5:
     user_get = int(input("Введіть число:\n"))
     if user_get <= 7:
        print(list_week[user_get] - 1)
     else:
        print("Інакше повертає “Неправильно, будь ласка, введіть число від 1 до 7")


#Функція повинна приймати три аргументи: операція (строка/символ), значення1 (число), значення2 (число).
#Функція повинна повертати результат чисел після застосування обраної операції.

#Приклади (Оператор, значення1, значення2) –> результат
#(’+’, 4, 7) –> 11
#(’-’, 15, 18) –> -3
#(’*’, 5, 5) –> 25
#(’/’, 49, 7) –> 7


def Practic3():
    user_number1 = int(input("Введіть 1 число -->\n"))
    user_operation = input("Введіть тип операції (+,-,*,/) -->\n")
    user_number2 = int(input("Введіть 2 число -->\n"))
    if user_operation == '+':
        print("Число: " + str(user_number1 + user_number2))
    elif user_operation == '-':
        print("Число: " + str(user_number1 - user_number2))
    elif user_operation == '*':
        print("Число: " + str(user_number1 * user_number2))
    elif user_operation == '/':
        print("Число: " + str(user_number1 / user_number2))
    else:
        print("такої операції не існує")

def HomeWork():
    print("*****")
    print("****")
    print("***")
    print("**")
    print("*")




