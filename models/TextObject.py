import pygame

class TextObject:
    def __init__(self, message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        self.Text = newFont.render(message, 0, textColor)

    def draw(self, surface, x, y):
        surface.blit(self.Text, (x, y))
