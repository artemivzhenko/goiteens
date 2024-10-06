import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
my_turtle = turtle.Turtle()

circleDescription = "Circle. Shape without angles"
traingleDescription = "Triangle. Have three angles. Sum of degrees of angles equals 180"
squareDescription = "Square. Have four angles."

def move():
    my_turtle.clear()

    my_turtle.penup()
    my_turtle.goto(-200, 100)
    my_turtle.pendown()
    square()
    my_turtle.write(squareDescription)

    my_turtle.penup()

    my_turtle.penup()
    my_turtle.goto(200, -100)
    my_turtle.pendown()
    traingle()
    my_turtle.write(traingleDescription)

    my_turtle.penup()

    my_turtle.penup()
    my_turtle.goto(0, 150)
    my_turtle.pendown()
    cilcle()
    my_turtle.write(circleDescription)



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

def cilcle():


    my_turtle.circle(100)

def traingle():

    my_turtle.forward(100)
    my_turtle.right(180-180/3)
    my_turtle.forward(100)
    my_turtle.right(180 - 180 / 3)
    my_turtle.forward(100)
    my_turtle.right(180 - 180 / 3)

move()
screen.mainloop()
