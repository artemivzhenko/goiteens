import turtle

screen = turtle.Screen()

my_turtle = turtle.Turtle()

my_turtle.pendown()

my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)

my_turtle.left(45)
my_turtle.forward(70)
my_turtle.right(90)
my_turtle.forward(70)

my_turtle.penup()

my_turtle.right(90)
my_turtle.forward(70)
my_turtle.right(45)

my_turtle.pendown()

for _ in range(25):
    my_turtle.forward(3)
    my_turtle.right(15)

screen.mainloop()