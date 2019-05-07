import pygame
import config.settings as c

from models.GameObject import GameObject


class Core(GameObject):
    def __init__(self, game, controller, x, y):
        GameObject.__init__(self, game, controller, c.core_hp, x, y, c.core_width, c.core_height)

    def draw(self):
        pygame.draw.circle(self.game.surface, (255, 50, 0), (self.x, self.y), self.width // 2)