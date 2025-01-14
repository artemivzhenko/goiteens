import pygame
# import sys
#
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Анімація простого об'єкта")
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# x = 0
# y = 300
# speed = 5
#
# clock = pygame.time.Clock()
# fps = 30
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     screen.fill(WHITE)
#
#     pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
#
#     x += speed
#     if x > 800:
#         x = -50
#     pygame.display.flip()
#
#     clock.tick(fps)
#     pygame.time.delay(10)


import pygame
import sys

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Циклічна анімація")

WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
color_index = 0

clock = pygame.time.Clock()
fps = 60

ANIMATION_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMATION_EVENT, 200)
animation_counter = 0
x = 200
y = 200
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == ANIMATION_EVENT:
            color_index = (color_index + 1) % len(colors)


    screen.fill(WHITE)
    pygame.draw.rect(screen, colors[color_index], (x, y, 100, 100))
    pygame.display.flip()
    clock.tick(fps)
