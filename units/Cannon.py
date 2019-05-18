import pygame

import Resources
from controllers.Controller import Controller
from units.AttackableUnit import AttackableUnit
from units.Building import Building


class Cannon(Building, AttackableUnit):
    def __init__(self, game_map, pos, texture):
        Building.__init__(self, game_map, Controller(), 10, pos, 66, 66, "cannon", Resources.UnitTypes.gun, 5, texture)
        AttackableUnit.__init__(self, game_map, Controller(), 10, pos, 66, 66, 1, 200, "cannon",
                                Resources.UnitTypes.gun)

    def draw(self):
        self.game_map.surface.blit(self.surface, self.pos)

    def is_collide(self, to):
        return True
