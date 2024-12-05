# for number in range(1, 10 + 1):   # range(1, 10 + 1) ітераційний обʼєкт
#     print(number)                 # одна дія циклу - ітерація
#
#
# user_input = int(input("Введіть число -> \n"))
# while user_input < 10000:
#     print(user_input)
#     user_input = user_input * 2
# import turtle

#
# from turtle import Turtle
# from turtle import Screen
#
# my_screen = Screen()
# my_turtle = Turtle()
#
# position = my_turtle.position()
# is_this_first_try = True
#
# steps = 10
#
# while steps > 0:
#     print(steps > 0)
#     steps = steps - 1
#     my_turtle.forward(100)
#     my_turtle.right(35)
#
# print(f"Result {steps > 0}")
# my_screen.mainloop()
#
#
# x = 5
# y = 5
# z = 8
# condition_1 = (x == y)
# print(f"condition 1 x == y {condition_1}")
# condition_2 = (z != x)
# print(f"condition 2 z != x {condition_2}")
# condition_3 = (z > x)
# print(f"condition 3 z > x {condition_3}")
# condition_4 = (x >= y)
# print(f"condition 4 x >= y {condition_4}")
# condition_5 = (z <= y)
# print(f"condition 5 z <= y {condition_5}")
# print(f"condition 1 and condition 2 {condition_1 and condition_2}")
# print(f"condition 4 and condition 5 {condition_4 and condition_5}")
# print(f"condition 4 or condition 5 {condition_4 or condition_5}")
# print(f"condition 4 and not condition 5 {condition_4 and not condition_5}")
#
#
#

# while True:
#     user_input = int(input("Put your number -> \n"))
#     if user_input > 10 or user_input < 3:
#         print(f"Please enter a number in range [3-10]")
#     else:
#         break

#
# import turtle
#
#
# screen = turtle.Screen()
# my_turtle = turtle.Turtle()

# while True:
#     user_input = int(input("Put your number -> \n"))
#     if user_input > 10 or user_input < 3:
#         print(f"Please enter a number in range [3-10]")
#     else:
#         break



# user_input = int(input("Put your number -> \n"))
#
# if user_input == 3:  # якщо
#     for _ in range(3):
#         my_turtle.forward(100)
#         my_turtle.left(120)
# elif user_input == 4:  # інакше якщо
#     for _ in range(4):
#         my_turtle.forward(100)
#         my_turtle.left(90)
# else:  # якщо жодна умова не здійснилась
#     for _ in range(6):
#         my_turtle.forward(100)
#         my_turtle.left(45)
#


user_input = input("Скільки разів написати Hello-> \n")
user_input_to_integer = int(user_input)
for number in range(user_input_to_integer):
    print(f"Номер {number} Hello")