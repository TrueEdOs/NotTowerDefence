import pygame
import Resources


from config.settings import Settings
from controllers.ZombieController import ZombieController

from units.MovableUnit import MovableUnit


class Zombie(MovableUnit):
    def __init__(self, game_map, pos):
        MovableUnit.__init__(self, game_map, ZombieController(), Settings.zombie_hp,
                             pos, Settings.zombie_width, Settings.zombie_height, Settings.zombie_speed, "evil", "zombie", Resources.UnitTypes.enemy)

    def draw(self):
        pygame.draw.circle(self.game_map.surface, (0, 200, 0),
                           (int(self.pos[0] + self.width / 2), int(self.pos[1] + self.height / 2)), self.width // 2)

    def is_collide(self, to):
        if to.unit_type == Resources.UnitTypes.core:
            return True
        return False

