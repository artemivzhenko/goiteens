# STRING

summary: str = "Hello " + "World"
print(summary)
summary += "!!!!!!!!"
print(summary)


multiple = "Multiple " * 5
print(multiple)
multiple *= 2
print(multiple)

summary: str = summary.replace("Hello", "Goodbye")
print(summary)


print(summary.islower())
print(summary.isupper())


upper_s = summary.upper()
print(upper_s)
print(upper_s.isupper())
lower_s = summary.lower()
print(lower_s)
print(lower_s.islower())

capitalized = lower_s.capitalize()
print(capitalized)

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

