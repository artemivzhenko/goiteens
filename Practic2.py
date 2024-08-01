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



def HomeWork():
    print("*****")
    print("****")
    print("***")
    print("**")
    print("*")

HomeWork()



