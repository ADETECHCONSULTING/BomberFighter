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

    for bmb in bombs:
        if bmb.x < 500 and bmb.x > 0:
            bmb.x += bmb.velocity
        else:
            bombs.pop(bombs.index(bmb))

    keys = pygame.key.get_pressed()

    if player1.playerNumber == 1:
        if keys[pygame.K_SPACE]:
            facing = 1
            if player1.left:
                facing = -1

            if len(bombs) < 5:
                bombs.append(bomb.Bomb(int(player1.x + player1.width //2), int(player1.y + player1.height //2), facing, 10, player1.playerNumber))

        if keys[pygame.KMOD_CTRL]:
            for bomb_explode in bombs:
                if bomb_explode.player == player1.playerNumber:
                    bomb_explode.explode(window)

    if player2.playerNumber == 2:
        facing = 1
        if player2.left:
            facing = -1

        if keys[pygame.K_s]:
            if len(bombs) < 5:
                bombs.append(bomb.Bomb(int(player2.x + player2.width //2), int(player2.y + player2.height //2), facing, 10, player2.playerNumber))

    if keys[pygame.KMOD_CTRL]:
            for bomb_explode in bombs:
                if bomb_explode.player == player2.playerNumber:
                    bomb_explode.explode(window)

    player1.update(keys, screenWidth)
    player2.update(keys, screenWidth)

    redrawGameWindow()

pygame.quit()
