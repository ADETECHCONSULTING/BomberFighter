import pygame


class Bomb(object):
    def __init__(self, x, y, bombRange=5):
        self.x = x
        self.y = y
        self.velocity = 5
        self.bombRange = bombRange
        self.timeToExplode = 3000

    def update(self, dt):
        self.timeToExplode -= dt

    def explode(self, screen):
        pygame.draw.line(screen, (200, 0, 0), (self.x, self.y),
                         (self.x + 20 + (40 * self.bombRange), self.y), 40)
        pygame.draw.line(screen, (200, 0, 0), (self.x, self.y),
                         (self.x - 20 - (40 * self.bombRange), self.y), 40)
        pygame.draw.line(screen, (200, 0, 0), (self.x, self.y),
                         (self.x, self.y + 20 + (40 * self.bombRange)), 40)
        pygame.draw.line(screen, (200, 0, 0), (self.x, self.y),
                         (self.x, self.y - 20 - (40 * self.bombRange)), 40)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 20)
