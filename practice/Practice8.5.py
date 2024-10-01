first_number = int(input("Введіть початок діапазону -> \n "))
second_number = int(input("Введіть кінець діапазону -> \n "))

sum = 0

for i in range(first_number, second_number + 1):
    sum += i

print(f"Сума всіх чисел в діапазоні від {first_number} до {second_number} дорівнює {sum}")