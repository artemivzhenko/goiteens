import turtle, random


Tx = ("text","Text","text_")
Type = ("Arial","Times New Roman","Courier New")
colors = ("red","blue","yellow","black","green","pink")

window = turtle.Screen()
window.title("Повноекранне вікно для черепашки")
window.setup(width=1000, height=1000)

screen = turtle.Screen()
pen = turtle.Turtle()
pen.color(random.choice(colors))
text = "hello world\n"
Text = "hello world\n\n"
text_ = "hello world"
pen.write(text ,font = (random.choice(Type),34,"normal"))
pen.write(Text ,font = (random.choice(Type),34,"normal"))
pen.write(text_ ,font = (random.choice(Type),34,"normal"))
screen.mainloop()