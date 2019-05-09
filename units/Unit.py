import pygame


class Unit:
    def __init__(self, game, controller, hp, x, y, width, height):
        self.game = game
        self.hp = hp
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.controller = controller

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width

    @property
    def bottom(self):
        return self.y

    @property
    def top(self):
        return self.y + self.height

    def draw(self):
        pass

    def action(self):
        self.controller.do(self, self.game.units)

    def get_damage(self, value):
        self.hp -= value

    def get_healing(self, value):
        self.hp += value
