# import turtle
# import time
#
# screen = turtle.Screen()
# my_turtle = turtle.Turtle()
#
# my_turtle.shape("turtle")
# time.sleep(2)
# my_turtle.shape("circle")
# time.sleep(2)
# my_turtle.shape("triangle")
#
# turtle.done()


#
import turtle
import time

screen = turtle.Screen()
t = turtle.Turtle()

t.shape("arrow")
t.shape("turtle")
t.shape("square")
t.shape("circle")
t.shape("triangle")

turtle.done()

#
# import turtle
# import time
#
# screen = turtle.Screen()
# t = turtle.Turtle()
#
# screen.addshape("crying-vaughn-chat.gif")
# t.shape("crying-vaughn-chat.gif")
# t.forward(10)
# turtle.done()

#
#
# import turtle
# import time
#
# screen = turtle.Screen()
# t = turtle.Turtle()
#
# t.color("red", "yellow")
# t.begin_fill()
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.end_fill()
# turtle.done()


#
#
#
import turtle


screen = turtle.Screen()
t = turtle.Turtle()

t.color("blue")
t.speed(5)
t.pensize(8)
for i in range(10):
    t.circle(i * 5, 180)

t.forward(100)
t.backward(100)
turtle.done()