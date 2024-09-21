import turtle


screen = turtle.Screen()
pen = turtle.Turtle()


user_input = int(input("напишіть числоn до 20 -> "))

pen.right(90)

for number in range(1, user_input + 1):


    pen.forward(100)
    pen.backward(100)
    pen.penup()
    pen.goto(20 * number, 10 * number)
    pen.pendown()














screen.mainloop()