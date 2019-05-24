import pygame

from config.Resources import Constants, UnitTypes
from config import colors as color
from controllers.ShellController import ShellController
from units.Unit import Unit
from units.MovableUnit import MovableUnit
from units.AttackableUnit import AttackableUnit


class Shell(MovableUnit, AttackableUnit):
    def __init__(self, game_map, pos, target_pos):
        MovableUnit.__init__(self, game_map, ShellController(), Constants.shell_hp,
                             pos, Constants.shell_width, Constants.shell_height, Constants.shell_speed, "good",
                             "shell", UnitTypes.bullet)
        AttackableUnit.__init__(self, game_map, ShellController(), Constants.shell_hp,
                                pos, Constants.shell_width, Constants.shell_height, Constants.shell_damage,
                                Constants.shell_range, 100, "good", "shell", UnitTypes.bullet)
        old_pos = self.pos
        dx, dy = self.step_to(target_pos)
        self.step_to(old_pos)
        self.target_direction = target_pos[0] + dx * 1000, target_pos[1] + dy * 1000

    def draw(self):
        pygame.draw.circle(self.game_map.surface, color.brick,
                           (int(self.pos[0] + self.width / 2), int(self.pos[1] + self.height / 2)), self.width // 2)

    def is_collide(self, to):
        #if to.unit_type == UnitTypes.wall or to.unit_type == UnitTypes.gun:
            #return False
        return False

    def attack(self, unit):
        if self.is_reloaded == self.reload_time - 1:
            self.get_damage(self.hp)
            return False

        if unit.unit_type == UnitTypes.enemy and self.can_attack(unit):
            self.get_damage(min(unit.hp, self.hp))
            unit.get_damage(min(unit.hp, self.damage))
            return True
        return False
