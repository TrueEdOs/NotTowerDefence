import pygame

import Resources
import Utils
import config.settings as c

from controllers.Controller import Controller
from models.BuildMenu import BuildMenu
from models.Map import Map
from runnable.Runnable import Runnable
from units.Core import Core
from units.Wall import Wall
from units.Zombie import Zombie
from controllers.ZombieController import ZombieController


class Game(Runnable):
    def __init__(self, width, height, runnable_stack):
        Runnable.__init__(self, width, height, runnable_stack)
        self.timer = 0
        self.wave_count = 0
        self.game_over = False
        self.background_image = pygame.image.load(c.background_image)
        self.game_map = Map(width - Resources.Constants.build_menu_width, height)
        self.hand = None
        self.money = 0
        self.build_menu = BuildMenu([lambda: Wall(self.game_map, (0, 0))])
        ####
        self.game_map.add_unit(Core(self.game_map, (300, 300)))
        self.game_map.add_unit(Zombie(self.game_map, (100, 100)))
        self.game_map.add_unit(Zombie(self.game_map, (100, 400)))
        self.game_map.add_unit(Zombie(self.game_map, (600, 600)))
        self.game_map.add_unit(Zombie(self.game_map, (300, 700)))


    def handle_player_events(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                self.runnable_stack.pop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                res = self.build_menu.clicked((event.pos[0] - self.game_map.width, event.pos[1]))
                if not res:
                    if self.hand:
                        if not self.game_map.add_unit(self.hand):
                            continue
                        self.money -= self.hand.cost
                        self.hand = None
                    continue
                self.hand = res
        pass

    def update_state(self):
        self.game_map.step()
        if self.hand:
            self.hand.pos = pygame.mouse.get_pos()
        pass

    def update_surface(self):
        if self.hand:
            self.hand.draw()
        self.surface.blit(self.game_map.surface, (0, 0))
        self.surface.blit(self.build_menu.surface, (self.game_map.width, 0))
        pass
