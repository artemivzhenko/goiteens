game_number = 0
with open("game_number.txt", "r") as f:
    game_number = int(f.readline())
print(game_number)

# Game going on
game_number += 1

with open("game_number.txt", "w") as f:
    f.write(str(game_number))

