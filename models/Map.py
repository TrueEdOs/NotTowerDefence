import pygame


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height))
        self.units = {}

    def is_collide_with_something(self, x):
        for unit in self.units.values():
            if x.is_collide(unit):
                return unit
        return None

    def add_unit(self, unit):
        self.units[unit.id] = unit

    def update_surface(self):
        self.surface.fill((255, 255, 255))
        for unit in self.units.values():
            unit.draw()

    def action_all(self):
        for unit in self.units.values():
            unit.action()

    def step(self):
        self.action_all()
        self.update_surface()
