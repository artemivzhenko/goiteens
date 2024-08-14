cap = (input("Please put cap\n"))
on = int(input("Please put on\n"))
wait = int(input("Please put wait\n"))

free_place = cap - on
all_places = wait - free_places

if all_places > 0:
    print(f"Автобус не може вмістити ще {all_places} людей")
else:
    print("Всі пасажири влізли")




user_input = input("Put your string")

if len(user_input) > 10:
    print("Сторона має більше 10 символів")
else:
    print("Сторона має меньше 10 символів")




message_input("Put your string")

message = "Строка має більше 10 символів" if len(user_input) > 10 else "Строка має меньше 10 символів або кількість символів = ..."

#
# if len(user_input) > 10:
#   message = "Строка має більше 10 символів"
#else:
#   message = "Строка має меньше 10 символів"


print(message)

user_value =int(input("Put your number\n"))

value = user_value ** 2 if user_value < 100 else user_value / 2



#ЗАРАЗ БУДУТЬ ЗАВДАННЯ ВІН ВЧИТЕЛЯ. ПРАКТИКА!!


user_value =int(input("Put your number\n"))
value = user_value ** 2 if user_value < 100 else user_value / 2
user_value = int(input("Please put number\n"))
print(value)
X = input("Please put x\n")
x = int(x)
y = input("Please puty\n")
y = int(y)
message = if x > y else "y > x"
print(message)


user_value= int(input("Plrase put your number\n"))
if user_value > = 0:
    print(user_value+1)
else:
    print(user_value-2)


user_value =input("[lease put your number\n")
message = "Число парне" if int(user_value)x 2==0 else "Число не парне"
value_len = user_value