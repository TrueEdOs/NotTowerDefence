import pygame
import config.settings as c

from controllers.Controller import Controller
from units.Core import Core
from units.Zombie import Zombie
from controllers.ZombieController import ZombieController


class Game:
    def __init__(self):
        self.units = []
        self.timer = 0
        self.wave_count = 0
        self.game_over = False
        self.background_image = pygame.image.load(c.background_image)
        pygame.init()
        self.surface = pygame.display.set_mode((c.screen_width, c.screen_height))
        pygame.display.set_caption("No Tower Defense")
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
        self.units.append(Zombie(self, ZombieController(), 50, 50))
        self.units.append(Core(self, Controller(), 500, 500))
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.surface.blit(self.background_image, (0, 0))
            self.handle_player_events()
            self.handle_unit_actions()
            self.draw()
            pygame.display.update()
            self.clock.tick(c.fps)
