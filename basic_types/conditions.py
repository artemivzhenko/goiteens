
number = 10

if 10 <= number <= 20 or (number > 30 and number % 2 == 0):
    print("число в діапазоні від 10 до 20 або Число більше 30 і парне")
else:
    print("Умова не виконана")



#
# print(number > 10)
# print(number == 10)
# print(number >= 10)
#

long_condition: bool = (number > 10 or number == 10) == (number >= 10)
short_condition: bool = number >= 10


print(long_condition == short_condition)


# greater_than_10 = number >= 10
# print(greater_than_10)
#
# if number >= 10:
#     print("Число більше або дорівнює 10")

number_x = 44
number_y = 67

print(number_x > number_y)          # X більше У = False
print(number_x < number_y)          # X меньше У = True
print(number_x >= number_y)         # X більше або дорівнює У = False
print(number_x <= number_y)         # X меньше або дорівнює У = True
print(number_x == number_y)         # Х дорівнює У    = False
print(number_x != number_y)         # X не дорівнює У = True
print(not (number_x == number_y))   # NOT (Х дорівнює У) = True

number = int(input("Put your number"))
result = "Число кратне 5 та більше 100" if number % 5 == 0 and number > 100 else "Число не кратне 5 та менше 100"


if (number := int(input("Put your number"))) % 5 == 0:
    print(number * 8)
    print("Число кратне 5")
else:
    print("Число не кратне 5")

