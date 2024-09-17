import random

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Компьютер загадал число от 1 до 100. Попробуй угадать его!")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Введите ваше предположение (или 'выход' для завершения игры): ")

        if guess.lower() == 'выход':
            print("Спасибо за игру! До новых встреч!")
            break

        if not guess.isdigit():
            print("Пожалуйста, введите число!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Загаданное число больше!")
        elif guess > number:
            print("Загаданное число меньше!")
        else:
            print(f"Поздравляем! Вы угадали число {number} за {attempts} попыток!")
            break
