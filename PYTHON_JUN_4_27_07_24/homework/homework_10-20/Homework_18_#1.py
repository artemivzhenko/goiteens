import pygame


pygame.init()
black = (0,0,0)
white = (255,255,255)

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("ННР")
font = pygame.font.Font(None, 36)
text_1 = font.render("Привіт, pygame", True, white)
text_r = text_1.get_rect()
text_r.center(320,240)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(black)
    screen.blit(text_1, text_r)
    pygame.display.flip()

pygame.quit()