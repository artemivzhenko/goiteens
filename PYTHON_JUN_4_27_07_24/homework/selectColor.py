import turtle

penColor = input("What colour use for painting?")

screen = turtle.Screen()

my_turtle = turtle.Turtle()
screen.setup(width=600.0, height=600.0)
penSize = 5

my_turtle.shape("turtle")
my_turtle.color(penColor)
my_turtle.pensize(penSize)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)

screen.mainloop()