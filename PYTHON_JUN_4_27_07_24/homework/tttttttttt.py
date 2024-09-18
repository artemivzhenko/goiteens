import turtle

# Отримання користувацького вводу
user_color = input("Введіть назву кольору (наприклад, 'red', 'blue', 'green'): ")

# Налаштування черепашки
t = turtle.Turtle()
t.pencolor(user_color)

# Малюємо квадрат
for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()