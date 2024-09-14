import turtle
import time

screen = turtle.Screen()
my_turtle = turtle.Turtle()
penSize = 5

my_turtle.shape("turtle")
my_turtle.color("Blue")
my_turtle.pensize(penSize)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)

my_turtle.up()
my_turtle.goto(-300, -300)
my_turtle.down()

penSize = penSize +4
my_turtle.shape("circle")
my_turtle.color("yellow")
my_turtle.pensize(penSize)

my_turtle.speed(2)
my_turtle.forward(100)
my_turtle.left(120)
my_turtle.forward(100)
my_turtle.left(120)
my_turtle.forward(100)
my_turtle.left(120)


my_turtle.up()
my_turtle.goto(-300, 0)
my_turtle.down()

penSize = penSize - 7
my_turtle.shape("arrow")
my_turtle.color("Black")
my_turtle.pensize(penSize)

my_turtle.forward(40)
my_turtle.left(90)
my_turtle.forward(150)
my_turtle.right(90)
my_turtle.forward(40)
my_turtle.left(135)
my_turtle.forward(120)
my_turtle.left(90)
my_turtle.forward(120)
my_turtle.left(135)
my_turtle.forward(40)
my_turtle.right(90)
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(40)

my_turtle.up()
my_turtle.goto(300, -200)
my_turtle.down()

penSize = penSize
my_turtle.shape("square")
my_turtle.color("Green")
my_turtle.pensize(penSize)

my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)
my_turtle.left(30)
my_turtle.forward(50)


turtle.done()

