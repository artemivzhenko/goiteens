import turtle
import random



screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_shape_list = ["circle", "arrow", "turtle", "square", "triangle"]



for number in range(1, 16):
    my_turtle.penup()
    my_turtle.setx(number * random.randint(0, 10))
    my_turtle.sety(number * random.randint(0, 10))
    my_turtle.pendown()
    for shape in my_shape_list:
        my_turtle.shape(shape)
        my_turtle.shapesize(0.2 * number)
        my_turtle.circle(30 * number, 30)
        my_turtle.stamp()
    my_turtle.clear()
screen.mainloop()