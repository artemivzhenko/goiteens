import turtle
window = turtle.Screen()
window.title("Повноекранне вікно для черепашки")          
window.setup(width=700, height=700)

y = turtle.Turtle()
y.color("blue")
y.shape("square")
y.pensize(6)
y.forward(80)
y.left(120)
y.forward(80)
y.left(120)
y.forward(80)
y.left(120)


x = turtle.Turtle()
x.up()
x.goto(140, 0)
x.down()
x.color("red")
x.shape("triangle")
x.pensize(9)
x.forward(40)
x.left(90)
x.forward(40)
x.left(90)
x.forward(40)
x.left(90)
x.forward(40)
x.left(90)





a = turtle.Turtle()
a.up()
a.goto(-210, 0)
a.down()
a.color("black")
a.shape("turtle")
a.pensize(3)
a.forward(120)
a.left(72)
a.forward(120)
a.left(72)
a.forward(120)
a.left(72)
a.forward(120)
a.left(72)
a.forward(120)
a.left(72)

turtle.done()


