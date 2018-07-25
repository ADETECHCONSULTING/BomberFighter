import pygame
import player
import bomb

pygame.init()

screenWidth = 800
screenHeight = 525

pygame.display.set_caption("BombermanFighter")

window = pygame.display.set_mode((screenWidth,screenHeight))
bg = pygame.image.load('images/background.png')

clock = pygame.time.Clock()
player1 = player.Player(50, 410, 64, 64, 1)
player2 = player.Player(700, 410, 64, 64, 2)
player1.set_versus_player(player2)
player2.set_versus_player(player1)


def redrawGameWindow():
    global walkCount
    window.blit(bg, (0,0))
    player1.draw(window)
    player2.draw(window)

    for bomb in player1.bombs:
        bomb.draw(window)

    for bomb in player2.bombs:
        bomb.draw(window)

    pygame.display.update()


#MAIN loop
running = True
bombs = []
while running:
    clock.tick(27) #27 fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.KMOD_CTRL]:
            for bomb_explode in bombs:
                if bomb_explode.player == player2.playerNumber:
                    bomb_explode.explode(window)

    player1.update(keys, screenWidth,window)
    player2.update(keys, screenWidth,window)

    redrawGameWindow()

pygame.quit()
