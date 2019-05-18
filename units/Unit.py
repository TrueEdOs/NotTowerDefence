import pygame


class Unit:
    unit_id = 0

    def __init__(self, game_map, controller, hp, pos, width, height, owner, name, unit_type):
        self.game_map = game_map
        self.hp = hp
        self.pos = pos
        self.width = width
        self.height = height
        self.controller = controller
        self.owner = owner
        self.name = name
        self.unit_type = unit_type
        self.id = Unit.unit_id
        Unit.unit_id += 1

    @property
    def left(self):
        return self.pos[0]

    @property
    def right(self):
        return self.left() + self.width

    @property
    def bottom(self):
        return self.pos[1]

    @property
    def top(self):
        return self.bottom() + self.height

    def draw(self):
        pass

    def action(self):
        self.controller.do(self, self.game_map.units.values())

    def get_damage(self, value):
        self.hp -= value

    def get_healing(self, value):
        self.hp += value

    def is_collide(self, to):
        return False
