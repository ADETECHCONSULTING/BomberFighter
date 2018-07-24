import pygame
import player

pygame.init()

screenWidth = 800
screenHeight = 525

pygame.display.set_caption("First game")

window = pygame.display.set_mode((screenWidth,screenHeight))
bg = pygame.image.load('images/background.png')

clock = pygame.time.Clock()
man = player.Player(50, 410, 64, 64)


def redrawGameWindow():
    global walkCount
    window.blit(bg, (0,0))
    man.draw(window)

    pygame.display.update()


#MAIN loop
running = True
while running:
    clock.tick(27) #27 fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()


    man.update(keys, screenWidth)

    redrawGameWindow()

pygame.quit()
