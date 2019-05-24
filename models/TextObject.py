import pygame

class TextObject:
    def __init__(self, message, textFont, textSize, textColor):
        new_font = pygame.font.Font(textFont, textSize)
        self.Text = new_font.render(message, 0, textColor)

    def draw(self, surface, x, y):
        surface.blit(self.Text, (x, y))
