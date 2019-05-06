import pygame

from models.MovableObject import MovableObject


class Zombie(MovableObject):
    def __init__(self, game, controller, x, y):
        MovableObject.__init__(self, game, controller, 50, x, y, 50, 50, 1)

    def draw(self):
        pygame.draw.circle(self.game.surface, (30, 255, 150), (self.x, self.y), self.width // 2)


