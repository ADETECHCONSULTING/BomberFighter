import pygame


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, facing, radius, player, bombRange=5):
        self.x = x
        self.y = y
        self.facing = facing
        self.radius = radius
        self.player = player
        self.velocity = facing * 8
        self.bombRange = bombRange
        self.timeToExplode = 3000

    def update(self, dt):
        self.timeToExplode -= dt

    def explode(self, screen):
        pygame.draw.line(screen, (200, 0, 0), (self.x, self.y),(self.x + 20 + (40 * self.bombRange), self.y), 40)
        pygame.draw.line(screen, (200, 0, 0), (self.x, self.y),(self.x - 20 - (40 * self.bombRange), self.y), 40)
        pygame.draw.line(screen, (200, 0, 0), (self.x, self.y),(self.x, self.y - 20 - (40 * self.bombRange)), 40)
        pygame.display.flip()

    def draw(self, window):
        pygame.draw.circle(window, (0, 0, 0), (self.x, self.y), self.radius)
