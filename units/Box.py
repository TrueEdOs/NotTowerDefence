import pygame
from units.Unit import Unit


class Box(Unit):
    def __init__(self, game, controller, hp, x, y, width, height, texture_path):
        Unit.__init__(self, game, controller, hp, x, y, width, height)
        self.texture_path = texture_path

    def draw(self):
        box_surf = pygame.image.load(self.texture_path)

        pygame.draw.circle(box_surf, (30, 90, 150), (40, 40), 40)
        box_rect = box_surf.get_rect(topleft=(self.width, self.height))
        self.game.surface.blit(box_surf, box_rect)
