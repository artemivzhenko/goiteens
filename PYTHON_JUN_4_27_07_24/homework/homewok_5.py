import turtle

window = turtle.Screen()
color_turtle = window.textinput("Колір черепашки" , "Ввдедіть колір черепашки:")
shape_turtle = window.textinput("Формa черепашки", "Введіть форму черепашки(turtle, arrow, circle, square, triangle")

turtle = turtle.Turtle()
turtle.pencolor(color_turtle)
turtle.shape(shape_turtle)

turtle.circle(50)

turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.penup()
turtle.goto(-50, -200)
turtle.pendown()



turtle.speed(3)
turtle.forward(90)
turtle.left(90)

turtle.speed(5)
turtle.forward(90)
turtle.left(90)

turtle.speed(8)
turtle.forward(90)
turtle.left(90)

turtle.speed(0)
turtle.forward(90)
turtle.left(90)


window.mainloop()