import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
coordinates_list = []
for i in range(10):
    coordinates_list.append((random.randint(0, 800), random.randint(0, 800)))

wall = pygame.image.load("photo_2024-12-21_13-20-05.jpg")
wall1 = pygame.transform.scale(wall, (50, 800))
wall2 = pygame.transform.scale(wall, (800, 50))
wall = pygame.transform.scale(wall, (50, 50))
alpha = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    alpha += 5
    if alpha > 255:
        alpha = 0
    screen.fill((0, 0, 0))
    for i in range(0, 16):
        screen.blit(wall, (0, 50*i))
        screen.blit(wall, (50*i, 0))
    pygame.display.flip()
    pygame.time.delay(30)