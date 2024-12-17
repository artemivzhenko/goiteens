import random
secret_number = random.randint(1, 100)
guess = None
while guess != secret_number:
    guess = int(input("Вгадайте число від 1 до 100: "))
    if guess < secret_number:
        print("Занадто мале")
    elif guess > secret_number:
        print("Занадто велике")
    else:
        print("Вітаємо! Ви вгадали число!")


year = int(input("Введіть рік: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} є високосним роком.")
else:
    print(f"{year} не є високосним роком.")


for i in range(1, 21):
    for j in range(1, 21):
        print(f"{i * j:4}", end="")
    print()


number = int(input("Введіть число: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(f"{number} не є простим числом")
            break
    else:
        print(f"{number} є простим числом")
else:
    print(f"{number} не є простим числом")


even_numbers = list(range(2, 101, 2))
print(even_numbers)