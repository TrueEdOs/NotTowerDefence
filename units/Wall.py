import pygame

import Resources
from controllers.Controller import Controller
from units.Building import Building


class Wall(Building):
    def __init__(self, game_map, pos):
        Building.__init__(self, game_map, Controller(), 10, pos, 66, 66, "wall", Resources.UnitTypes.wall, 1)

    def is_collide(self, to):
        if to.unit_type == Resources.UnitTypes.bullet:
            return False
        return True

    def draw(self):
        self.game_map.surface.blit(pygame.transform.scale
                           (pygame.image.load("images/box.jpg"), (self.width, self.height)), self.pos)

    def is_collide(self, to):
        return True

