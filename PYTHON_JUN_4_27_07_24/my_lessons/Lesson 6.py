import turtle


user_input = input("Склільки кутів має бути у фігури\n")
user_color = input("Який буде колір?\n")


screen = turtle.Screen()
my_turtle = turtle.Turtle()


if user_color == "red":
    my_turtle.pencolor("red")
elif user_color == "green":
    my_turtle.pencolor("green")
elif user_color == "blue":
    my_turtle.pencolor("blue")
elif user_color == "yellow":
    my_turtle.pencolor("yellow")

if user_input == "3":
    my_turtle.forward(90)
    my_turtle.right(120)
    my_turtle.forward(90)
    my_turtle.right(120)
    my_turtle.forward(90)
    my_turtle.right(120)
elif user_input == "4":
    my_turtle.forward(90)
    my_turtle.right(90)
    my_turtle.forward(90)
    my_turtle.right(90)
    my_turtle.forward(90)
    my_turtle.right(90)
    my_turtle.forward(90)
    my_turtle.right(90)
elif user_input == "5":
    my_turtle.forward(90)
    my_turtle.right(72)
    my_turtle.forward(90)
    my_turtle.right(72)
    my_turtle.forward(90)
    my_turtle.right(72)
    my_turtle.forward(90)
    my_turtle.right(72)
    my_turtle.forward(90)
    my_turtle.right(72)


screen.mainloop()