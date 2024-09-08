import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
my_turtle = turtle.Turtle()

text = "Hello, World!"

pen.color("Red")
pen.goto(0, 10)
pen.write(text, font=("Arial", 20, "normal"))
pen.up()
pen.down()

pen.color("Green")
pen.goto(0, 100)
pen.write(text, font=("Comic Sans", 30, "normal"))
pen.up()
pen.down()

pen.color("Blue")
pen.goto(-0, 200)
pen.write(text, font=("Times new roman", 40, "normal"))
pen.up()

pen.down()


screen.mainloop()