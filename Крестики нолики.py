import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all([spot != " " for row in board for spot in row])

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in [1, 2, 3]:
                return value - 1
            else:
                print("Недопустимый ввод. Введите число от 1 до 3.")
        except ValueError:
            print("Недопустимый ввод. Введите число от 1 до 3.")

def get_ai_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(available_moves)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    is_ai = input("Хотите играть против ИИ? (да/нет): ").lower() == "да"

    while True:
        print_board(board)

        if current_player == "X":
            row = get_valid_input(f"Игрок {current_player}, введите номер строки (1-3): ")
            col = get_valid_input(f"Игрок {current_player}, введите номер столбца (1-3): ")
        else:
            if is_ai:
                print("Ход ИИ...")
                row, col = get_ai_move(board)
            else:
                row = get_valid_input(f"Игрок {current_player}, введите номер столбца (1-3): ")
                col = get_valid_input(f"Игрок {current_player}, введите номер строки (1-3): ")

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Эта клетка уже занята! Попробуйте снова.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            break
        elif is_draw(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
