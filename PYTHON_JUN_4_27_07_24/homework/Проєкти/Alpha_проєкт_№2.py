import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
coordinates_list = []
for i in range(10):
    coordinates_list.append((random.randint(0, 800), random.randint(0, 800)))

wall = pygame.image.load("Wall.png")
wall1 = pygame.transform.scale(wall, (50, 800))
wall2 = pygame.transform.scale(wall, (800, 150))
wall = pygame.transform.scale(wall, (50, 50))
wall_2 = pygame.transform.scale(wall, (100,100))
alpha = 0



pygame.display.set_caption("Проста анімація квадрата")

character_image = pygame.image.load("images.png")
character_image = pygame.transform.scale(character_image, (100, 100))
static_square = pygame.Rect(50, 250, 100, 100)
static_square_color = (0, 128, 255)
x, y = 500, 200
speed = 25
dragging = False
color = (0, 0, 200)
game_is_running = True
offset_x = 0
offset_y = 0
while game_is_running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
        elif event.type == pygame.KEYDOWN:
            move_buttons = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE]
            if event.key in move_buttons:
                match event.key:
                    case pygame.K_LEFT:
                        x -= speed
                    case pygame.K_RIGHT:
                        x += speed
                    case pygame.K_UP:
                        y -= speed
                    case pygame.K_DOWN:
                        y += speed
                    case pygame.K_SPACE:
                        x, y = 400, 400
    screen.fill((0, 0, 0))
    for i in range(0, 20):
        screen.blit(wall, (0, 50 * i))
        screen.blit(wall, (50 * i, 0))
    for a in range(3, 13):
        screen.blit(wall, (50 * a , 100))
        screen.blit(wall , (50 * a , 400))
    for g in range(3,4):
        screen.blit(wall , (150 , 50 * g))
        screen.blit(wall,(400 ,50 * g ))
    for f in range(7, 11):
        screen.blit(wall,(150,50 * f))
        screen.blit(wall, (350, 50 * f))
    for n in range(3, 17):
            screen.blit(wall, (50 * n, 700))
    for p in range(0, 17):
        screen.blit(wall, (50 * p, 850))
    for u in range(0,15):
        screen.blit(wall, (600, 50 * u))
    for h in range(0, 15):
        screen.blit(wall, (600, 50 * h))
    for j in range(3, 20):
        screen.blit(wall, (950, 50 * j))
    for k in range(15, 20):
        screen.blit(wall, (50 * k, 500))
    for klj in range(15, 20):
        screen.blit(wall, (50 * klj, 150))
    for kl in range(12, 17):
        screen.blit(wall, (50 * kl, 300))
    for z in range(3,13):
        screen.blit(wall, (50 * z, 50))
        screen.blit(wall, (50 * z, 350))


    screen.blit(character_image, (x, y))
    pygame.display.flip()


pygame.display.flip()
pygame.time.delay(30)