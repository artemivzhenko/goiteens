import pygame
import os


pygame.init()


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

pygame.init()

TILE_SIZE = 40
WIDTH = len(maze[0]) * TILE_SIZE
HEIGHT = len(maze) * TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = pygame.image.load("game_over.png")
game_over = pygame.transform.scale(game_over, (len(maze[0]) * TILE_SIZE, len(maze) * TILE_SIZE))

wall_image = pygame.image.load("wall.png")
wall_image = pygame.transform.scale(wall_image, (TILE_SIZE, TILE_SIZE))

player_image = pygame.image.load("bugsbunny.jpg")
player_image = pygame.transform.scale(player_image, (TILE_SIZE, TILE_SIZE))

key_image = pygame.image.load("key.png")
key_image = pygame.transform.scale(key_image, (TILE_SIZE, TILE_SIZE))

door_image = pygame.image.load("door.png")
door_image = pygame.transform.scale(door_image, (TILE_SIZE, TILE_SIZE))

pygame.mixer.init()
exit_sound = pygame.mixer.Sound(os.path.join("assets", "game-start.mp3"))
collect_sound = pygame.mixer.Sound(os.path.join("assets", "game-character.mp3"))
collect_sound.play()

background_music = os.path.join("assets", "game-loop.mp3")
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)


player_x, player_y = 1, 1
door_x, door_y = 1, 8
key_x, key_y = 17, 1

has_key = False
show_door = True
game_over_call = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and maze[player_y - 1][player_x] == 0:
                player_y -= 1
            elif event.key == pygame.K_DOWN and maze[player_y + 1][player_x] == 0:
                player_y += 1
            elif event.key == pygame.K_LEFT and maze[player_y][player_x - 1] == 0:
                player_x -= 1
            elif event.key == pygame.K_RIGHT and maze[player_y][player_x + 1] == 0:
                player_x += 1

    screen.fill((0, 0, 0))
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            if maze[row][col] == 1:
                screen.blit(wall_image, (x, y))

    if (key_x, key_y) == (player_x, player_y):
        collect_sound.play()
        has_key = True
        maze[8][1] = 0

    screen.blit(player_image, (player_x * TILE_SIZE, player_y * TILE_SIZE))
    screen.blit(door_image, (door_x * TILE_SIZE, door_y * TILE_SIZE))
    if (door_x, door_y) == (player_x, player_y) and has_key:
        show_door = False
        screen.blit(game_over, (0, 0))
        if not game_over_call:
            exit_sound.play()
            game_over_call = True
    if not has_key:
        screen.blit(key_image, (key_x * TILE_SIZE, key_y * TILE_SIZE))
    pygame.display.flip()
    pygame.time.delay(60)
