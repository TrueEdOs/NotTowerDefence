import Utils
from units.Unit import Unit
import math


class AttackableUnit(Unit):
    def __init__(self, game_map, controller, hp, pos, width, height, damage, attack_range, owner, name, unit_type):
        Unit.__init__(self, game_map, controller, hp, pos, width, height, owner, name, unit_type)
        self.damage = damage
        self.attack_range = attack_range

    def attack(self, unit):
        if self.can_attack(unit):
            unit.get_damage(self.damage)
            return True
        return False

    def can_attack(self, unit):
        if self.attack_range < Utils.dist(self, unit):
            return False
        return True
