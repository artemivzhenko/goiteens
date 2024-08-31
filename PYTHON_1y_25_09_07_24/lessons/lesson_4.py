user_input = input("Put your string")

message = "Строка має більше 10 символів" if len(user_input) > 10 else "Строка має меньше 10 символів або кількість символів = 10"

#
# if len(user_input) > 10:
#     message = "Строка має більше 10 символів"
# else:
#     message = "Строка має меньше 10 символів"

print(message)

user_value = int(input("Put your number\n"))

value = user_value ** 2 if user_value < 100 else user_value / 2

