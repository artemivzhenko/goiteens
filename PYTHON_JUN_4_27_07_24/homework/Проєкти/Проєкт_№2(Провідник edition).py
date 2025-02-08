import os
import pygame
import random


pygame.init()
#Не чіпати!
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]



#Не чіпати!
pygame.mixer.init()
background_music = os.path.join("Music", "play.mp3")
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)



#Не чіпати!
TILE_SIZE = 40
WIDTH = len(maze[0]) * TILE_SIZE
HEIGHT = len(maze) * TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
wall_image = pygame.image.load("Wall_1.png")
player_image = pygame.image.load("images.png")
key_image = pygame.image.load("key.png")
door_image = pygame.image.load("door.jpg")
gameover = pygame.image.load("Gameover.jpg")
MMM_1 = pygame.image.load("MMM.jpg")
MMM_2 = pygame.transform.scale(MMM_1,(len(maze[0]) * TILE_SIZE, len(maze) * TILE_SIZE))
gameover = pygame.transform.scale(gameover,(len(maze[0]) * TILE_SIZE, len(maze) * TILE_SIZE))
wall_image = pygame.transform.scale(wall_image, (TILE_SIZE, TILE_SIZE))
player_image = pygame.transform.scale(player_image,(TILE_SIZE ,TILE_SIZE))
door_image = pygame.transform.scale(door_image,(TILE_SIZE ,TILE_SIZE))
key_image = pygame.transform.scale(key_image,(TILE_SIZE ,TILE_SIZE))

start_background = pygame.image.load("MMM.jpg")
start_background = pygame.transform.scale(start_background, (WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 75)
start_button_text = font.render("СТАРТ", True, (255, 255, 255))
start_button_rect = start_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))


def show_start_screen():
    waiting = True
    while waiting:
        screen.blit(start_background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), start_button_rect.inflate(20, 20))
        screen.blit(start_button_text, start_button_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    waiting = False

show_start_screen()


game_over_exit = pygame.mixer.Sound(os.path.join("Music","Gameover.mp3"))
game_over_exit_play = False


#Не чіпати!
collect_sound = pygame.mixer.Sound(os.path.join("Music", "Holdkey.mp3"))
collect_sound_play = False


#Не чіпати!
player_x, player_y = 1, 1
door_x, door_y = 3, 6
key_x, key_y = 5, 5


#Не чіпати?
x, y = 500, 200


#Не чіпати!
dragging = False


#Не чіпати!
has_key = False


#Не чіпати!
in_door = True

#Не чіпати!!!!
running = True
while running:
    keys = pygame.key.get_pressed()
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



    # Не чіпати!
    if player_x == key_x and player_y == key_y:
        has_key = True

        if not  collect_sound_play:
            collect_sound_play = True
            collect_sound.play()

    screen.fill((0, 0, 0))


    #Не чіпати!
    if (key_x,key_y) == (player_x,player_y):
        has_key = True
        maze[6][3] = 0


    #Не чіпати!
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            if maze[row][col] == 1:
                screen.blit(wall_image, (x, y))


    #Не чіпати!
    screen.blit(player_image, (player_x * TILE_SIZE, player_y * TILE_SIZE))
    screen.blit(door_image, (door_x * TILE_SIZE, door_y * TILE_SIZE))


    #Не чіпати!
    if not has_key:
        screen.blit(key_image,(key_y * TILE_SIZE, key_y * TILE_SIZE))
    pygame.display.flip()
    pygame.time.delay(60)



    #Не чіпати!
    if player_x == door_x and player_y == door_y and has_key:
        running = False
        if not game_over_exit_play:
            game_over_exit_play = True
            game_over_exit.play()
game_end = True
while game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = False
    screen.blit(gameover, (0, 0))
    pygame.display.flip()
    pygame.time.delay(60)

