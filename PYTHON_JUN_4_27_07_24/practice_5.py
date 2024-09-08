import turtle
import time

screen = turtle.Screen()
my_turtle = turtle.Turtle()

my_turtle.color("blue", "yellow")
my_turtle.shape("triangle")
my_turtle.pensize(5)
my_turtle.speed(3)
my_turtle.begin_fill()

my_turtle.forward(100)
my_turtle.right(120)
time.sleep(0.5)
my_turtle.forward(100)
my_turtle.right(120)
time.sleep(0.5)
my_turtle.forward(100)
my_turtle.right(120)
time.sleep(0.5)

my_turtle.end_fill()


my_turtle.color("red", "green")
my_turtle.shape("turtle")
my_turtle.pensize(10)
my_turtle.speed(8)


my_turtle.penup()
my_turtle.goto(0, 100)
my_turtle.pendown()

my_turtle.begin_fill()
my_turtle.circle(50)
my_turtle.end_fill()


my_turtle.color("blue", "purple")
my_turtle.shape("arrow")
my_turtle.pensize(2)
my_turtle.speed(5)


my_turtle.penup()
my_turtle.goto(0, -200)
my_turtle.pendown()

my_turtle.begin_fill()
my_turtle.right(120)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.left(60)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)
my_turtle.end_fill()                    


screen.mainloop()
