import pygame

pygame.init()

screen = pygame.display.set_mode([1000, 1000])

scree =  pygame.display.set_caption ( "paddles ")

running = True

x = 500

y = 500

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -=10
            if event.key == pygame.K_RIGHT:
                x +=10
            if event.key == pygame.K_UP:
                y -=10
            if event.key == pygame.K_DOWN:
                y +=10

    #screen.fill((0, 0,))

    #does't show rectangle just black background

    # Initializing Color
    color = (0, 0, 153)

    # Drawing Rectangle
    pygame.draw.rect(screen, color, pygame.Rect(0, 230, 30, 500))
    pygame.display.flip()

    # Initializing Color
    color = (153, 0, 0)

    # Drawing Rectangle
    pygame.draw.rect(screen, color, pygame.Rect(970, 230, 30, 500))

pygame.quit()