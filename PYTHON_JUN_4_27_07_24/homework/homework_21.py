import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

red_rect = pygame.Rect(100, 100, 50, 50)
blue_rect = pygame.Rect(300, 100, 50, 50)
object_rect = pygame.Rect(200, 300, 50, 50)
speed = [5, 5]

dragging = None
counter = 0
font = pygame.font.SysFont(None, 55)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if red_rect.collidepoint(event.pos):
                dragging = red_rect
            elif blue_rect.collidepoint(event.pos):
                dragging = blue_rect
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                dragging.x = event.pos[0] - dragging.width // 2
                dragging.y = event.pos[1] - dragging.height // 2

    if red_rect.colliderect(blue_rect):
        counter += 1
        blue_rect.x = 100
        blue_rect.y = 100

    object_rect.x += speed[0]
    object_rect.y += speed[1]

    if object_rect.left < 0 or object_rect.right > 800:
        speed[0] = -speed[0]
    if object_rect.top < 0 or object_rect.bottom > 600:
        speed[1] = -speed[1]

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, red_rect)
    pygame.draw.rect(screen, BLUE, blue_rect)
    pygame.draw.rect(screen, RED, object_rect)
    text = font.render("Counter: " + str(counter), True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()

pygame.quit()
