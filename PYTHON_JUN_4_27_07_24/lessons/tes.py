import turtle
s = turtle.Screen()
my_turtle = turtle.Turtle()
user_input = int(s.textinput("Input","введіть число фігур"))
my_turtle.shape("turtle")
my_turtle.penup()
my_turtle.setx(-300)
my_turtle.sety(300)
my_turtle.pendown()
figure_number = 0
for _ in range(user_input):
    my_turtle.penup()
    my_turtle.setx(-300 + _ * 100)
    my_turtle.sety(300 - (_ * 100))
    my_turtle.pendown()
    if figure_number == 0:
        my_turtle.shape("turtle")
        my_turtle.color("green")
        for _ in range(5):
            my_turtle.forward(50)
            my_turtle.stamp()
            my_turtle.forward(50)
            my_turtle.left(72)
            my_turtle.stamp()
    elif figure_number == 1:
        my_turtle.shape("square")
        my_turtle.color("red")
        for _ in range(4):
            my_turtle.forward(50)
            my_turtle.stamp()
            my_turtle.forward(50)
            my_turtle.left(90)
            my_turtle.stamp()
    elif figure_number == 2:
        my_turtle.shape("triangle")
        my_turtle.color("blue")
        for _ in range(3):
            my_turtle.forward(50)
            my_turtle.stamp()
            my_turtle.forward(50)
            my_turtle.left(120)
            my_turtle.stamp()
    elif figure_number == 3:
        my_turtle.shape("circle")
        my_turtle.color("orange")
        for _ in range(8):
            my_turtle.circle(50, 45)
            my_turtle.stamp()
    if figure_number == 3:
        figure_number = 0
    else:
        figure_number += 1

s.mainloop()
