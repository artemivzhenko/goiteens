import turtle
import time

screen = turtle.Screen()
my_turtle = turtle.Turtle()

my_turtle.color("blue", "yellow")       # Вказали колір черепашки "blue" і колір заливки "yellow"
my_turtle.shape("triangle")             # Вказали форму черепашки на triangle
my_turtle.pensize(5)                    # Вказали товщину лінії черепашки на 5
my_turtle.speed(3)                      # Вказали швидкість малювання на 3
my_turtle.begin_fill()                  # Вказали початок заливки

my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)

my_turtle.end_fill()                    # Вказали закінчення заливки


my_turtle.color("blue", "yellow")       # Вказали колір черепашки "blue" і колір заливки "yellow"
my_turtle.shape("triangle")             # Вказали форму черепашки на triangle
my_turtle.pensize(5)                    # Вказали товщину лінії черепашки на 5
my_turtle.speed(3)                      # Вказали швидкість малювання на 3
my_turtle.begin_fill()                  # Вказали початок заливки

screen.mainloop()
