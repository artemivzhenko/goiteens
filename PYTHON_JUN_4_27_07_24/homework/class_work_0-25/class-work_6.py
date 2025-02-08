import turtle



screen = turtle.Screen()
pen = turtle.Turtle()




pen.up()
pen.goto(-250,-250)
pen.down()
pen.color("red")

for _ in range(4):
    pen.forward(100)
    pen.right(90)

pen.up()
pen.goto(0,0)
pen.down()
pen.color("blue")

for _ in range(6):
    pen.forward(100)
    pen.right(60)

pen.up()
pen.goto(150,150)
pen.down()
pen.color("green")

for _ in range(3):
    pen.forward(100)
    pen.right(120)




screen.mainloop()