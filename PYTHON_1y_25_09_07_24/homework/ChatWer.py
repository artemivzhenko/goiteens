import random
from colorama import Fore, Style

board = [
    ["none", "none", "none"],
    ["none", "none", "none"],
    ["none", "none", "none"]
]
mod = str(input("Граєш проти друга чи проти пк?(Friend, PC) >>\t"))
def main():
    
    if(mod == "Friend"):
        for i in range(5):
            peopleGo()
            if endGame():
                break
            print_board()
            peopleGo1()
            if endGame():
                break
            print_board()
    elif(mod == "PC"):
        pidkazku = str(input("Граємо з підказками чи без?(T,F) >>\t"))
        for i in range(5):
            peopleGo()
            if endGame():
                break
            pcGo()
            if endGame():
                break
            print_board()
            if(pidkazku == "T"):
                pidkazka()  
            elif(pidkazku == "F"):
                print()
            else:
                print()
    else:
        for i in range(5):
            peopleGo()
            if endGame():
                break
            pcGo()
            if endGame():
                break
            print_board()
            if(pidkazku == "T"):
                pidkazka()  
            elif(pidkazku == "F"):
                print()
            else:
                print()
    

def peopleGo1():
    squareTo = [None, None]
    squareIs = ["рядок", "колонка"]
    while True:
        try:
            for i in range(2):
                squareTo[i] = int(input(f"Введіть {squareIs[i]}(від 0 до 2): "))
            if (0 <= squareTo[0] <= 2) and (0 <= squareTo[1] <= 2):
                if board[squareTo[0]][squareTo[1]] == "none":
                    board[squareTo[0]][squareTo[1]] = f"{Fore.GREEN}O{Style.RESET_ALL}"
                    break
                else:
                    print("Це місце вже зайняте.")
            else:
                print("Неправильний діапазон, спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, введіть число від 0 до 2.")

def peopleGo():
    squareTo = [None, None]
    squareIs = ["рядок", "колонка"]
    while True:
        try:
            for i in range(2):
                squareTo[i] = int(input(f"Введіть {squareIs[i]}(від 0 до 2): "))
            if (0 <= squareTo[0] <= 2) and (0 <= squareTo[1] <= 2):
                if board[squareTo[0]][squareTo[1]] == "none":
                    board[squareTo[0]][squareTo[1]] = f"{Fore.RED}X{Style.RESET_ALL}"
                    break
                else:
                    print("Це місце вже зайняте.")
            else:
                print("Неправильний діапазон, спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, введіть число від 0 до 2.")

def pcGo():
    while True:
        squareTo = [random.randint(0, 2) for _ in range(2)]
        if board[squareTo[0]][squareTo[1]] == "none":
            board[squareTo[0]][squareTo[1]] = f"{Fore.GREEN}O{Style.RESET_ALL}"
            break

def print_board():
    for row in board:
        print("\t | \t".join(row))
    print()  

def endGame():
    lines = [
        board[0], board[1], board[2],
        [board[0][0], board[1][0], board[2][0]], 
        [board[0][1], board[1][1], board[2][1]], 
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]], 
        [board[0][2], board[1][1], board[2][0]] 
    ]
    
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != "none":
            if(mod == "Friend"):     
                if line[0] == f"{Fore.GREEN}O{Style.RESET_ALL}":
                    print("Кінець гри, виграв: гравець 1")
                else:
                    print("Кінець гри, виграв: гравець")
                return True
            elif(mod == "PC"):
                if line[0] == f"{Fore.RED}X{Style.RESET_ALL}":
                    print("Кінець гри, виграв: гравець")
                else:
                    print("Кінець гри, виграв: AI")
    
    if all(cell != "none" for row in board for cell in row):
        print("Кінець гри, нічия")
        return True
    
    return False

def pidkazka():
    winLines = [
        [board[0][0], board[0][1], (0, 2)], 
        [board[1][0], board[1][1], (1, 2)], 
        [board[2][0], board[2][1], (2, 2)],
        [board[0][0], board[1][0], (2, 0)], 
        [board[0][1], board[1][1], (2, 1)], 
        [board[0][2], board[1][2], (2, 2)],
        [board[0][0], board[1][1], (2, 2)], 
        [board[0][2], board[1][1], (2, 0)]
    ]

    for line in winLines:
        if line[0] == line[1] and line[0] != "none" and board[line[2][0]][line[2][1]] == "none":
            print(f"Підказка: йдіть до board{line[2]}")  # Підказка для виграшу
            return
    print("Немає підказок.")

main()
