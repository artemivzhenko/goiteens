import turtle
window = turtle.Screen()
my_turtle = turtle.Turtle()
user_name = (input('Enter your name\n'))
user_second_name = (input('Enter your second name\n'))
window_color = (input('Enter your favorite color\n'))
window.bgcolor(window_color)

my_turtle.color('yellow')
my_turtle.write(user_name + user_second_name, font =('Arial', 24, 'normal'))





window.mainloop()