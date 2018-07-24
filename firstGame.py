import pygame
import player
import bomb

pygame.init()

screenWidth = 800
screenHeight = 525

pygame.display.set_caption("First game")

window = pygame.display.set_mode((screenWidth,screenHeight))
bg = pygame.image.load('images/background.png')

clock = pygame.time.Clock()
player1 = player.Player(50, 410, 64, 64, 1)
player2 = player.Player(700, 410, 64, 64, 2)


def redrawGameWindow():
    global walkCount
    window.blit(bg, (0,0))
    player1.draw(window)
    player2.draw(window)
    for bomb in bombs:
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

    for bomb in bombs:
        if bomb.x < 500 and bomb.x > 0:
            bomb.x += bomb.velocity
        else:
            bombs.pop(bombs.index(bomb))

    keys = pygame.key.get_pressed()

    player1.update(keys, screenWidth)
    player2.update(keys, screenWidth)

    if player1.playerNumber == 1:
        if keys[pygame.K_SPACE]:
            if len(bombs) < 5:
                bombs.append(bomb.Bomb(int(player1.x + player1.width //2), int(player1.y + player1.height //2)))

    if player2.playerNumber == 2:
        if keys[pygame.K_s]:
            if len(bombs) < 5:
                bombs.append(bomb.Bomb(int(player2.x + player1.width //2), int(player2.y + player2.height //2)))

    redrawGameWindow()

pygame.quit()
