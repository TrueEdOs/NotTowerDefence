import pygame

from config.Resources import Constants, UnitTypes
from controllers.ZombieController import ZombieController

from units.MovableUnit import MovableUnit
from units.AttackableUnit import AttackableUnit


class Zombie(MovableUnit, AttackableUnit):
    def __init__(self, game_map, pos):
        MovableUnit.__init__(self, game_map, ZombieController(), Constants.zombie_hp,
                             pos, Constants.zombie_width, Constants.zombie_height, Constants.zombie_speed, "evil",
                             "zombie", UnitTypes.enemy)
        AttackableUnit.__init__(self, game_map, ZombieController(), Constants.zombie_hp,
                                pos, Constants.zombie_width, Constants.zombie_height, Constants.zombie_damage,
                                Constants.zombie_range, Constants.zombie_reload_time, "evil", "zombie", UnitTypes.enemy)

    def draw(self):
        pygame.draw.circle(self.game_map.surface, (0, 200, 0),
                           (int(self.pos[0] + self.width / 2), int(self.pos[1] + self.height / 2)), self.width // 2)

    def is_collide(self, to):
        if to.unit_type == UnitTypes.core:
            return True
        return False

