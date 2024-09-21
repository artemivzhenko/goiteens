import turtle

user_go = input("В яку сторону підемо?\n")
user_time = input("Який час дня?\n")
screen = turtle.Screen()
my_turtle = turtle.Turtle()

if user_go == "вперед":
    my_turtle.color("red")
    my_turtle.left(90)
    my_turtle.forward(50)
elif user_go == "назад":
    my_turtle.color("green")
    my_turtle.left(90)
    my_turtle.backward(50)
elif user_go == "вліво":
    my_turtle.color("blue")
    my_turtle.left(180)
    my_turtle.forward(50)
elif user_go == "вправо":
    my_turtle.color("purple")
    my_turtle.forward(50)


if user_time == "день":
    screen.bgcolor("white")
elif user_time == "вечір":
    screen.bgcolor("orange")
elif user_time == "ранок":
    screen.bgcolor("orange")
elif user_time == "ніч":
    screen.bgcolor("black")

screen.mainloop()