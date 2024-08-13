#Напишіть функцію, яка приймає ціле число n та рядок s як параметри і повертає рядок s , повторений рівно n разів.

user_input = input("Put your string").split(",")

print(user_input)
number = int(user_input[0])
user_string = user_input[1]
print(number*user_string)