import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()
screen.setup(width=800, height=600)


# Малювання меж поля
my_turtle.penup()
my_turtle.goto(-350, -250)  # Нижній лівий кут
my_turtle.pendown()
my_turtle.color("black")

my_turtle.pensize(3)
for _ in range(2):
    my_turtle.forward(700)  # Довжина поля
    my_turtle.left(90)
    my_turtle.forward(500)  # Висота поля
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

my_turtle.hideturtle()

screen.mainloop()