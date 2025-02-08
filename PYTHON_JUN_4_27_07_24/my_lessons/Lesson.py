import pygame
import random

# Ініціалізація Pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Green to Red Cubes")

# Налаштування кольорів
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Налаштування розміру кубика
CUBE_SIZE = 50

# Генерація випадкових координат для кубиків
cubes = []
for _ in range(10):
    x = random.randint(0, 800 - CUBE_SIZE)
    y = random.randint(0, 800 - CUBE_SIZE)
    cubes.append(pygame.Rect(x, y, CUBE_SIZE, CUBE_SIZE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Очищення екрану

    for cube in cubes:
        pygame.draw.rect(screen, GREEN, cube)

    for i in range(len(cubes)):
        for j in range(i + 1, len(cubes)):
            if cubes[i].colliderect(cubes[j]):
                pygame.draw.rect(screen, RED, cubes[i])
                pygame.draw.rect(screen, RED, cubes[j])

    pygame.display.flip()  # Оновлення екрану
    pygame.time.delay(30)

pygame.quit()

