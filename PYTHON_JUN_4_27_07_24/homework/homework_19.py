import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Виконання завдань")

rectangles = [
    ((50, 50), (100, 200), (255, 0, 0)),
    ((200, 150), (150, 100), (0, 255, 0)),
    ((400, 300), (200, 150), (0, 0, 255)),
    ((600, 400), (120, 160), (255, 255, 0))
]

circle_color = (0, 255, 255)
circle_pos = (400, 300)
circle_radius = 50

sprite = pygame.image.load("sprite.png")
sprite_rect = sprite.get_rect()
sprite_rect.topleft = (50, 50)

line_color = (0, 0, 255)
line_thickness = 5

circles = [
    {"pos": (100, 100), "radius": 30, "color": (255, 0, 0)},
    {"pos": (200, 200), "radius": 40, "color": (0, 255, 0)},
    {"pos": (300, 300), "radius": 50, "color": (0, 0, 255)},
    {"pos": (400, 400), "radius": 60, "color": (255, 255, 0)},
    {"pos": (500, 500), "radius": 70, "color": (0, 255, 255)}
]

run_images = [pygame.image.load(f"run_{i}.png") for i in range(1, 5)]
run_index = 0
running = False

clock = pygame.time.Clock()
running_game = True
while running_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            elif event.key == pygame.K_a:
                sprite_rect.x -= 10
            elif event.key == pygame.K_d:
                sprite_rect.x += 10
            elif event.key == pygame.K_w:
                sprite_rect.y -= 10
            elif event.key == pygame.K_s:
                sprite_rect.y += 10
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                line_thickness += 1
            elif event.key == pygame.K_MINUS:
                line_thickness -= 1
            elif event.key == pygame.K_UP:
                running = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                for circle in circles:
                    if event.key == pygame.K_LEFT:
                        circle["radius"] -= 10
                    elif event.key == pygame.K_RIGHT:
                        circle["radius"] += 10

    screen.fill((255, 255, 255))

    for rect in rectangles:
        pygame.draw.rect(screen, rect[2], (*rect[0], *rect[1]))

    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)

    screen.blit(sprite, sprite_rect)

    pygame.draw.line(screen, line_color, (100, 500), (700, 500), line_thickness)

    for circle in circles:
        pygame.draw.circle(screen, circle["color"], circle["pos"], circle["radius"])

    if running:
        run_index = (run_index + 1) % len(run_images)
        screen.blit(run_images[run_index], sprite_rect.topleft)
        time.sleep(0.1)
    else:
        screen.blit(run_images[0], sprite_rect.topleft)

    pygame.display.flip()
    time.delay(60)

pygame.quit()
