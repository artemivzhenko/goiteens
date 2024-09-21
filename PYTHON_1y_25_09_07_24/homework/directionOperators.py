import turtle

screen = turtle.Screen()
screen.title("Screen for painting")
screen.setup(width=600.0, height=600.0)

my_turtle = turtle.Turtle()


direction = input("Which direction? (use A,W,S,D)")

if(direction == "W" or direction == "w"):
    my_turtle.forward(20)

elif (direction == "A" or "a" == direction):
    my_turtle.left(90)
    my_turtle.forward(20)

elif (direction == "D" or direction == "d"):
    my_turtle.right(90)
    my_turtle.forward(20)

elif (direction == "S" or direction == "s"):
    my_turtle.backward(20)

screen.mainloop()