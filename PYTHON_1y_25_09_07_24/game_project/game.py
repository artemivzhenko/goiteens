import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

my_turtle.goto(0, 0)
my_turtle.penup()

my_turtle.color("black")
my_turtle.write("Welcome on board!", align="center", font=("Arial", 20, "bold"))

def start_game(x,y):
    print("Game started!")
    global num_players
    num_players = int(screen.textinput("Number of players", "Enter the number of players (1-4):"))
    print(f"Number of players: {num_players}")

    screen.clearscreen()

    my_turtle.penup()
    my_turtle.goto(-350, -250)
    my_turtle.pendown()
    my_turtle.color("black")

    my_turtle.pensize(3)
    for _ in range(2):
        my_turtle.forward(700)
        my_turtle.left(90)
        my_turtle.forward(500)
        my_turtle.left(90)

    start_x, start_y = -350, -200

    my_turtle.penup()
    my_turtle.goto(start_x, start_y)
    my_turtle.pendown()
    my_turtle.color("blue")
    my_turtle.forward(700)

    finish_x, finish_y = -350, 200

    my_turtle.penup()
    my_turtle.goto(finish_x, finish_y)
    my_turtle.pendown()
    my_turtle.color("red")
    my_turtle.forward(700)

    my_turtle.penup()
    my_turtle.goto(start_x + 10, start_y - 30)
    my_turtle.color("blue")
    my_turtle.write("Старт", font=("Arial", 16, "bold"))
    my_turtle.goto(finish_x + 10, finish_y + 20)
    my_turtle.color("red")
    my_turtle.write("Фініш", font=("Arial", 16, "bold"))

    my_turtle.hideturtle()

    turtles = []
    colors = ["red", "blue", "green", "yellow", ]
    for i in range(num_players):
        t = turtle.Turtle()
        t.color(colors[i])
        t.shape("turtle")
        # t.shape("triangle")
        t.penup()
        t.goto(start_x + (700 / (num_players + 1)) * (i + 1), start_y)
        t.pendown()
        turtles.append(t)

my_turtle.penup()
my_turtle.goto(-50, 0)
my_turtle.pendown()
my_turtle.color("green")
my_turtle.begin_fill()
for _ in range(2):
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.right(90)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(0, -20)
my_turtle.color("Yellow")
my_turtle.write("Game start.", align="center", font=("Arial", 12, "bold"))
my_turtle.hideturtle()

screen.onscreenclick(start_game, 1)

screen.mainloop()
