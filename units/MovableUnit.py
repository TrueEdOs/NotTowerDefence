import Utils
from units.Unit import Unit
import math


class MovableUnit(Unit):
    def __init__(self, game_map, controller, hp, pos, width, height, speed, owner, name, unit_type):
        Unit.__init__(self, game_map, controller, hp, pos, width, height, owner, name, unit_type)
        self.speed = speed

    def step_to(self, pos):
        dx = abs(pos[0] - self.pos[0])
        dy = abs(pos[1] - self.pos[1])
        if dx != 0:
            alpha = math.atan(dy / dx)
        else:
            alpha = math.pi
        dx = math.cos(alpha) * self.speed
        if self.pos[0] > pos[0]:
            dx *= -1
        if abs(dx) > abs(pos[0] - self.pos[0]):
            dx = pos[0] - self.pos[0]
        dy = math.sin(alpha) * self.speed
        if abs(dy) > abs(pos[1] - self.pos[1]):
            dy = pos[1] - self.pos[1]
        if self.pos[1] > pos[1]:
            dy *= -1
        #print(self.pos, pos, dx, dy)
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def move(self, pos):
        old_pos = (self.pos[0], self.pos[1])
        self.step_to(pos)
        if self.is_blocked():
            #print("AAAA")
            self.step_to(old_pos)
            return False
        return True

    def is_blocked(self):
        for unit in self.game_map.units.values():
            if (self.is_collide(unit) or unit.is_collide(self)) and Utils.is_intersected(self, unit):
                return True
        return False
