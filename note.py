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


if 5 > 3:
    print("5 is greater than 3")
    print("Hello")
    print("World")


if 6 > 4:
    print("5 is greater than 4")
    print("We call this function from elif block")
else:
    print("We call this function from else block")


# BOOLEAN

first_boolean: bool = True
second_boolean: bool = False
third_boolean: bool = False


print("A and B =", first_boolean and second_boolean)                   # Logical AND
print("A or B =", first_boolean or second_boolean or third_boolean)    # Logical OR
print("Not A =", not second_boolean)                                   # Logical NOT

result = (first_boolean or second_boolean) and not (first_boolean and second_boolean)
print("Result of (A or B) and not (A and B) =", result)

a_int: int = int(first_boolean)
b_int: int = int(second_boolean)
print("Integer value of A:", a_int)
print("Integer value of B:", b_int)

is_greater: bool = 5 > 3
print("Is 5 greater than 3?", is_greater)

is_equal: bool = (3 + 4) == 7
print("Is 3 + 4 equal to 7?", is_equal)

a = not first_boolean
b = not second_boolean
print("New value of A (after negation):", a)
print("New value of B (after negation):", b)


practice_boolean: bool = 5 * 10 == 74
print(practice_boolean)
practice_boolean_2: bool = "Pavlo" != "Ivan"
print(practice_boolean_2)
practice_boolean_3: bool = "Andrii" == "Petro"
print(practice_boolean_3)
