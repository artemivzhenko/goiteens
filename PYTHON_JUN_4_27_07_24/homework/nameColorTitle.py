import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
my_turtle = turtle.Turtle()


username = screen.textinput("Input name", "What is your name?:")
fontSize = screen.textinput("Input font size", "What size you prefer?:")
pen.write(username, font=("Arial", int(fontSize), "normal"))
color = screen.textinput("Input", "Put your color:")
pen.color(color)
pen.up()
pen.goto(100, 100)
pen.down()
pen.write(username)

screen.mainloop()