import pygame
import config.settings as c

from units.MovableUnit import MovableUnit


class Zombie(MovableUnit):
    def __init__(self, game, controller, x, y):
        MovableUnit.__init__(self, game, controller, c.zombie_hp, x, y, c.zombie_width, c.zombie_height, c.zombie_speed)

    def draw(self):
        pygame.draw.circle(self.game.surface, (30, 255, 150), (self.x, self.y), self.width // 2)


