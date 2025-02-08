import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Спіраль")

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
color_index = 0

x_center = 320
y_center = 240
angle = 0
radius = 5
angle_step = 5
radius_step = 1
color_change_step = 10
steps = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for i in range(0, angle, angle_step):
        x = x_center + int(radius * math.cos(math.radians(i)))
        y = y_center + int(radius * math.sin(math.radians(i)))
        pygame.draw.circle(screen, colors[color_index], (x, y), 2)

        radius += radius_step
        steps += 1
        if steps % color_change_step == 0:
            color_index = (color_index + 1) % len(colors)

    angle += angle_step
    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
