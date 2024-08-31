import turtle



screen = turtle.Screen()
pen = turtle.Turtle()
pen.color("blue")
pen.up()
pen.goto(-100, -100)
pen.down()
text = screen.textinput("Input", "Enter some text:")
pen.write(text, font=("Arial", 24, "normal"))
screen.mainloop()