while True:
    number = int(input("Введіть число: "))
    if number >= 100:
        print("Ви ввели число:", number)
        break
    else:
        print("Число менше 100. Будь ласка, спробуйте ще раз.")