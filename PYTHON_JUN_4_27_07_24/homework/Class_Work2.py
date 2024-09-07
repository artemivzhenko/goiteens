import turtle

screen = turtle.Screen()
t = turtle.Turtle()
turtle.shape("triangle")
turtle.color("blue")
turtle.pensize(3)
turtle.forward(50)
turtle.down()
turtle.shape('turtle')
turtle.color("red")
turtle.pensize(5)
turtle.goto(50, 50)
turtle.shape('square')
turtle.color("green")
turtle.pensize(6)
turtle.goto(-8,50)
turtle.shape('arrow')
turtle.color("orange")
turtle.pensize(10)
turtle.goto(-8,-2)







screen.mainloop()