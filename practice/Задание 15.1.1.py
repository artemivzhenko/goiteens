
temperatures_celsius = list(map(int, input("Введите температуры в градусах Цельсия через пробел: ").split()))
temperatures_fahrenheit = list(map(lambda c: c * 9/5 + 32, temperatures_celsius))
print("Температуры в Фаренгейтах:", temperatures_fahrenheit)
