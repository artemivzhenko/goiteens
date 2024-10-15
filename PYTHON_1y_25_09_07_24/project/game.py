import turtle


def generate_board(size):
    return [[None for _ in range(size)] for _ in range(size)]


def main():
    pen = turtle.Turtle()
    pen.shape("turtle")
    while True:
        board_size = int(screen.textinput("Input", "Input board size:"))
        if board_size >= 3:
            break
    board = generate_board(board_size)
    start_x = -50 * (board_size - 2)
    start_y = 50 * board_size
    pen.speed(10)
    pen.penup()
    pen.goto(start_x, start_y)
    pen.right(90)
    pen.pendown()
    for _ in range(1, board_size):
        pen.forward(100 * board_size)
        pen.backward(100 * board_size)
        pen.penup()
        pen.goto(start_x + (_ * 100), start_y)
        pen.pendown()
    pen.penup()
    start_x -= 100
    start_y -= 100
    pen.goto(start_x, start_y)
    pen.left(90)
    pen.pendown()
    for _ in range(1, board_size):
        pen.forward(100 * board_size)
        pen.backward(100 * board_size)
        pen.penup()
        pen.goto(start_x, start_y - (_ * 100))
        pen.pendown()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    for _ in range(1, board_size):
        x, y = [int(_) for _ in screen.textinput("Input", "Input coordinates:").split(",")]
        pen.penup()
        pen.goto(x, y)
        pen.pendown()


if __name__ == '__main__':
    screen = turtle.Screen()
    main()
    screen.mainloop()

