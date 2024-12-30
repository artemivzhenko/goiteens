import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Моя перша гра")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

font = pygame.font.Font(None, 74)
text = font.render("Привіт, Pygame!", True, WHITE)
text_rect = text.get_rect(center=(320, 240))

square_x = 0
square_y = 220
square_speed = 5

circles = []
for _ in range(5):
    x = random.randint(50, 590)
    y = random.randint(50, 430)
    radius = 20
    dx = random.choice([-5, 5])
    dy = random.choice([-5, 5])
    color = [random.randint(0, 255) for _ in range(3)]
    circles.append([x, y, radius, dx, dy, color])


x, y = 50, 50
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    square_x += square_speed
    if square_x > 640:
        square_x = -50

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed

    for circle in circles:
        circle[0] += circle[3]
        circle[1] += circle[4]

        if circle[0] - circle[2] < 0 or circle[0] + circle[2] > 640:
            circle[3] = -circle[3]
        if circle[1] - circle[2] < 0 or circle[1] + circle[2] > 480:
            circle[4] = -circle[4]

    screen.fill(RED)
    screen.blit(text, text_rect)
    pygame.draw.rect(screen, BLUE, (square_x, square_y, 50, 50))

    for circle in circles:
        pygame.draw.circle(screen, circle[5], (circle[0], circle[1]), circle[2])

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
