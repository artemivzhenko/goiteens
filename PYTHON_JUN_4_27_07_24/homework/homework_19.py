import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))

x, y = 320, 240
radius = 30
color = (255, 0, 0)
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x - radius > 0:
        x -= speed
    if keys[pygame.K_d] and x + radius < 640:
        x += speed
    if keys[pygame.K_w] and y - radius > 0:
        y -= speed
    if keys[pygame.K_s] and y + radius < 480:
        y += speed

    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.draw.circle(screen, (0, 0, 255), (mouse_x, mouse_y), radius, 1)
    pygame.display.flip()

pygame.quit()
