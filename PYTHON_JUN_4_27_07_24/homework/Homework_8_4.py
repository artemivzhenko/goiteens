import turtle



screen = turtle.Screen()
screen.title("Turtle Move")
t = turtle.Turtle()
t.speed(1)


def move_turtle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


while True:
    x = int(screen.numinput("Координати", "Введіть координату x:", 0, minval=-screen.window_width()//2, maxval=screen.window_width()//2))
    y = int(screen.numinput("Координати", "Введіть координату y:", 0, minval=-screen.window_height()//2, maxval=screen.window_height()//2))
    move_turtle(x, y)












screen.mainloop()





