while True:
    number = int(input("Введіть число -> \n "))

    if number > 100:
        print("Завершено")


    result = number * 4
    print(f"{number} * 4 = {result}")