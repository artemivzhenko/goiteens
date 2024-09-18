import turtle



user_input = input("Склільки кутів має бути у фігури\n")

User_input = input("Виберіть колір blue,red,yellow чи green\n")

screen = turtle.Screen()
my_turtle = turtle.Turtle()




if User_input == "red":
    my_turtle.pencolor("red")
elif User_input == "blue":
    my_turtle.pencolor("blue")
elif User_input == "yellow":
    my_turtle.pencolor("yellow")
elif User_input == "green":
    my_turtle.pencolor("green")



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