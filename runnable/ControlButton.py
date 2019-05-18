import pygame
import config.colors as color

from config.Resources import Constants
from pygame.surface import Surface
from models.TextObject import TextObject


class ControlButton:
    button_id = 0

    def __init__(self, title, name, x, y, width, height, button_color, font_color, func, background_image=None):
        self.title = title
        self.name = name
        self.id = ControlButton.button_id
        ControlButton.button_id += 1
        self.x = x
        self.y = y
        self.abs_x = x
        self.abs_y = y
        self.width = width
        self.height = height
        self.func = func
        self.button_color = button_color
        self.font_color = font_color
        self.__selected_color = color.white
        self.background_image = background_image
        if background_image:
            img_surf = pygame.image.load(background_image)
            self.surface = pygame.transform.scale(img_surf, (width, height))
        else:
            self.surface = Surface((self.width, self.height))
        self.draw()

    def selected(self):
        self.__selected_color, self.font_color = self.font_color, self.__selected_color

    def draw(self):
        if not self.background_image:
            text = TextObject(self.title, Constants.font, Constants.control_button_text_size, self.font_color)
            self.surface.fill(self.button_color)
            self.surface.blit(text.Text, (10, 10))

    def pushed(self):
        return self.func()
