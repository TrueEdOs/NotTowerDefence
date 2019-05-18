import pygame
import config.colors as color

from config.Resources import Constants
from runnable.ControlButton import ControlButton
from runnable.Game import Game
from runnable.Runnable import Runnable
from models.TextObject import TextObject
from runnable.TestMenu import TestMenu


class MainMenu(Runnable):
    def handle_player_events(self):
        for event in self.events:
            if event.type is pygame.KEYDOWN:
                if self.controls:
                    self.controls[self.selected_button].selected()
                    if event.key == pygame.K_UP:
                        self.selected_button -= 1
                    elif event.key == pygame.K_DOWN:
                        self.selected_button += 1
                    self.selected_button %= len(self.controls)
                    self.controls[self.selected_button].selected()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.controls[self.selected_button].pushed()

    def __init__(self, width, height, runnable_stack, bg_color, background = None):
        Runnable.__init__(self, width, height, runnable_stack)
        #self.menu_surface = pygame.display.set_mode((width, height))
        self.is_menu_running = False
        self.surface.fill(bg_color)
        self.title = TextObject("Not Tower Defense", Constants.font, 90, color.yellow)
        self.surface.blit(self.title.Text, (width / 2 - 250, 100))
        self.selected_button = 0

        new_game_button = ControlButton("New game", "newgame", width / 2 - 125, height / 2 - 75, 250, 100,  color.brick, color.black,
                                        lambda: runnable_stack.push(Game(Constants.screen_width, Constants.screen_height, self.runnable_stack)))
        quit_button = ControlButton("Quit", "quit", width / 2 - 75, height / 2 + 25, 250, 100, color.brick,
                                    color.black, lambda: runnable_stack.pop())

        self.add_control_button(new_game_button)
        self.add_control_button(quit_button)
        self.controls[self.selected_button].selected()
