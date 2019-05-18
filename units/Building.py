import pygame

from config.textures import Textures
from units.Unit import Unit


class Building(Unit):
    def __init__(self, game_map, controller, hp, pos, width, height, name, unit_type, cost, texture):
        Unit.__init__(self, game_map, controller, hp, pos, width, height, "player", name, unit_type)
        self.cost = cost
        self.surface = pygame.transform.scale(Textures.textures[texture], (self.width, self.height))
