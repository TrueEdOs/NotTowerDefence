import pygame
import config.colors as color
import Utils

from config.settings import Settings
from controllers.Controller import Controller
from models.Map import Map
from runnable.Runnable import Runnable
from units.Core import Core
from units.Zombie import Zombie
from controllers.ZombieController import ZombieController
from runnable.PauseMenu import PauseMenu


class Game(Runnable):
    def __init__(self, width, height, runnable_stack):
        Runnable.__init__(self, width, height, runnable_stack)
        self.timer = 0
        self.wave_count = 0
        self.game_over = False
        self.background_image = pygame.image.load(Settings.background_image)
        self.game_map = Map(width, height)
        self.game_map.add_unit(Core(self.game_map, (300, 300)))
        self.game_map.add_unit(Zombie(self.game_map, (100, 100)))
       # self.game_map.add_unit(Zombie(self.game_map, (100, 400)))
       # self.game_map.add_unit(Zombie(self.game_map, (600, 600)))
       # self.game_map.add_unit(Zombie(self.game_map, (300, 700)))

    def handle_player_events(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                self.runnable_stack.pop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.runnable_stack.push(PauseMenu(Settings.pause_menu_width, Settings.pause_menu_height,
                                                       self.runnable_stack, color.lightgrey,
                                                       x=Settings.screen_width // 2 - Settings.pause_menu_width // 2,
                                                       y=Settings.screen_height // 2 - Settings.pause_menu_height // 2))

    def update_state(self):
        self.game_map.step()
        pass

    def update_surface(self):
        self.surface.blit(self.game_map.surface, (self.x, self.y))
        pass
