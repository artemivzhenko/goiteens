import pygame
import random


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Анімація кіл")

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

num_circles = 5
circles = []
for i in range(num_circles):
    radius = random.randint(20, 30)
    x = random.randint(radius, 640 - radius)
    y = random.randint(radius, 480 - radius)
    speed_x = random.choice([-3, -2, -1, 1, 2, 3])
    speed_y = random.choice([-3, -2, -1, 1, 2, 3])
    color = random.choice(colors)
    circles.append({'x': x, 'y': y, 'radius': radius, 'speed_x': speed_x, 'speed_y': speed_y, 'color': color})


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for circle in circles:
        circle['x'] += circle['speed_x']
        circle['y'] += circle['speed_y']

        if circle['x'] - circle['radius'] <= 0 or circle['x'] + circle['radius'] >= 640:
            circle['speed_x'] *= -1
        if circle['y'] - circle['radius'] <= 0 or circle['y'] + circle['radius'] >= 480:
            circle['speed_y'] *= -1

    screen.fill((0, 0, 0))

    for circle in circles:
        pygame.draw.circle(screen, circle['color'], (circle['x'], circle['y']), circle['radius'])

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()

