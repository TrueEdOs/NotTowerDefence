import pygame
from pygame.surface import Surface


class ControlButton:
    button_id = 0

    def __init__(self, title, name, x, y, width, height, func):
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
        self.draw()

    def draw(self):
        font = pygame.font.SysFont("arial", 15)
        text = font.render(self.title, 0, (255, 255, 255))
        self.surface.fill((255, 0, 0))
        self.surface.blit(text, (10, 10))

    def pushed(self):
        self.func()
