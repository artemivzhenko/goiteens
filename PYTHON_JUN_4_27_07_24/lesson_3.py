import turtle


window = turtle.Screen()
window.title("Повноекранне вікно для черепашки")           # Вказуємо назву вікна для малювання
window.setup(width=700, height=700)                        # Вказуємо розмірність нашого вікна (int числа більше 1 = розмір у пікселях, float числа >= 1 розмір вікна у %)

my_turtle = turtle.Turtle()
# my_turtle.forward(100)
# my_turtle.up()
# my_turtle.forward(50)
# my_turtle.down()
# my_turtle.forward(100)
#
my_turtle.up()
my_turtle.goto(100, 100)
my_turtle.down()
#
# my_turtle.forward(50)# my_turtle.reset()                                         # Очистити поле і повернути черепашку на її місце


for _ in range(5):
    my_turtle.forward(100)
    my_turtle.left(72)

my_turtle.up()
my_turtle.goto(-100, -100)
my_turtle.down()

my_turtle.forward(100)
my_turtle.left(120)
my_turtle.forward(100)
my_turtle.left(120)
my_turtle.forward(100)


turtle.done()
window.mainloop()                                          # Відкриття вікна


# wn.bgcolor("green")
# wn.setup(width=0.8, height=0.6)
# t = turtle.Turtle()
# t.forward(100)
#
# t.up()
# t.forward(50)
# t.goto(100, 100)
# t.down()
# t.forward(100)
#
# turtle.done()


# Для трикутника у якого 1 кут = 60 ми робили зміщення 120 тому що 180 - 60 = 120
# Для чотирикутника у якого 1 кут = 90 ми робили зміщення 90 тому що 180 - 90 = 90
# Треба порахувати для пятикутника у якого 540 градусів сума кутів
# 540
#  Для пятикутника у якого 1 кут = 108 ми робили зміщення 72 тому що 180 - 108 = 72
#
#
