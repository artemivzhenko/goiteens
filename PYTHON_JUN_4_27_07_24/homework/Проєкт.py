import turtle
import random


screen = turtle.Screen()

Question = int(screen.textinput("Запитання?","Виберіть кількість гравців(2-5)"))
fan_turtle = screen.textinput("Обрання черепашки", "За яку черепашку ви вболіваєте? (red, blue, green, orange, yellow)")
sc = screen.bgcolor("skyblue")


pen = turtle.Turtle()

pen.penup()
pen.goto(-200, 190)
pen.pendown()
pen.speed(1000000000)
pen.color("black")
pen.forward(400)
pen.right(90)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.right(90)
pen.forward(400)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(50)
pen.color("black")
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.right(90)
pen.forward(350)
pen.left(90)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.color("white")
pen.forward(10)
pen.color("black")
pen.forward(10)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.hideturtle()






def init_turtle(color,Y):
    my_t = turtle.Turtle()

    my_t.penup()
    my_t.goto(-200, 40*Y)
    my_t.pendown()
    my_t.shape("turtle")
    my_t.color(color)
    return my_t

colors = ("red","blue","green","orange",'yellow')
my_turtle_list = []
my_turtle_positions = []
distances = {color: 0 for color in colors[:Question]}
fan_wins = 1
for number in range(Question):
    my_turtle = init_turtle(colors[number],number)
    my_turtle_list.append(my_turtle)
    my_turtle_positions.append(my_turtle.position()[0])


gameon = True
while gameon:
    for number in range(Question):
        my_turtle_list[number].forward(random.randint(20, 60))
        if my_turtle_list[number].xcor() >= 150:
            gameon = False
            winner_color = my_turtle_list[number].color()[0]
            break

result = turtle.Turtle()
result.penup()
result.hideturtle()
result.goto(0, 200)
result.write(f"Переможець: {winner_color}", align="center", font=("Arial", 35, "normal"))



y_offset = -100
for color in distances:
    result.goto(0, y_offset)
    result.write(f"{color.capitalize()} turtle: {distances[color]} units", align="center", font=("Arial", 20, "normal"))
    y_offset -= 30


result.goto(0, 250)
result.write(f"{fan_turtle.capitalize()} turtle wins: {fan_wins}", align="center", font=("Arial", 20, "normal"))












screen.mainloop()
