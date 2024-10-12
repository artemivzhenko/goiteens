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