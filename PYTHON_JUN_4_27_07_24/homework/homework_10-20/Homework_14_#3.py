numbers = input("Напишіть числа з пробілами:")
numbers_2 = list(map(int,numbers.split()))
print("Початковий",numbers_2)

numbers_2.reverse()
print("Кінцевий",numbers_2)
