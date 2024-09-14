import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

penSize = 5

my_turtle.shape("turtle")
my_turtle.color("Blue")

my_turtle.penup()
my_turtle.goto(-100, -100)
my_turtle.pendown()

my_turtle.pensize(penSize)
my_turtle.speed(1)
my_turtle.forward(400)
my_turtle.left(90)

my_turtle.speed(5)
my_turtle.forward(400)
my_turtle.left(90)

my_turtle.speed(2)
my_turtle.forward(400)
my_turtle.left(90)

my_turtle.speed(10)
my_turtle.forward(400)
my_turtle.left(90)

screen.mainloop()