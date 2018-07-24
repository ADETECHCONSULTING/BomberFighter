import pygame

pygame.init()

screenWidth = 800
screenHeight = 525

pygame.display.set_caption("First game")

window = pygame.display.set_mode((screenWidth,screenHeight))

walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/background.png')

x = 50
y = 425
width = 64
height = 64
velocity = 5
isJumping = False
jumpHeight = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    window.blit(bg, (0,0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()







#MAIN loop
running = True
while running:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x-= velocity

    if keys[pygame.K_RIGHT] and x < screenWidth - width - velocity:
        x+= velocity

    if not(isJumping):
        if keys[pygame.K_SPACE]:
            isJumping = True
    else:
        if jumpHeight >= -10:
            neg = 1
            if jumpHeight < 0:
                neg = -1
            y -= (jumpHeight ** 2) * 0.5 * neg
            jumpHeight -= 1
        else:
            isJumping = False
            jumpHeight = 10

    redrawGameWindow()

pygame.quit()
