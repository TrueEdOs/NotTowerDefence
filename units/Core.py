import pygame
import Resources

from config.settings import Settings
from controllers.Controller import Controller

from units.Unit import Unit


class Core(Unit):
    def __init__(self, game_map, pos):
        Unit.__init__(self, game_map, Controller(), Settings.core_hp, pos, Settings.core_width,
                      Settings.core_height, "player", "core", Resources.UnitTypes.core)

    def draw(self):
        pygame.draw.circle(self.game_map.surface, (255, 50, 0),
                           (int(self.pos[0] + self.width / 2), int(self.pos[1] + self.height / 2)), self.width // 2)

    def is_collide(self, to):
        if to.unit_type == Resources.UnitTypes.enemy:
            return True
        return False
