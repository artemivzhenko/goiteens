year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    day = 366
else:
    day = 365

print("Количество дней в году:", day)
