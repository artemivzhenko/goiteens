import turtle



window = turtle.Screen()
t = turtle.Turtle()


User_input = window.textinput("Input", "Виберіть свою частину дня наприклад (Ніч,День,Ранок,Вечір):")
if User_input == "Ніч":
    window.bgcolor("Black")
elif User_input == "День":
    window.bgcolor("yellow")
elif User_input == "Ранок":
    window.bgcolor("skyblue")
elif User_input == "Вечір":
    window.bgcolor("orange")
else:
    print("Не зрозуміло повторіть спробу :( ")






window.mainloop()