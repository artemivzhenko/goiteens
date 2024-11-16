
import turtle

my_turtle = turtle.Turtle()

def move():
    my_turtle.forward(10)
    my_turtle.left(10)
    turtle.ontimer(move, 100)
    my_turtle.stamp()

move()

turtle.mainloop()
