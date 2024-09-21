import turtle



timeOfDay = input("What hour is now?")

if (int(timeOfDay)  >=6 and int(timeOfDay) < 20):
    color = "Yellow"
elif(int(timeOfDay) >=0 and int(timeOfDay) <6 or int(timeOfDay) >=20 and int(timeOfDay) <24):
    color = "Blue"
else:

    print("Its not correct hour")

screen = turtle.Screen()
screen.title("Screen for painting")
screen.setup(width=600.0, height=600.0)
screen.bgcolor(color)

screen.mainloop()