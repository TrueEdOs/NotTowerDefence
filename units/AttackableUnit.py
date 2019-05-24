from Utils import dist, is_visible_from
from units.Unit import Unit
from config.Resources import UnitTypes
import math


class AttackableUnit(Unit):
    def __init__(self, game_map, controller, hp, pos, width, height, damage, attack_range, reload_time, owner, name, unit_type):
        Unit.__init__(self, game_map, controller, hp, pos, width, height, owner, name, unit_type)
        self.damage = damage
        self.attack_range = attack_range
        self.reload_time = reload_time
        self.is_reloaded = 0

    def attack(self, unit):
        if self.is_reloaded == 0 and self.can_attack(unit):
            unit.get_damage(self.damage)
            return True
        return False

    def can_attack(self, unit):
        if self.attack_range < dist(self, unit):
            return False
        if self.attack_range > 50 and not is_visible_from(self, unit, UnitTypes.bullet):
            return False
        return True

    def reload(self):
        self.is_reloaded += 1
        self.is_reloaded %= self.reload_time
