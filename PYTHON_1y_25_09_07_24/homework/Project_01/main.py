import random
from colorama import Fore, Style
import pickle


board = [
    ["none", "none", "none"],
    ["none", "none", "none"],
    ["none", "none", "none"]
]

data = {
    "game_number": 0,
    "people_wins": 0,
    "people1_wins": 0,
    "people2_wins": 0,
    "ai_wins": 0,
    "draw": 0
}
while True:
    mod = str(input("Граєш проти друга чи проти пк?(Friend, PC) >>\t"))
    if(mod == "Friend" ):
        break
    elif(mod == "PC"):
        break
    else:
        print("Again. You chose wrong mod")
    
    

winner = ["player", "player1", "player2", "ai", "draw"]
final_winner = ""



def main(): 
    global loaded_data
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
        pass
        # for i in range(5):
        #     peopleGo()
        #     if endGame():
        #         break
        #     pcGo()
        #     if endGame():
        #         break
        #     print_board()
        #     if(pidkazku == "T"):
        #         pidkazka()  
        #     elif(pidkazku == "F"):
        #         print()
        #     else:
        #         print()

    game_stats()
    
    

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
    global loaded_data
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
                    print(f"Кінець гри, виграв: {winner[1]}")
                    final_winner = winner[1]
                    loaded_data["people_wins1"] += 1
                else:
                    print(f"Кінець гри, виграв: {winner[2]}")
                    final_winner = winner[2]
                    loaded_data["people_wins2"] += 1
                return True
            elif(mod == "PC"):
                if line[0] == f"{Fore.RED}X{Style.RESET_ALL}":
                    print(f"Кінець гри, виграв: {winner[0]}")
                    final_winner = winner[0]
                    loaded_data["people_wins"] += 1
                else:
                    print(f"Кінець гри, виграв: {winner[3]}")
                    final_winner = winner[3]
                    loaded_data["ai_wins"] += 1
                return True
    
    if all(cell != "none" for row in board for cell in row):
        print("Кінець гри, нічия")
        final_winner = winner[4]
        loaded_data["draw"] += 1
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



def game_stats():  
    global loaded_data
    loaded_data["game_number"] += 1    
    
    print(f"Games: {loaded_data["game_number"]}\n \tWHOLE STATISTIC \n ")

    for key, value in loaded_data.items():
        print(key, value)


with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

main()

with open('data.pkl', 'wb') as file:
        pickle.dump(loaded_data, file)