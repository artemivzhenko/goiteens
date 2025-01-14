# import pygame
# import random
#
# pygame.init()
# screen = pygame.display.set_mode((800, 800))
# coordinates_list = []
# for i in range(10):
#     coordinates_list.append((random.randint(0, 800), random.randint(0, 800)))
#
# wall = pygame.image.load("/Users/artem/PycharmProjects/GoIT/git/PYTHON_JUN_4_27_07_24/lessons/wall.png")
# wall1 = pygame.transform.scale(wall, (50, 800))
# wall2 = pygame.transform.scale(wall, (800, 50))
# wall = pygame.transform.scale(wall, (50, 50))
# alpha = 0
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     alpha += 5
#     if alpha > 255:
#         alpha = 0
#     screen.fill((0, 0, 0))
#     for i in range(0, 16):
#         screen.blit(wall, (0, 50*i))
#         screen.blit(wall, (50*i, 0))
#     pygame.display.flip()
#     pygame.time.delay(30)


import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Проєкт")
character_image = pygame.image.load("door.png")
character_image = pygame.transform.scale(character_image, (50, 50))
game_is_running = True
x, y = 50, 50
while game_is_running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
    if event.type == pygame.KEYDOWN:
        move_buttons = [pygame.K_a, pygame.K, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE]
        if event.key in move_buttons:
            match event.key:
                case pygame.K_LEFT:
                    x -= 5
                case pygame.K_RIGHT:
                    x += 5
                case pygame.K_UP:
                    y -= 5
                case pygame.K_DOWN:
                    y += 5
    screen.fill((255, 255, 255))
    screen.blit(character_image, (x, y))
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()


# image = pygame.image.load("superman.png")
# alpha = 0
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     alpha += 5
#     if alpha > 255:
#         alpha = 0
#
#     image.set_alpha(alpha)
#     screen.fill((0, 0, 0))
#     screen.blit(image, (100, 150))
#     pygame.display.flip()

# scaled_image = pygame.transform.scale(hero_image, (200, 300))
# screen.blit(scaled_image, (100, 150))
# pygame.display.flip()


# rotated_image = pygame.transform.rotate(hero_image, 45)
# screen.blit(rotated_image, (100, 150))
# pygame.display.flip()
# running = True


# image.set_alpha(128)
#
# screen.blit(image, (100, 150))
# pygame.display.flip()
#
# image = pygame.image.load("sprite.png")
# image_copy = image.copy()
# image_copy.fill((255, 0, 0, 128), special_flags=pygame.BLEND_RGBA_MULT)
# screen.blit(image_copy, (100, 150))
# pygame.display.flip()

#
# pixel_array = pygame.PixelArray(image)
#
# for x in range(image.get_width()):
#     for y in range(image.get_height()):
#         r, g, b, a = image.unmap_rgb(pixel_array[x, y])
#         gray = (r + g + b) // 3
#         pixel_array[x, y] = (gray, gray, gray, a)
#
# image_bw = pixel_array.make_surface()
#
# screen.blit(image_bw, (100, 150))
# pygame.display.flip()
