import pygame
from models.GameObject import GameObject


class Core(GameObject):
    def __init__(self, game, controller, x, y):
        GameObject.__init__(self, game, controller, 1500, x, y, 100, 100)

    def draw(self):
        pygame.draw.circle(self.game.surface, (255, 50, 0), (self.x, self.y), self.width // 2)
