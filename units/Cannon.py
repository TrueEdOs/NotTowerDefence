import pygame

from controllers.CannonController import CannonController
from config.Resources import Constants, UnitTypes
from units.AttackableUnit import AttackableUnit
from units.Building import Building
from units.Shell import Shell


class Cannon(Building, AttackableUnit):
    def __init__(self, game_map, pos, texture):
        Building.__init__(self, game_map, CannonController(), 10, pos, Constants.cannon_width, Constants.cannon_height,
                          "cannon", UnitTypes.gun, 5, texture)
        AttackableUnit.__init__(self, game_map, CannonController(), Constants.cannon_hp,
                                pos, Constants.cannon_width, Constants.cannon_height, Constants.cannon_damage,
                                Constants.cannon_range, Constants.cannon_reload_time, "good", "cannon", UnitTypes.gun)

    def draw(self):
        self.game_map.surface.blit(self.surface, self.pos)

    def is_collide(self, to):
        if to.unit_type == UnitTypes.bullet:
            return False
        return True

    def attack(self, unit):
        if self.is_reloaded == 0:
            self.game_map.add_unit(Shell(self.game_map, (self.pos[0], self.pos[1]), unit.pos))
            return True
        return False
