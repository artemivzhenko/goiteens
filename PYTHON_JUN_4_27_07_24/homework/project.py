import turtle
import random
import time

screen = turtle.Screen()
pen = turtle.Turtle()
screen.setup(width=2160, height=800, startx=0, starty=0)
screen.bgcolor("orange")
screen.title("Battleship")


win_stats = {'red': 0, 'green': 0, 'blue': 0, 'black': 0}


while True:
    player_number = int(screen.textinput("Players", "Enter how many players?(2-4)"))
    if player_number > 4 or player_number < 2:
        player_number = int(screen.textinput("Players", "Enter how many players?(2-4)"))
    else:
        break

pen.speed(0)

def init_field(pen, y):
    pen.penup()
    pen.goto(-550, 100 * y)
    pen.down()
    pen.right(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(1050)
    pen.left(90)
    pen.up()
    pen.forward(100)
    pen.down()
    pen.left(90)
    pen.forward(1050)
    pen.backward(50)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(950)
    pen.left(90)
    pen.color("white")
    for _ in range(5):
        pen.forward(10)
        pen.up()
        pen.forward(10)
        pen.down()
    pen.left(180)
    pen.color("black")
    for _ in range(5):
        pen.forward(10)
        pen.up()
        pen.forward(10)
        pen.down()
    pen.left(90)
    pen.forward(1)
    pen.left(90)
    pen.color("white")
    for _ in range(5):
        pen.forward(10)
        pen.up()
        pen.forward(10)
        pen.down()
    pen.left(180)
    pen.color("black")
    for _ in range(5):
        pen.forward(10)
        pen.up()
        pen.forward(10)
        pen.down()
    pen.left(90)

def init_turtle(color, y):
    new_turtle = turtle.Turtle()
    new_turtle.speed(0)
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-500, (100 * y) - 50)
    new_turtle.shape("turtle")
    new_turtle.pendown()
    return new_turtle

colors = ("red", "green", "blue", "black")

while True:
    my_turtle_list = []
    for i in range(player_number):
        init_field(pen, i)
        my_turtle = init_turtle(colors[i], i)
        my_turtle.speed(5)
        my_turtle_list.append(my_turtle)
    pen.hideturtle()
    winner = None
    game_on = True
    while game_on:
        for i in range(player_number):
            my_turtle_list[i].forward(random.randint(50, 150))
            if my_turtle_list[i].position()[0] >= 500.0:
                winner = my_turtle_list[i]
                game_on = False
                break


    win_color = winner.color()[0]
    win_stats[win_color] += 1
    pen.up()
    pen.goto(0, -200)
    pen.down()
    pen.write(f"Player {win_color} wins!", align="center", font=("Arial", 30, "normal"))
    pen.up()
    pen.goto(0, -250)
    pen.down()
    pen.write(f"Win statistics: {win_stats}", align="center", font=("Arial", 20, "normal"))

    again = screen.textinput("Продовження" , "Почати гру ше раз?")
    if again == "Так":
        game_on = True
        screen.clear()
        time.sleep(2)
        screen.bgcolor("orange")
    else:
        break

screen.mainloop()
