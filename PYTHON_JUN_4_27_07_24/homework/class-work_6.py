import turtle



screen = turtle.Screen()
pen = turtle.Turtle()
pen.color =  "red"

user_input = int(input("ведіть число\n"))



for _ in range(1,user_input + 1):

    for _ in range(4):

        pen.right(90)
        pen.forward(50)


        for _ in range(3):
            pen.forward(100)
            pen.right(120)








screen.mainloop()