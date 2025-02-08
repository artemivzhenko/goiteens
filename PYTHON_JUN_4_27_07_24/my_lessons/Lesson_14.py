import random


random_number = random.randint(1, 50)

print("Я задумав число від 1 до 50. Спробуй його вгадати!")

while True:
    user_input = int(input("Введи своє припущення:\n"))


    if user_input < random_number:
        print("Занадто мале!")
    elif user_input > random_number:
        print("Занадто велике!")
    else:
        print("Прям в яблочко!!! Молодець!!!")
        break
