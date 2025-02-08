import turtle



screen = turtle.Screen()
pen = turtle.Turtle()

pen.up()
pen.goto(0,0)
pen.down()

pen.speed(10000000)

pen.color("green")
for i in range(300):
    pen.forward(20 + i * 2)
    pen.left(90)














screen.mainloop()