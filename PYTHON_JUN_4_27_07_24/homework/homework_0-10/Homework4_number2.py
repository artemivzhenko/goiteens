import turtle


screen = turtle.Screen()
pen = turtle.Turtle()


text = "Hello World!"

pen.color("Red")
pen.write(text, font=("Arial", 24, "normal"))

pen.up()
pen.goto(0, 100)
pen.down()
pen.color("Blue")
pen.write(text, font=("Comic Sans MS", 24, "normal"))

pen.up()
pen.goto(0, 200)
pen.down()
pen.color("Black")
pen.write(text, font=("Verdana", 24, "normal"))

screen.mainloop()