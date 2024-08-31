import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.color("blue")
pen.up()
pen.goto(-100, -100)
pen.down()
pen.write("Привіт, світ!", font=("Arial", 24, "normal"))
screen.mainloop()
