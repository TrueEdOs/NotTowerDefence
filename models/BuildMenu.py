import pygame
import Utils
import config.colors as color

from runnable.ControlButton import ControlButton
from config.Resources import Constants


class BuildMenu:
    def __init__(self, spawn_funcs):
        width = Constants.build_menu_width
        height = Constants.build_menu_height
        self.surface = pygame.Surface((width, height))
        self.surface.fill((255, 0, 0))
        self.controls = []
        y = 0
        for func in spawn_funcs:
            self.controls.append(ControlButton(func().name + "   " + str(func().cost) + "$$", func().name + "SB",
                                               0, y, width, 100, color.gray13, color.black, func))
            y += 100
        self.draw()

    def draw(self):
        self.surface.fill((0, 244, 0))
        for button in self.controls:
            button.draw()
            self.surface.blit(button.surface, (button.x, button.y))

    def clicked(self, pos):
        for button in self.controls:
            if Utils.is_inside(pos, (button.abs_x, button.abs_y),
                               (button.abs_x + button.width, button.abs_y + button.height)):
                return button.pushed()
        return None
