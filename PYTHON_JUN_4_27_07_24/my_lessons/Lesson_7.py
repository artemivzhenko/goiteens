import turtle


while True:
    user_input = int(input("Put your number -> \n"))
    if user_input > 10 or user_input < 3:
        print(f"Please enter a number in range [3-10]")
    else:
        break


screen = turtle.Screen()
my_turtle = turtle.Turtle()


if user_input == 3:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(120)
elif user_input == 4:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(90)
elif user_input == 5:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(72)
elif user_input == 6:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(60)
elif user_input == 7:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(52)
elif user_input == 8:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(45)
elif user_input == 9:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(42)
elif user_input == 10:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(40)


screen.mainloop()