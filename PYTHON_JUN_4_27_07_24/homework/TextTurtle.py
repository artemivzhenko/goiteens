import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
my_turtle = turtle.Turtle()


username = screen.textinput("Input", "What is your name?:")
pen.write(username, font=("Arial", 24, "normal"))

pen.color("Red")
pen.up()
pen.goto(100, 100)
pen.down()
pen.write(username)

screen.mainloop()