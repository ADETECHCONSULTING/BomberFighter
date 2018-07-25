import pygame
import bomb

class Player(object):

    def __init__(self, x, y, width, height, playerNumber, versus_player = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJumping = False
        self.jumpHeight = 10
        self.right = False
        self.left = False
        self.walkCount = 0
        self.standing = True
        self.bombs = []
        self.playerNumber = playerNumber
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.__versus_player = versus_player
        self.shootLoop = 0
        self.health = 10
        self.visible = True


        self.walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'),
                     pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'),
                     pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'),
                     pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'),
                     pygame.image.load('images/R9.png')]
        self.walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'),
                    pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'),
                    pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'),
                    pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'),
                    pygame.image.load('images/L9.png')]
        self.stay = pygame.image.load('images/standing.png')

    def get_versus_player(self):
        return self.__versus_player

    def set_versus_player(self, versus_player):
        self.__versus_player = versus_player

    def draw(self, window):
        if self.visible:
            if self.walkCount + 1 >= 27:  # because 27 frames per seconds
                self.walkCount = 0

            if not self.standing:
                if self.left:
                    window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1

                elif self.right:
                    window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    window.blit(self.walkRight[0], (self.x, self.y))
                else:
                    window.blit(self.walkLeft[0], (self.x, self.y))

            self.hitbox = (self.x + 20, self.y, 28, 60)
            pygame.draw.rect(window, (255, 0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            #pygame.draw.rect(window, (255,0,0,0), self.hitbox, 2)


    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("hit")

    def update(self, keys, screenWidth, window):

        if self.playerNumber == 1:

            #basic timer pour les shoots un par un
            if self.shootLoop > 0:
                self.shootLoop += 1
            if self.shootLoop > 5:
                self.shootLoop = 0

            for bmb in self.bombs:

                if self.__versus_player != None:
                    if bmb.timeToExplode <= 0:
                        if bmb.y - bmb.radius < self.__versus_player.hitbox[1] + self.__versus_player.hitbox[3] and bmb.y + bmb.radius > self.__versus_player.hitbox[1]:
                            if bmb.x + (40 * 5) > self.__versus_player.hitbox[0] and bmb.x - (40 * 5) < self.__versus_player.hitbox[0] + self.__versus_player.hitbox[2]:
                                self.__versus_player.hit()
                                self.bombs.pop(self.bombs.index(bmb))
                    else:
                        if bmb.y - bmb.radius < self.__versus_player.hitbox[1] + self.__versus_player.hitbox[3] and bmb.y + bmb.radius > self.__versus_player.hitbox[1]:
                            if bmb.x + bmb.radius > self.__versus_player.hitbox[0] and bmb.x - bmb.radius < self.__versus_player.hitbox[0] + self.__versus_player.hitbox[2]:
                                self.__versus_player.hit()
                                self.bombs.pop(self.bombs.index(bmb))

                if bmb.x < 800 and bmb.x > 0:
                    bmb.x += bmb.velocity
                    bmb.update(50)
                    if bmb.timeToExplode <= 0:
                        bmb.explode(window)
                else:
                    self.bombs.pop(self.bombs.index(bmb))

            if keys[pygame.K_DOWN] and self.shootLoop == 0:
                facing = 1
                if self.left:
                    facing = -1

                if len(self.bombs) < 5:
                    self.bombs.append(
                        bomb.Bomb(int(self.x + self.width // 2), int(self.y + self.height // 2), facing, 10,
                                  self.playerNumber))

                self.shootLoop = 1

            if keys[pygame.KMOD_CTRL]:
                for bomb_explode in self.bombs:
                    if bomb_explode.player == self.playerNumber:
                        bomb_explode.explode(window)

            if keys[pygame.K_LEFT] and self.x > self.velocity:
                self.x -= self.velocity
                self.left = True
                self.right = False
                self.standing = False

            elif keys[pygame.K_RIGHT] and self.x < screenWidth - self.width - self.velocity:
                self.x += self.velocity
                self.left = False
                self.right = True
                self.standing = False

            else:
                self.standing = True
                self.walkCount = 0

            if not (self.isJumping):
                if keys[pygame.K_UP]:
                    self.isJumping = True
            else:
                if self.jumpHeight >= -10:
                    neg = 1
                    if self.jumpHeight < 0:
                        neg = -1
                    self.y -= (self.jumpHeight ** 2) * 0.5 * neg
                    self.jumpHeight -= 1
                else:
                    self.isJumping = False
                    self.jumpHeight = 10

        else:
            # basic timer pour les shoots un par un
            if self.shootLoop > 0:
                self.shootLoop += 1
            if self.shootLoop > 5:
                self.shootLoop = 0

            for bmb in self.bombs:

                if self.__versus_player != None:
                    if bmb.timeToExplode <= 0:
                        if bmb.y - bmb.radius < self.__versus_player.hitbox[1] + self.__versus_player.hitbox[3] and bmb.y + bmb.radius > self.__versus_player.hitbox[1]:
                            if bmb.x + (40 * 5) > self.__versus_player.hitbox[0] and bmb.x - (40 * 5) < \
                                    self.__versus_player.hitbox[0] + self.__versus_player.hitbox[2]:
                                self.__versus_player.hit()
                                self.bombs.pop(self.bombs.index(bmb))
                    else:
                        if bmb.y - bmb.radius < self.__versus_player.hitbox[1] + self.__versus_player.hitbox[3] and bmb.y + bmb.radius > self.__versus_player.hitbox[1]:
                            if bmb.x + bmb.radius > self.__versus_player.hitbox[0] and bmb.x - bmb.radius < \
                                    self.__versus_player.hitbox[0] + self.__versus_player.hitbox[2]:
                                self.__versus_player.hit()
                                self.bombs.pop(self.bombs.index(bmb))

            for bmb in self.bombs:
                if bmb.x < 800 and bmb.x > 0:
                    bmb.x += bmb.velocity
                    bmb.update(50)
                    if bmb.timeToExplode <= 0:
                        bmb.explode(window)
                else:
                    self.bombs.pop(self.bombs.index(bmb))

            facing = -1
            if self.right:
                facing = 1

            if keys[pygame.K_s] and self.shootLoop == 0:
                intx = int(self.x + self.width // 2)
                inty = int(self.y + self.height // 2)
                if len(self.bombs) < 5:
                    self.bombs.append(bomb.Bomb(intx, inty, facing, 10, self.playerNumber))


            if keys[pygame.K_a] and self.x > self.velocity:
                self.x -= self.velocity
                self.left = True
                self.right = False
                self.standing = False

            elif keys[pygame.K_d] and self.x < screenWidth - self.width - self.velocity:
                self.x += self.velocity
                self.left = False
                self.right = True
                self.standing = False

            else:
                self.standing = True
                self.walkCount = 0

            if not (self.isJumping):
                if keys[pygame.K_w]:
                    self.isJumping = True
            else:
                if self.jumpHeight >= -10:
                    neg = 1
                    if self.jumpHeight < 0:
                        neg = -1
                    self.y -= (self.jumpHeight ** 2) * 0.5 * neg
                    self.jumpHeight -= 1
                else:
                    self.isJumping = False
                    self.jumpHeight = 10