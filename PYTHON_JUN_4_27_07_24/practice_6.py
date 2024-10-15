import turtle

user_input = input("Склільки кутів має бути у фігури\n")

screen = turtle.Screen()

my_turtle = turtle.Turtle()

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
