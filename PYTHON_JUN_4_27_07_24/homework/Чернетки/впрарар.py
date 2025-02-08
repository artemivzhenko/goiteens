import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Проста анімація квадрата")
square = pygame.Rect(350, 250, 100, 100)
static_square = pygame.Rect(50, 250, 100, 100)
static_square_color = (0, 128, 255)
x, y = 400, 400
speed = 5
dragging = False
color = (0, 0, 200)
game_is_running = True
offset_x = 0
offset_y = 0
while game_is_running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
        elif event.type == pygame.KEYDOWN:
            move_buttons = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE]
            if event.key in move_buttons:
                match event.key:
                    case pygame.K_LEFT:
                        x -= speed
                    case pygame.K_RIGHT:
                        x += speed
                    case pygame.K_UP:
                        y -= speed
                    case pygame.K_DOWN:
                        y += speed
                    case pygame.K_SPACE:
                        x, y = 400, 400
            else:
                match event.key:
                    case pygame.K_r:
                        color = (255, 0, 0)
                    case pygame.K_g:
                        color = (0, 255, 0)
                    case pygame.K_b:
                        color = (0, 0, 255)
                    case _:
                        color = (0, 0, 0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if square.collidepoint(event.pos):
                dragging = True
                mouse_x, mouse_y = event.pos
                offset_x = square.x - mouse_x
                offset_y = square.y - mouse_y
            match event.button:
                case 1:
                    print("Ви натиснули ліву кнопку миші")
                case 3:
                    print("Ви натиснули праву кнопку миші")
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            if not square.colliderect(static_square):
                mouse_x, mouse_y = event.pos
                square.x = mouse_x + offset_x
                square.y = mouse_y + offset_y
            else:
                square.x = 400
                square.y = 400
                dragging = False
        if square.colliderect(static_square):
            static_square_color = (255, 0, 128)
        else:
            static_square_color = (0, 128, 255)

    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
        if keys[pygame.K_c]:
            print("Ви натиснули комбінацію ctrl+c")
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color, square)
    pygame.draw.rect(screen, static_square_color, static_square)
    pygame.display.flip()

pygame.quit()