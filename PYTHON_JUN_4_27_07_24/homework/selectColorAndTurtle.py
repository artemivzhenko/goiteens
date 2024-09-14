import turtle

penColor = input("What colour use for painting?")
turtleShape = input("What shape use for painting? (turtle, arrow, circle, square, triangle): ")

screen = turtle.Screen()
my_turtle = turtle.Turtle()
screen.setup(width=600.0, height=600.0)
penSize = 6
my_turtle.pencolor(penColor)
my_turtle.shape(turtleShape)

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

screen.mainloop()