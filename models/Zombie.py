import pygame
import config.settings as c

from models.MovableObject import MovableObject


class Zombie(MovableObject):
    def __init__(self, game, controller, x, y):
        MovableObject.__init__(self, game, controller, c.zombie_hp, x, y, c.zombie_width, c.zombie_height, c.zombie_speed)

    def draw(self):
        pygame.draw.circle(self.game.surface, (30, 255, 150), (self.x, self.y), self.width // 2)


