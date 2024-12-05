import pygame
import math
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Малювання спіралі")
start_x, start_y = 400, 300
color = (0, 255, 0)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    x, y = start_x, start_y
    length = 5
    angle = 0
    for i in range(200):
        end_x = x + length * math.cos(angle)
        end_y = y + length * math.sin(angle)
        pygame.draw.line(screen, color, (x, y), (end_x, end_y), 2)
        x, y = end_x, end_y
        angle += math.pi / 20
        length += 1
        time.sleep(1)
    pygame.display.flip()
    pygame.time.delay(50)
pygame.quit()
