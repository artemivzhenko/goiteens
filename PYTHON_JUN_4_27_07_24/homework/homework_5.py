

import turtle

screen = turtle.Screen()
User_color = screen.textinput( input ,"Введіть назву кольору (наприклад, 'red', 'blue', 'green'): ")
User_shape = screen.textinput( input , "Ведіть назву модельки(наприклад, 'turtle', 'circle', 'square'): ")
my_turtle = turtle.Turtle()
my_turtle.pencolor(User_color)
my_turtle.shape(User_shape)





my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.goto(20, 20)
my_turtle.goto(20, 110)
my_turtle.goto(110, 110)
my_turtle.down()
my_turtle.goto(100, 100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.goto(20, 110)
my_turtle.right(90)
my_turtle.forward(90)
my_turtle.right(90)
my_turtle.forward(91)
my_turtle.right(90)
my_turtle.goto(20, 19)
my_turtle.left(90)
my_turtle.goto(0, -1)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.goto(111, 20)





my_turtle.penup()
my_turtle.goto(200,100)
my_turtle.forward(100)
my_turtle.pendown()
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.speed(10)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.speed(15)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.speed(20)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.speed(25)

turtle.done()

# Написати програму, що дозволяє користувачу ввести назву кольору, який буде використовуватися для малювання.
# Програма має змінити колір пера (pencolor()) відповідно до користувацького вводу.
# Створити малюнок за допомогою черепашки, де не має бути видимих перетинів ліній.
# Використовувати penup() та pendown() для контролювання, коли черепашка залишає слід.
# Створити програму, яка дозволяє користувачу вибирати форму та колір черепашки.
# Учень має додати опції для зміни цих параметрів на початку виконання програми.
# Створити просту анімацію, де черепашка малює квадрат, але змінює свою швидкість (speed()) після кожної сторони.


import turtle


screen = turtle.Screen()

turtle = turtle.Turtle()
turtle.speed(1)

turtle.forward(90)
turtle.backward(90)

turtle.penup()

turtle.goto(0, 90)

turtle.pendown()
turtle.forward(90)
turtle.backward(90)


screen.mainloop()

