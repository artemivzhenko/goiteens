import turtle
import time

screen = turtle.Screen()
my_turtle = turtle.Turtle()

my_turtle.color("blue", "yellow")       # Вказали колір черепашки "blue" і колір заливки на "yellow"
my_turtle.shape("triangle")             # Вказали форму черепашки на triangle
my_turtle.pensize(5)                    # Вказали товщину лінії черепашки на 5
my_turtle.speed(3)                      # Вказали швидкість малювання на 3
my_turtle.begin_fill()                  # Вказали початок заливки

my_turtle.forward(100)
my_turtle.right(120)
time.sleep(0.5)
my_turtle.forward(100)
my_turtle.right(120)
time.sleep(0.5)
my_turtle.forward(100)
my_turtle.right(120)
time.sleep(0.5)

my_turtle.end_fill()                    # Вказали закінчення заливки


my_turtle.color("red", "green")         # Вказали колір черепашки "red" і колір заливки на "green"
my_turtle.shape("turtle")               # Вказали форму черепашки на turtle
my_turtle.pensize(10)                   # Вказали товщину лінії черепашки на 10
my_turtle.speed(8)                      # Вказали швидкість малювання на 8


my_turtle.penup()
my_turtle.goto(0, 100)
my_turtle.pendown()

my_turtle.begin_fill()                  # Вказали початок заливки
my_turtle.circle(50)
my_turtle.end_fill()                    # Вказали закінчення заливки


my_turtle.color("blue", "purple")          # Вказали колір черепашки "blue" і колір заливки на "purple"
my_turtle.shape("arrow")                   # Вказали форму черепашки на arrow
my_turtle.pensize(2)                       # Вказали товщину лінії черепашки на 10
my_turtle.speed(5)                         # Вказали швидкість малювання на 8


my_turtle.penup()
my_turtle.goto(0, -200)
my_turtle.pendown()

my_turtle.begin_fill()                  # Вказали початок заливки
my_turtle.right(120)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.left(60)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)
my_turtle.end_fill()                    # Вказали закінчення заливки


screen.mainloop()
