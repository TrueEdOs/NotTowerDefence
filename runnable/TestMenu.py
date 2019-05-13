import pygame

import Utils
from runnable.Runnable import Runnable


class TestMenu(Runnable):
    def handle_player_events(self):
        for i in self.events:
            if i.type == pygame.QUIT:
                self.runnable_stack.clear()

    def update_surface(self):

        img_surf = pygame.image.load("images/box.jpg")
        w400_h400 = Utils.fit_surface(img_surf, 400, 400)
        w200_h200 = Utils.fit_surface(img_surf, 200, 200)
        w300_h100 = Utils.fit_surface(img_surf, 300, 100)
        w150_h400 = Utils.fit_surface(img_surf, 150, 400)
        self.surface.blit(w400_h400, (0, 0))
        self.surface.blit(w200_h200, (420, 0))
        self.surface.blit(w300_h100, (0, 420))
        self.surface.blit(w150_h400, (320, 420))

