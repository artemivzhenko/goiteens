import random

secret_number = random.randint(1, 100)

print("Вгадай число від 1 до 100")
while True:
    guess = int(input("Введіть ваше число: "))
    if guess < secret_number:
        print("Ваше число занадто мале.")
    elif guess > secret_number:
        print("Ваше число занадто велике.")
    else:
        print("Вітаємо! Ви вгадали число.")
    break