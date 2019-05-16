import pygame
import config.colors as color

from config.settings import Settings
from pygame.surface import Surface
from models.TextObject import TextObject


class ControlButton:
    button_id = 0

    def __init__(self, title, name, x, y, width, height, button_color, func):
        self.title = title
        self.name = name
        self.id = ControlButton.button_id
        ControlButton.button_id += 1
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.func = func
        self.surface = Surface((self.width, self.height))
        self.button_color = button_color
        self.__selected_color = color.white
        self.draw()

    def selected(self):
        self.__selected_color, self.button_color = self.button_color, self.__selected_color

    def draw(self):
        text = TextObject(self.title, Settings.font, Settings.control_button_text_size, self.button_color)
        self.surface.fill(color.brick)
        self.surface.blit(text.Text, (10, 10))

    def pushed(self):
        self.func()
