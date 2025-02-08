import pygame
import time

pygame.init()

pygame.display.set_caption("Гра Просторова Пригода")
screen = pygame.display.set_mode((800, 600))
icon_image = pygame.image.load("dog.jpg")
pygame.display.set_icon(icon_image)

screen.fill((0, 0, 255))
pygame.display.flip()

font = pygame.font.Font(None, 36)
text = font.render('Привіт, геймери!', True, (255, 255, 255))
screen.blit(text, (50, 50))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(1)
pygame.quit()