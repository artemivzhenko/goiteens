numbers = list(map(int, input("Введите числа через пробел: ").split()))
squared_numbers = list(map(lambda x: x ** 2, numbers))
even_squared_numbers = list(filter(lambda x: x % 2 == 0, squared_numbers))

print("Числа, возведённые в квадрат:", squared_numbers)
print("Чётные числа, возведённые в квадрат:", even_squared_numbers)
