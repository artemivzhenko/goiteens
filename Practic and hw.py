#Практика (Оператор, значення, значення2) = результат
#[ADD] HW


def Ratka():
user_input = input("Put your string")
user_input_list = user_input.split(",")
operation = int(user_input_list[0])
number_1 = int(user_input_list[1])
number_2 = int(user_input_list[2])



print(user_input_list)
if operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
if operation == "*":
    print(number_1 * number_2)
elif operation == "/":
    print(number_1 / number_2)
else:
    print("Incorrect operation")

#PATATATATTATATATATATTATATTATAAA!!!!!!!!!!!
Ratka()
