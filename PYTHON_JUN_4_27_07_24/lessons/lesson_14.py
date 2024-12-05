# user_input = int(input("Введіть число ->"))
#
#
# if user_input % 2 == 0 and user_input > 0:
#     print("Ви ввели число кратне 2")
# elif user_input % 5 == 0:
#     print(f"Число {user_input} кратне 5")
# else:
#     print(f"Число {user_input} не кратне 2 і не кратне 5")
#
user_input = int(input("Введіть опцію ->"))
match user_input:
    case 1:
        print("Ви вибрали опцію 1")
    case 2:
        print("Ви вибрали опцію 2")
    case 3:
        print("Ви вибрали опцію 3")
    case 4:
        print("Ви вибрали опцію 4")
    case _:
        print("Ви вибрали опцію за замовчуванням")


#
# user_input = int(input("Введіть число ->"))
#
# result = user_input ** 2 if user_input % 2 == 0 else user_input - 10
# print(result)
#

my_list = [78, 79, 80, 81, 82, 83, 84, 85, 86, 87]  # ітеруємий обʼєкт

x = 10

while x < 999:
    print(x < 999)
    print(f"x = {x}")
    x += 100
print(f"Out of while= {x < 999}")

for number in my_list:
    print(f"number + 8 = {number + 8}")


my_double_list = [number * 2 for number in my_list]
print(my_double_list)



