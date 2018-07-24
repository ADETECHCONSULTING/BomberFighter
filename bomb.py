import pygame

class Bomb(object):
    def __init__(self, x,y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing


    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
