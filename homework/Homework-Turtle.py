import turtle

window = turtle.Screen()
window.title("Повноекранне вікно для черепашки")
window.setup(width=500, height=500)

my_turtle = turtle.Turtle()
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.goto(20, 20)
my_turtle.goto(20, 110)
my_turtle.goto(110, 110)
my_turtle.down()
my_turtle.goto(100, 100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.goto(20, 110)
my_turtle.right(90)
my_turtle.forward(90)
my_turtle.right(90)
my_turtle.forward(91)
my_turtle.right(90)
my_turtle.goto(20, 19)
my_turtle.left(90)
my_turtle.goto(0, -1)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.goto(111, 20)





turtle.done()
window.mainloop()