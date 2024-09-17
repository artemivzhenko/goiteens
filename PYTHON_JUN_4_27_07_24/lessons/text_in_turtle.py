import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.color("blue")
pen.write(screen.textinput("Input", "Enter some text:"), font=("Arial", 24, "normal"))
screen.mainloop()
