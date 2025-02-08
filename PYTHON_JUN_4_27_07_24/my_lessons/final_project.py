import pygame
import os
import json

pygame.init()

def load_maze(string_maze):
    maze_from_file = []
    maze_file = string_maze.split('\n')
    for line in maze_file:
        maze_line = [int(x) for x in line.split(",")]
        maze_from_file.append(maze_line)
    return maze_from_file

def get_labyrinth_files():
    return [f for f in os.listdir("labirints") if f.endswith(".json")]


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

start_background = pygame.image.load("img.png")
start_background = pygame.transform.scale(start_background, (WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 75)
small_font = pygame.font.SysFont(None, 40)
start_button_text = font.render("СТАРТ", True, (255, 255, 255))
start_button_rect = start_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

labyrinth_files = get_labyrinth_files()
selected_labyrinth = labyrinth_files[0] if labyrinth_files else None


def show_start_screen():
    global selected_labyrinth
    dropdown_open = False
    dropdown_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 40)

    while True:
        screen.blit(start_background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), start_button_rect.inflate(20, 20))
        screen.blit(start_button_text, start_button_rect)

        pygame.draw.rect(screen, (50, 50, 50), dropdown_rect)
        selected_text = small_font.render(selected_labyrinth or "No files", True, (255, 255, 255))
        screen.blit(selected_text, (dropdown_rect.x + 5, dropdown_rect.y + 5))

        if dropdown_open:
            for i, file in enumerate(labyrinth_files):
                item_rect = pygame.Rect(dropdown_rect.x, dropdown_rect.y + (i + 1) * 40, 200, 40)
                pygame.draw.rect(screen, (70, 70, 70), item_rect)
                item_text = small_font.render(file, True, (255, 255, 255))
                screen.blit(item_text, (item_rect.x + 5, item_rect.y + 5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return selected_labyrinth
                if dropdown_rect.collidepoint(event.pos):
                    dropdown_open = not dropdown_open
                elif dropdown_open:
                    for i, file in enumerate(labyrinth_files):
                        item_rect = pygame.Rect(dropdown_rect.x, dropdown_rect.y + (i + 1) * 40, 200, 40)
                        if item_rect.collidepoint(event.pos):
                            selected_labyrinth = file
                            dropdown_open = False


selected_file = show_start_screen()


with open(os.path.join("labirints", selected_file), 'r') as file:
    maze_json = json.load(file)


player_x, player_y = maze_json["player"]
door_x_1, door_y_1 = maze_json["door"]
key_x, key_y = maze_json["key"]
maze = load_maze(maze_json["maze"])
TILE_SIZE = maze_json["TILE_SIZE"]
WIDTH = len(maze[0]) * TILE_SIZE
HEIGHT = len(maze) * TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.init()
background_music = os.path.join("musics", "cool-hip-hop-loop-275527.mp3")
collect_sound = pygame.mixer.Sound(os.path.join("musics", "game-bonus-144751 (1).mp3"))
end_sound = pygame.mixer.Sound(os.path.join("musics", "game-over-classic-206486.mp3"))
key_music_play = False
end_music_play = False
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)


start_background = pygame.image.load("img.png")
start_background = pygame.transform.scale(start_background, (WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 75)
start_button_text = font.render("Start", True, (255, 0, 162))
start_button_rect = start_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))


game_over_image = pygame.image.load("game_over.png")
game_over_image = pygame.transform.scale(game_over_image, (len(maze[0]) * TILE_SIZE, len(maze) * TILE_SIZE))

wall_image = pygame.image.load("wall.png")
wall_image = pygame.transform.scale(wall_image, (TILE_SIZE, TILE_SIZE))

player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (TILE_SIZE, TILE_SIZE))

key_image = pygame.image.load("key.png")
key_image = pygame.transform.scale(key_image, (TILE_SIZE, TILE_SIZE))

door_image = pygame.image.load("door.png")
door_image = pygame.transform.scale(door_image, (TILE_SIZE, TILE_SIZE))


has_key = False
key_music = False
door_music_play = False
game_end = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and maze[player_y - 1][player_x] == 0:
                player_y -= 1
            elif event.key == pygame.K_s and maze[player_y + 1][player_x] == 0:
                player_y += 1
            elif event.key == pygame.K_a and maze[player_y][player_x - 1] == 0:
                player_x -= 1
            elif event.key == pygame.K_d and maze[player_y][player_x + 1] == 0:
                player_x += 1
    if player_x == key_x and player_y == key_y:
        has_key = True
        if not key_music_play:
            key_music_play = True
            collect_sound.play()
        maze[door_y_1][door_x_1] = 0
    if player_x == door_x_1 and player_y == door_y_1 and has_key:
        show_door = False
        running = False
    screen.fill((255, 255, 255))
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            if maze[row][col] == 1:
                screen.blit(wall_image, (x, y))

    screen.blit(player_image, (player_x * TILE_SIZE, player_y * TILE_SIZE))
    screen.blit(door_image, (door_x_1 * TILE_SIZE, door_y_1 * TILE_SIZE))
    if not has_key:
        screen.blit(key_image, (key_x * TILE_SIZE, key_y * TILE_SIZE))
    pygame.display.flip()
    pygame.time.delay(60)

    if (door_x_1, door_y_1) == (player_x, player_y) and has_key:
        running = False
        if not door_music_play:
            door_music_play = True
            end_sound.play()
game_end = True
while game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = False

    screen.blit(game_over_image, (0, 0))
    pygame.display.flip()
    pygame.time.delay(60)