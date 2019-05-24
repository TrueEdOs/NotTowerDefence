import pygame
import Utils


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height))
        self.units = {}
        self.killed = []

    def is_collide_with_something(self, x):
        for unit in self.units.values():
            if x.is_collide(unit):
                return unit
        return None

    def add_unit(self, new_unit):
        for unit in self.units.values():
            if (unit.is_collide(new_unit) or new_unit.is_collide(unit)) and Utils.is_intersected(unit, new_unit):
                return False
        self.units[new_unit.id] = new_unit
        return True

    def update_surface(self):
        self.surface.fill((255, 255, 255))
        for unit in self.units.values():
            unit.draw()

    def action_all(self):
        for unit in list(self.units.values()):
            unit.action()
        self.killed.clear()
        for unit in list(self.units.values()):
            if unit.hp <= 0:
                self.killed.append(unit)
                self.units.pop(unit.id)

    def step(self):
        self.action_all()
        self.update_surface()
