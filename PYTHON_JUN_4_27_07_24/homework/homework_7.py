import turtle


while True:
    user_input = int(input("Put your number -> \n"))
    if user_input > 10 or user_input < 3:
        print(f"Please enter a number in range [3-10]")
    else:
        break


my_turtle = turtle.Turtle()
window = turtle.Screen()


window.setup(width=900, height=700)


for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)


my_turtle.up()
my_turtle.goto(200, 0)
my_turtle.down()
my_turtle.circle(50)


my_turtle.up()
my_turtle.goto(-200, 0)
my_turtle.down()


for _ in range(6):
    my_turtle.forward(100)
    my_turtle.left(60)
my_turtle.up()
my_turtle.goto(-200, -200)
my_turtle.down()


radius = 5
while radius < 100:
    my_turtle.circle(radius, 180)
    radius += 10


my_turtle.up()
my_turtle.goto(0, -50)
my_turtle.down()
my_turtle.color("red")
for _ in range(4):
    my_turtle.forward(30)
    my_turtle.left(90)
my_turtle.up()
my_turtle.goto(0, -100)
my_turtle.down()
my_turtle.color("yellow")
for _ in range(4):
    my_turtle.forward(30)
    my_turtle.left(90)
my_turtle.up()
my_turtle.goto(0, -150)
my_turtle.down()
my_turtle.color("green")
for _ in range(4):
    my_turtle.forward(30)
    my_turtle.left(90)
my_turtle.up()
my_turtle.goto(200, -300)
my_turtle.down()


if user_input == 3:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(120)
elif user_input == 4:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(90)
elif user_input == 5:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(72)
elif user_input == 6:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(60)
elif user_input == 7:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(52)
elif user_input == 8:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(45)
elif user_input == 9:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(42)
elif user_input == 10:
    for _ in range(user_input):
        my_turtle.forward(100)
        my_turtle.left(40)


window.mainloop()