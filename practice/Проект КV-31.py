import random
import json
from colorama import Fore, Style, init

init(autoreset=True)

def print_board(board):
    for row in board:
        print("|".join([Fore.RED + spot if spot == "X" else Fore.GREEN + spot if spot == "O" else spot for spot in row]))
        print("-" * (len(board) * 2 - 1))

def check_winner(board, player):
    size = len(board)
    for i in range(size):
        if all([spot == player for spot in board[i]]) or all([board[j][i] == player for j in range(size)]):
            return True
    if all([board[i][i] == player for i in range(size)]) or all([board[i][size - 1 - i] == player for i in range(size)]):
        return True
    return False

def is_draw(board):
    return all([spot != " " for row in board for spot in row])

def get_valid_input(prompt, size):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= size:
                return value - 1
            else:
                print(f"Недопустимый ввод. Введите число от 1 до {size}.")
        except ValueError:
            print(f"Недопустимый ввод. Введите число от 1 до {size}.")

def get_ai_move(board, difficulty):
    available_moves = [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == " "]
    if difficulty == "легкий":
        return random.choice(available_moves)
    elif difficulty == "средний":
        for move in available_moves:
            board[move[0]][move[1]] = "X"
            if check_winner(board, "X"):
                board[move[0]][move[1]] = " "
                return move
            board[move[0]][move[1]] = " "
        return random.choice(available_moves)
    else:
        for move in available_moves:
            board[move[0]][move[1]] = "O"
            if check_winner(board, "O"):
                return move
            board[move[0]][move[1]] = " "
        for move in available_moves:
            board[move[0]][move[1]] = "X"
            if check_winner(board, "X"):
                board[move[0]][move[1]] = " "
                return move
            board[move[0]][move[1]] = " "
        return random.choice(available_moves)

def provide_hint(board):
    available_moves = [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == " "]
    return random.choice(available_moves)

def save_game_result(winner, board_size):
    results = {"Размер поля": board_size, "Победитель": winner}
    try:
        with open("game_results.json", "a") as file:
            json.dump(results, file)
            file.write("\n")
    except Exception as e:
        print(f"Ошибка при сохранении результатов: {e}")

def show_statistics():
    try:
        with open("game_results.json", "r") as file:
            games = file.readlines()
            print(f"Всего игр: {len(games)}")
            for game in games:
                result = json.loads(game)
                print(f"Размер поля: {result['Размер поля']}, Победитель: {result['Победитель']}")
    except FileNotFoundError:
        print("Нет сохранённых результатов.")
    except Exception as e:
        print(f"Ошибка при чтении результатов: {e}")

def tic_tac_toe(board_size, difficulty, show_hint):
    board = [[" " for _ in range(board_size)] for _ in range(board_size)]
    current_player = "X"
    is_ai = input("Хотите играть против ИИ? (да/нет): ").lower() == "да"

    while True:
        print_board(board)

        if current_player == "X":
            row = get_valid_input(f"Игрок {current_player}, введите номер строки (1-{board_size}): ", board_size)
            col = get_valid_input(f"Игрок {current_player}, введите номер столбца (1-{board_size}): ", board_size)
        else:
            if is_ai:
                print("Ход ИИ...")
                row, col = get_ai_move(board, difficulty)
            else:
                row = get_valid_input(f"Игрок {current_player}, введите номер строки (1-{board_size}): ", board_size)
                col = get_valid_input(f"Игрок {current_player}, введите номер столбца (1-{board_size}): ", board_size)

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Эта клетка уже занята! Попробуйте снова.")
            continue

        if show_hint and current_player == "X":
            hint_row, hint_col = provide_hint(board)
            print(f"Подсказка: попробуйте поставить на клетку ({hint_row + 1}, {hint_col + 1})")

        if check_winner(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            save_game_result(current_player, board_size)
            break
        elif is_draw(board):
            print_board(board)
            print("Ничья!")
            save_game_result("Ничья", board_size)
            break

        current_player = "O" if current_player == "X" else "X"

    if input("Хотите посмотреть статистику игр? (да/нет): ").lower() == "да":
        show_statistics()

def show_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Начать игру")
        print("2. Настройки")
        print("3. Выход")

        choice = input("Выберите опцию (1-3): ").strip()

        if choice == "1":
            board_size = int(input("Выберите размер поля (3х3, 4х4, 5х5): ").strip()[0])
            difficulty = None
            show_hint = input("Хотите включить подсказки? (да/нет): ").lower() == "да"
            if input("Хотите играть против ИИ? (да/нет): ").lower() == "да":
                difficulty = input("Выберите уровень сложности (легкий, средний, трудный): ").lower()
            tic_tac_toe(board_size, difficulty, show_hint)
        elif choice == "2":
            print("\nНастройки:")
            print("1. Статистика")
            print("2. Подсказки")
            settings_choice = input("Выберите опцию (1-2): ").strip()
            if settings_choice == "1":
                show_statistics()
            elif settings_choice == "2":
                print("Подсказки: Включены/Отключены")
            else:
                print("Некорректный выбор.")
        elif choice == "3":
            print("Выход из игры.")
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    show_menu()
