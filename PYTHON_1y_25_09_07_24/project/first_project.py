import random
import time
import colorama
from colorama import Fore, Back, Style, init


def generate_board(size):
    return [[None for _ in range(size)] for _ in range(size)]


init(autoreset=True)
while True:
    board_size = int(input("Put your Board size ->   "))
    if board_size < 3:
        print("Please enter bigger than 3")
        continue
    board = generate_board(board_size)
    for element in line:
        print(end=" | ")
        [print(Fore.GREEN + element, end=" | ") for element in line]
        print()
    for line in board:
        print(line)
    for _ in range(board_size):
        while True:
            x = int(input("Put your coordinate X ->   ")) - 1
            y = int(input("Put your coordinate Y ->   ")) - 1
            if not board[x][y]:
                board[x][y] = "X"
                break
            else:
                print("This place is already busy.")
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if not board[x][y]:
                board[x][y] = "0"
                break
        for line in board:
            for element in line:
                print(end=" | ")
                match element:
                    case "X":
                        print(Fore.RED + element, end=" | ")
                    case "0":
                        print(Fore.BLUE + element, end=" | ")
                    case _:
                        print("-", end=" | ")
            print()
