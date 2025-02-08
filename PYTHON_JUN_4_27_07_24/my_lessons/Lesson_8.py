import turtle


t = turtle.Turtle()
screen = turtle.Screen()

user_input = int(screen.textinput("Figure","Put number(4-6) --> \n"))


if user_input == 4:
    t.up()
    t.goto(330, 245)
    t.down()
    for _ in range(8):
        t.circle(30, 45)
        t.stamp()


    t.up()
    t.goto(195, 145)
    t.down()
    for _ in range(4):
        t.forward(25)
        t.stamp()
        t.forward(25)
        t.stamp()
        t.left(90)


    t.up()
    t.goto(55, 45)
    t.down()
    for _ in range(3):
        t.forward(25)
        t.stamp()
        t.forward(25)
        t.stamp()
        t.left(120)


    t.up()
    t.goto(-90, -45)
    t.down()
    for _ in range(5):
        t.forward(20)
        t.stamp()
        t.forward(20)
        t.stamp()
        t.left(72)


elif user_input == 5:
    t.up()
    t.goto(330, 245)
    t.down()
    for _ in range(8):
        t.circle(30, 45)
        t.stamp()


    t.up()
    t.goto(195, 145)
    t.down()
    for _ in range(4):
        t.forward(25)
        t.stamp()
        t.forward(25)
        t.stamp()
        t.left(90)


    t.up()
    t.goto(55, 45)
    t.down()
    for _ in range(3):
        t.forward(25)
        t.stamp()
        t.forward(25)
        t.stamp()
        t.left(120)


    t.up()
    t.goto(-90, -45)
    t.down()
    for _ in range(5):
        t.forward(20)
        t.stamp()
        t.forward(20)
        t.stamp()
        t.left(72)

    t.up()
    t.goto(-240, -145)
    t.down()
    for _ in range(8):
        t.circle(30, 45)
        t.stamp()


elif user_input == 6:
    t.up()
    t.goto(330, 245)
    t.down()
    for _ in range(8):
        t.circle(30, 45)
        t.stamp()

    t.up()
    t.goto(195, 145)
    t.down()
    for _ in range(4):
        t.forward(25)
        t.stamp()
        t.forward(25)
        t.stamp()
        t.left(90)

    t.up()
    t.goto(60, 45)
    t.down()
    for _ in range(3):
        t.forward(25)
        t.stamp()
        t.forward(25)
        t.stamp()
        t.left(120)

    t.up()
    t.goto(-75, -45)
    t.down()
    for _ in range(5):
        t.forward(25)
        t.stamp()
        t.forward(25)
        t.stamp()
        t.left(72)

    t.up()
    t.goto(-210, -145)
    t.down()
    for _ in range(8):
        t.circle(30, 45)
        t.stamp()


    t.up()
    t.goto(-330, -245)
    t.down()
    for _ in range(4):
        t.forward(25)
        t.stamp()
        t.forward(25)
        t.stamp()
        t.left(90)

s.mainloop()