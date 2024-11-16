import turtle


screen = turtle.Screen()

t = turtle.Turtle()
t.speed(0)
def draw_shape():
    t.clear()
    t.penup()
    t.goto(-25, 0)
    t.pendown()
    t.color("blue")
    for _ in range(4):
        t.forward(50)
        t.right(90)
    screen.ontimer(draw_shape, 500)

draw_shape()



screen.mainloop()