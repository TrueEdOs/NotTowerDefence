import pygame
import Utils
import Resources
import config.colors as color

from config.settings import Settings
from controllers.Controller import Controller
from models.BuildMenu import BuildMenu
from models.Map import Map
from runnable.Runnable import Runnable
from units.Core import Core
from units.Cannon import Cannon
from units.Wall import Wall
from units.Zombie import Zombie
from controllers.ZombieController import ZombieController
from runnable.PauseMenu import PauseMenu
from models.TextObject import TextObject


class Game(Runnable):
    def __init__(self, width, height, runnable_stack):
        Runnable.__init__(self, width, height, runnable_stack)
        self.timer = 0
        self.wave_count = 0
        self.game_over = False

        self.background_image = pygame.image.load(Settings.background_image)
        self.game_map = Map(width - Resources.Constants.build_menu_width, height)
        self.hand = None
        self.money = 100
        self.money_label = None
        self.build_menu = BuildMenu([lambda: Wall(self.game_map, (0, 0), 'images/box.jpg'),
                                     lambda: Cannon(self.game_map, (0, 0), 'images/cannon.png')])

        self.game_map.add_unit(Core(self.game_map, (250, 250)))
        for i in range(7):
            self.game_map.add_unit(Wall(self.game_map, (200 + 31 * i, 200), 'images/box.jpg'))
        for i in range(1, 7):
            self.game_map.add_unit(Wall(self.game_map, (200 + 31 * 6, 200 + 31 * i), 'images/box.jpg'))

        for i in range(5, -1, -1):
            self.game_map.add_unit(Wall(self.game_map, (200 + 31 * i, 200 + 31 * 6), 'images/box.jpg'))

        for i in range(1, 6):
            self.game_map.add_unit(Wall(self.game_map, (200, 200 + 31 * i), 'images/box.jpg'))

        self.game_map.add_unit(Zombie(self.game_map, (100, 100)))
        self.game_map.add_unit(Zombie(self.game_map, (100, 400)))
        self.game_map.add_unit(Zombie(self.game_map, (600, 600)))
        self.game_map.add_unit(Zombie(self.game_map, (300, 700)))

    def update_labels(self):
        self.money_label = TextObject("Money: " + str(self.money), Settings.font, 50, color.red)

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
        self.update_labels()
        if self.hand:
            self.hand.pos = pygame.mouse.get_pos()
        pass

    def update_surface(self):
        if self.hand:
            self.hand.draw()
        self.surface.blit(self.game_map.surface, (self.x, self.y))
        self.surface.blit(self.build_menu.surface, (self.game_map.width, 0))

        self.surface.blit(self.money_label.Text, (0, 0))
