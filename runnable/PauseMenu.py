import pygame

import Resources
import config.colors as color

from config.settings import Settings
from runnable.ControlButton import ControlButton
from runnable.Runnable import Runnable
import runnable
from models.TextObject import TextObject
from runnable.TestMenu import TestMenu


class PauseMenu(Runnable):
    def handle_player_events(self):
        for event in self.events:
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.runnable_stack.pop()

    def __init__(self, width, height, runnable_stack, bg_color, background=None, x=0, y=0):
        Runnable.__init__(self, width, height, runnable_stack, x, y)
        # self.menu_surface = pygame.display.set_mode((width, height))
        self.is_menu_running = False
        self.surface.fill(bg_color)
        self.surface.set_alpha(Settings.menu_alpha)
        self.title = TextObject("Pause", Settings.font, 90, color.white)
        self.surface.blit(self.title.Text, (width // 4, 0))
        quit_button = ControlButton("", "quit", width // 4, height // 2, width // 6, width // 6,
                                    color.black, color.black,
                                    lambda: runnable_stack.set_one_task(
                                        runnable.MainMenu.MainMenu(Settings.screen_width, Settings.screen_height, runnable_stack,
                                                 color.brick)),
                                    Settings.quit_button_image)
        resume_button = ControlButton("", "resume", 3 * width // 4 - width // 6, height // 2, width // 6, width // 6,
                                      color.black, color.black, lambda: runnable_stack.pop(),
                                      Settings.resume_button_image)
        self.add_control_button(quit_button)
        self.add_control_button(resume_button)
