import turtle
import time


t = turtle.Turtle()


colors = ["red", "green","yellow"]


while True:
    for color in colors:
     t.clear()
     t.fillcolor(color)
     t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    time.sleep(1)




screen.mainloop()