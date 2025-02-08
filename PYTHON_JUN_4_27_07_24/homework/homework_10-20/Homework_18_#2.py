import pygame
pygame.init()


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Анімація руху квадрата")

blue = (0, 0, 255)
black = (0, 0, 0)

x = 0
y = 220
width = 50
height = 50
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += speed
    if x > 640:
        x = -width

    screen.fill(black)
    pygame.draw.rect(screen, blue, (x, y, width, height))
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
