import turtle
screen = turtle.Screen()

my_turtle = turtle.Turtle()

user_input = int(input("Input a number of horizontal lines from 1-4"))

for number in range(1, user_input + 1):
    turtle.forward(100)
    turtle.backward(100)
    turtle.penup()
    turtle.goto(0, 10 * number)
    turtle.pendown()

screen.mainloop()