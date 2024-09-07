import turtle, random

colors = ('red','green','blue','pink','yellow','purple','')
Colors = ('orange','green','blue','pink','yellow','purple','black',)



window = turtle.Screen()
window.bgcolor(random.choice(colors))
screen = turtle.Screen()
pen = turtle.Turtle()
pen.color(random.choice(Colors))
text = screen.textinput("input" , "What is your name and last name")
pen.write(text ,font=("Arial",34,"normal"))
screen.mainloop()