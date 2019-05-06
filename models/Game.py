import pygame

from models.Box import Box
from models.Controller import Controller
from models.Core import Core
from models.Zombie import Zombie


class Game:
    def __init__(self):
        pygame.init()
        self.units = []
        self.timer = 0
        self.wave_count = 0
        self.game_over = False
        self.surface = pygame.display.set_mode((1000, 1000))
        self.clock = pygame.time.Clock()

    def handle_player_events(self):
        pass

    def draw(self):
        for unit in self.units:
            unit.draw()

    def handle_unit_actions(self):
        for unit in self.units:
            unit.action()

    def run(self):
        self.units.append(Zombie(self, Controller(), 10, 50, 50))
        self.units.append(Core(self, Controller(), 10, 500, 500))
        while not self.game_over:
            pygame.event.pump()
            self.handle_player_events()
            self.handle_unit_actions()
            self.draw()
            pygame.display.update()
            self.clock.tick(300)
