for number in range(1, user_input + 1):


    pen.forward(100)
    pen.backward(100)
    pen.penup()
    pen.goto(20 * number, 10 * number)
    pen.pendown()

    my_turtle = turtle.Turtle()
    my_turtle.penup()
    my_turtle.goto(-200, 0)
    my_turtle.pendown()
    my_turtle.shape("turtle")
    my_turtle.color("green")
    my_turtle.speed(1)
    position = my_turtle.position()
    while position != (200.0, 0):
        my_turtle.forward(10)
        position = my_turtle.position()

        for _ in range(10):
            random_speed = random.randint(0, 10)
            my_t.speed(random_speed)
            my_t.forward(50)