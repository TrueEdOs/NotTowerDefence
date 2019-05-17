import pygame

import Resources
from controllers.Controller import Controller
from units.Building import Building


class Cannon(Building):
    def __init__(self, game_map, pos, texture):
        Building.__init__(self, game_map, Controller(), 10, pos, 66, 66, "cannon", Resources.UnitTypes.gun, 5, texture)

    def draw(self):
        self.game_map.surface.blit(self.surface, self.pos)

    def is_collide(self, to):
        return True

