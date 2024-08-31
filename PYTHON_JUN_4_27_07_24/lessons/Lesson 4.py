import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.color("red")
pen.up()
pen.goto(-100, -100)
pen.down()
text = screen.textinput("Input", "What is your name?:")
pen.write(text, font=("Arial", 24, "normal"))
screen.mainloop()