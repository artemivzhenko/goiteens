import random
import time
import os
from colorama import Fore, init

init(autoreset=True)


def print_board(board):
    for line in board:
        for cell in line:
            if cell == "X":
                print(Fore.BLUE + "X", end=" ")
            elif cell == 0:
                print(Fore.MAGENTA + "0", end=" ")
            else:
                print("-", end=" ")
        print()


def check_winner(board):
    win_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for combination in win_combinations:
        values = [board[x][y] for x, y in combination]
        if values == ["X", "X", "X"]:
            return "людина"
        if values == [0, 0, 0]:
            return "робот"

    if all(cell is not None for row in board for cell in row):
        return "нічия"

    return None


def player_move(board):
    try:
        x = int(input("Координата x -> \n ")) - 1
        y = int(input("Координата y -> \n ")) - 1
        if board[x][y] is None:
            board[x][y] = "X"
        else:
            print("Неможливо поставити на цю клітинку")
            player_move(board)
    except (IndexError, ValueError):
        print("Неправильні координати! Спробуйте знову.")
        player_move(board)


def computer_move(board):
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] is None:
            board[x][y] = 0
            break


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_stats(player_score, computer_score, draw_score):
    with open('game_stats.txt', 'a') as file:
        file.write(f"Man: {player_score}, Computer: {computer_score}, Draw: {draw_score}\n")


def game():
    player_score = 0
    computer_score = 0
    draw_score = 0

    while True:
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        while True:
            clear_console()
            print_board(board)
            time.sleep(1)

            player_move(board)
            winner = check_winner(board)
            if winner:
                break

            computer_move(board)
            winner = check_winner(board)
            if winner:
                break

        clear_console()
        print_board(board)

        if winner == "людина":
            print("Ви перемогли!")
            player_score += 1
        elif winner == "робот":
            print("Комп'ютер переміг!")
            computer_score += 1
        elif winner == "нічия":
            print("Нічия!")
            draw_score += 1

        print(f"Рахунок: Людина {player_score} - Робот {computer_score} - Нічия {draw_score}")

        save_stats(player_score, computer_score, draw_score)

        while True:
            cont = input("Бажаєте продовжити гру? (так/ні): \n").lower()
            if cont in ["так", "ні"]:
                break
            else:
                print("Некоректно введені дані. Спробуйте ще раз.")

        if cont == "ні":
            print("Гра завершена.")
            break


game()
