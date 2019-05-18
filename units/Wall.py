import pygame

import Resources
from controllers.Controller import Controller
from units.Building import Building


class Wall(Building):
    def __init__(self, game_map, pos, texture):
        Building.__init__(self, game_map, Controller(), 10, pos, 30, 30, "wall", Resources.UnitTypes.wall, 1, texture)


    def is_collide(self, to):
        if to.unit_type == Resources.UnitTypes.bullet:
            return False
        return True

    def draw(self):
        self.game_map.surface.blit(self.surface, self.pos)

    def is_collide(self, to):
        return True

