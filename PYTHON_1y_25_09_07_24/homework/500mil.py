import turtle

screen = turtle.Screen()

my_turtle = turtle.Turtle()

def move():
    my_turtle.clear()
    square()

    turtle.ontimer(move, 500)

def square():
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)

move()

screen.mainloop()