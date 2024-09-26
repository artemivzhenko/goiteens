from colorama import Fore, Back, Style, init
init(autoreset=True)
import random
import time
winner= None
hint= None
EMPTY = " "


while True:
    mode = int(input("Do you want play with (1-friend/2-bot): "))
    if mode != 1 and mode != 2:
        print("Incorrect, pleas try again")
        continue
    if mode == 1:
        size = int(input("Enter a field size from 3 to 6: "))
        if size >= 3 and size <= 6:
            None
        else:
            print("Incorrect, pleas try again")
            continue
    if mode == 1:
        player_1_name=input("What is your name: ")
        player_2_name = input("What is name of your friend: ")

    if mode == 2:
        hint = int(input("Do you want play with hint (1-yes/2-no): "))
        if hint != 1 and hint != 2:
            print("Incorrect, pleas try again")
            continue
        size = int(input("Enter a field size from 3 to 6: "))
        if size >= 3 and size <= 6:
            None
        else:
            print("Incorrect, pleas try again")
            continue
    if mode == 1:
        user_1 = int(input(f"{player_1_name} choose your symbol (1-X/2-0): "))
        if user_1 != 1 and user_1 != 2:
            print("Incorrect, pleas try again")
            continue

    board=[]
    for i in range(size):
        item= [" "] * size
        board.append(item)



    if mode == 2:
        while True:
            while True:
                x = int(input("Put your coordinate X -> ")) - 1
                y = int(input("Put your coordinate Y -> ")) - 1
                if x >= size or y >= size:
                    print("incorrect coordinates")
                else:
                    break
            board[x][y] = Fore.RED + "X"
            time.sleep(1)

            bot_x = random.randint(0, size -1)
            bot_y = random.randint(0, size -1)

            while board[bot_x][bot_y] != " ":
                bot_x = random.randint(0, size -1)
                bot_y = random.randint(0, size -1)

            board[bot_x][bot_y] = Fore.BLUE + "0"
            for line in board:
                if size == 3:
                    print(line[0], '|', line[1], '|', line[2])
                    print("---------")
                elif size == 4:
                    print(line[0], '|', line[1], '|', line[2], '|', line[3])
                    print("-------------")
                elif size == 5:
                    print(line[0], '|', line[1], '|', line[2], '|', line[3], '|', line[4])
                    print("------------------")
                elif size == 6:
                    print(line[0], '|', line[1], '|', line[2], '|', line[3], '|', line[4], '|', line[5])
                    print("----------------------")




            if hint == 1:
                hint_given = False
                for i in range(size):
                    if board[i].count(Fore.RED + "X") == size - 1 and board[i].count(EMPTY) == 1:
                        empty_index = board[i].index(EMPTY)
                        print(f"You can put {"X"} on the coordinates: (X={i + 1} and Y= {empty_index + 1})")
                        hint_given = True
                        break

                if not hint_given:
                    for i in range(size):
                        col = [board[j][i] for j in range(size)]
                        if col.count(Fore.RED + "X") == size - 1 and col.count(EMPTY) == 1:
                            empty_index = col.index(EMPTY)
                            print(f"You can put {"X"} on the coordinates: (X={empty_index + 1} and Y={i + 1})")
                            hint_given = True
                            break

                if not hint_given:
                    main_diag = [board[i][i] for i in range(size)]
                    if main_diag.count(Fore.RED + "X") == size - 1 and main_diag.count(EMPTY) == 1:
                        empty_index = main_diag.index(EMPTY)
                        print(f"You can put {"X"} on the coordinates: (X={empty_index + 1} and Y={empty_index + 1})")
                        hint_given = True

                    anti_diag = [board[i][size - 1 - i] for i in range(size)]
                    if anti_diag.count(Fore.RED + "X") == size - 1 and anti_diag.count(EMPTY) == 1:
                        empty_index = anti_diag.index(EMPTY)
                        print(f"You can put {"X"} on the coordinates: (X={empty_index + 1} and Y={size - empty_index})")
                        hint_given = True

            winner = False
            for i in range(size):
                if all(cell == Fore.RED + "X" for cell in board[i]) or all(board[j][i] == Fore.RED + "X" for j in range(size)):
                    winner = True
                    break

            if all(board[i][i] == Fore.RED + "X" for i in range(size)) or all(
                    board[i][size - 1 - i] == Fore.RED + "X" for i in range(size)):
                winner = True

            if winner:
                print("player is winner!")
                break

            if all(cell != EMPTY for row in board for cell in row):
                print("Draw!")
                break

    if mode == 1:
        if user_1 == 1:
            player_1 = Fore.RED + "X"
        else:
            player_1 = Fore.BLUE + "0"

        if player_1 == Fore.RED + "X":
            player_2 = Fore.BLUE + "0"
        else:
            player_2 = Fore.RED + "X"

        print(f"Then {player_2_name} will be {player_2}")
        while True:
            while True:
                player_1_x = int(input(f"{player_1_name} put your coordinate X -> ")) - 1
                player_1_y = int(input(f"{player_1_name} put your coordinate Y -> ")) - 1
                if player_1_x >= size or player_1_y >= size:
                    print("incorrect coordinates")
                else:
                    break

            board[player_1_x][player_1_y] = player_1

            for line in board:
                if size == 3:
                    print(line[0], '|', line[1], '|', line[2])
                    print("---------")
                elif size == 4:
                    print(line[0], '|', line[1], '|', line[2], '|', line[3])
                    print("-------------")
                elif size == 5:
                    print(line[0], '|', line[1], '|', line[2], '|', line[3], '|', line[4])
                    print("------------------")
                elif size == 6:
                    print(line[0], '|', line[1], '|', line[2], '|', line[3], '|', line[4], '|', line[5])
                    print("----------------------")

            while True:
                player_2_x = int(input(f"{player_2_name} put your coordinate X -> ")) - 1
                player_2_y = int(input(f"{player_2_name} put your coordinate Y -> ")) - 1
                if player_2_x >= size or player_2_y >= size:
                    print("incorrect coordinates")
                else:
                    break

            board[player_2_x][player_2_y] = player_2

            for line in board:
                if size == 3:
                    print(line[0], '|', line[1], '|', line[2])
                    print("---------")
                elif size == 4:
                    print(line[0], '|', line[1], '|', line[2], '|', line[3])
                    print("-------------")
                elif size == 5:
                    print(line[0], '|', line[1], '|', line[2], '|', line[3], '|', line[4])
                    print("------------------")
                elif size == 6:
                    print(line[0], '|', line[1], '|', line[2], '|', line[3], '|', line[4], '|', line[5])
                    print("----------------------")

            winner = 0
            for i in range(size):
                if all(cell == player_1 for cell in board[i]) or all(
                        board[j][i] == player_1 for j in range(size)):
                    winner = 1
                    break

            if all(board[i][i] == player_1 for i in range(size)) or all(
                    board[i][size - 1 - i] == player_1 for i in range(size)):
                winner = 1

            for i in range(size):
                if all(cell == player_2 for cell in board[i]) or all(
                        board[j][i] == player_2 for j in range(size)):
                    winner = 2
                    break

            if all(board[i][i] == player_2 for i in range(size)) or all(
                    board[i][size - 1 - i] == player_2 for i in range(size)):
                winner = 2

            if winner == 1:
                print(f"{player_1_name} is winner!")
                exit()
            elif winner == 2:
                print(f"{player_2_name} is winner!")
                exit()


            if all(cell != EMPTY for row in board for cell in row):
                print("Draw!")
                exit()





