import turtle



screen = turtle.Screen()
pen = turtle.Turtle()


for _ in range(4):
    pen.forward(100)
    pen.right(90)
pen.write("Квадрат")

pen.up()
pen.goto(-200,0)
pen.down()

for _ in range(6):
    pen.right(60)
    pen.forward(60)

pen.left(180)
pen.forward(60)

pen.write("Шестекутник")


pen.up()
pen.goto(250,0)
pen.down()


for _ in range(5):
    pen.left(72)
    pen.forward(70)

pen.write("П'ятекутник")






























screen.mainloop()