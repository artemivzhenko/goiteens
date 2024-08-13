# INTEGER, FLOAT

x: int = 14
y: int = -5

print("X * Y = " + str(x * y))  # Множення
print("X + Y = " + str(x + y))  # Додавання
print("X - Y = " + str(x - y))  # Віднімання
print("X / Y = " + str(x / y))  # Ділення
print("X ** Y = " + str(x ** -y))  # Взведення у степінь
print("X // Y = " + str(x // y))  # Ділення без остачі
print("X % Y = " + str(x % y))  # Отримання остачі від ділення
str_x: str = str(x)  # Перетвоерння числа у текст
str_y: str = str(y)  # Перетвоерння числа у текст

x_int: int = int(float(str_x))  # Перетвоерння тексту у число
y_int: int = int(float(str_y))  # Перетвоерння тексту у число
print(x_int)
print(y_int)


if 5 > 3:
    print("5 is greater than 3")
    print("Hello")
    print("World")
elif 8 < 4:
    print("8 is greater than 4")


if 6 > 4:
    print("5 is greater than 4")
    print("We call this function from elif block")
else:
    print("We call this function from else block")
