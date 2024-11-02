import turtle


screen = turtle.Screen()
my_turtle = turtle.Turtle()

my_shape_list = ["circle", "arrow", "turtle", "square", "triangle"]
my_turtle.speed(0)
for number in range(1, 16):
    for shape in my_shape_list:
        my_turtle.shape(shape)
        my_turtle.shapesize(0.2 * number)
        my_turtle.circle(30 * number, 30)
        my_turtle.stamp()

screen.mainloop()