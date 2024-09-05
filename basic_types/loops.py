first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for first_number in range(1, 4):
#     print(f"Таблиця множення для {first_number}")
#     for second_number in range(1, 4):
#         result = first_number * second_number
#         message = f"{first_number} * {second_number} = {result}"
#         print(message)


# my_list = list(range(7, 20))
# print(my_list)

# input_value = int(input("Введіть число->\n"))
# while input_value > 1:
#     print(list(range(1, input_value)))
#     input_value -= 1


input_value = int(input("Введіть число->\n"))

length = (input_value // 2) + 1
print(length)

for i in range(1, length+1):
    print((" " * i) + "*" * i)


print(range())