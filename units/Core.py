import pygame

from config.Resources import Constants, UnitTypes
from controllers.Controller import Controller

from units.Unit import Unit


class Core(Unit):
    def __init__(self, game_map, pos):
        Unit.__init__(self, game_map, Controller(), Constants.core_hp, pos, Constants.core_width,
                      Constants.core_height, "player", "core", UnitTypes.core)

    def draw(self):
        pygame.draw.circle(self.game_map.surface, (255, 50, 0),
                           (int(self.pos[0] + self.width / 2), int(self.pos[1] + self.height / 2)), self.width // 2)

    def is_collide(self, to):
        if to.unit_type == UnitTypes.enemy:
            return True
        return False
