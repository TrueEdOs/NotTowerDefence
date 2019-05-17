import pygame

import Resources
import Utils
from config import colors
from runnable.ControlButton import ControlButton


class BuildMenu:
    def __init__(self, spawn_funcs):
        width = Resources.Constants.build_menu_width
        height = Resources.Constants.build_menu_height
        self.surface = pygame.Surface((width, height))
        self.surface.fill((255, 0, 0))
        self.controls = []
        y = 0
        for func in spawn_funcs:
            self.controls.append(ControlButton(func().name + "   " + str(func().cost) + "$$", func().name + "SB",
                                               0, y, width, 100, colors.gray13, func))
            y += 100
        self.draw()

    def draw(self):
        self.surface.fill((0, 244, 0))
        for button in self.controls:
            button.draw()
            self.surface.blit(button.surface, (button.x, button.y))

    def clicked(self, pos):
        for button in self.controls:
            if Utils.is_inside(pos, (button.x, button.y),
                               (button.x + button.width, button.y + button.height)):
                return button.pushed()
        return None
