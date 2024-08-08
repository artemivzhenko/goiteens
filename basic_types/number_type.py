# INTEGER, FLOAT

x: float = 13.56
y: float = -5.1

print("X * Y = " + str(x * y))
print("X + Y = " + str(x + y))
print("X - Y = " + str(x - y))
print("X / Y = " + str(x / y))
print("X ** Y = " + str(x ** -y))
print("X // Y = " + str(x // y))
print("X % Y = " + str(x % y))
str_x: str = str(x)
str_y: str = str(y)

x_int: int = int(float(str_x))
y_int: int = int(float(str_y))
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
