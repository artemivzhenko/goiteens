import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Гра з фоновим зображенням")

background = pygame.image.load("background.jpg")

num_objects = 5
objects = []
for i in range(num_objects):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    speed_x = random.choice([-3, -2, -1, 1, 2, 3])
    speed_y = random.choice([-3, -2, -1, 1, 2, 3])
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    radius = random.randint(10, 30)
    objects.append({'x': x, 'y': y, 'speed_x': speed_x, 'speed_y': speed_y, 'color': color, 'radius': radius})


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    for obj in objects:
        obj['x'] += obj['speed_x']
        obj['y'] += obj['speed_y']


        if obj['x'] - obj['radius'] <= 0 or obj['x'] + obj['radius'] >= 800:
            obj['speed_x'] *= -1
        if obj['y'] - obj['radius'] <= 0 or obj['y'] + obj['radius'] >= 600:
            obj['speed_y'] *= -1

    screen.blit(background, (0, 0))

    for obj in objects:
        pygame.draw.circle(screen, obj['color'], (obj['x'], obj['y']), obj['radius'])

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
