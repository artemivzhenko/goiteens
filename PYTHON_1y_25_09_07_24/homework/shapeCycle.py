

# У вас є 4 фігури(коло, квадрат, трикутник, пятикутник)
# Користувач вводить число і ви малюєте вказану кількість
# фігур по порядку(фігури мають бути намальовані різним
# кольором і різною фігурою) зі зміщенням з
# лівого верхнього кута у правий нижній

import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

a = int(input("How many angles in the shape? (from 3 to 10)"))

x = int(-400)
y = int(400)
step = int(50)

my_turtle.penup()
my_turtle.goto(x, y)
my_turtle.pendown()

# if (a > 0):
#     print(1)
#
# if (a > 1):
#     print(2)
#
# if (a > 2):
#     print(3)
#
# if (a > 3):
#     print(4)
#
# if (a > 4):
#     print(1111)

my_turtle.penup()
for _ in range(a):
    x = x + a * step
    y = y - a * step / 2
    my_turtle.goto(x, y)

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

    my_turtle.circle(30)

    my_turtle.penup()
    my_turtle.goto(x, y-step)
    my_turtle.pendown()
    for _ in range(3):
        my_turtle.forward(50)
        my_turtle.right(360 / 3)

    my_turtle.penup()
    my_turtle.goto(x, y - step*2)
    my_turtle.pendown()

    for _ in range(4):
        my_turtle.forward(50)
        my_turtle.right(360/4)

    my_turtle.penup()
    my_turtle.goto(x, y-step*4)
    my_turtle.pendown()

    for _ in range(5):
        my_turtle.forward(50)
        my_turtle.right(360/5)

    my_turtle.penup()

screen.mainloop()