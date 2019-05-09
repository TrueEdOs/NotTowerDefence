import pygame
import config.settings as c

from units.Unit import Unit


class Core(Unit):
    def __init__(self, game, controller, x, y):
        Unit.__init__(self, game, controller, c.core_hp, x, y, c.core_width, c.core_height)

    def draw(self):
        pygame.draw.circle(self.game.surface, (255, 50, 0), (self.x, self.y), self.width // 2)
