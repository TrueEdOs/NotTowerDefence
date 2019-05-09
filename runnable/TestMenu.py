import pygame
from runnable.Runnable import Runnable


class TestMenu(Runnable):
    def handle_player_events(self):
        for i in self.events:
            if i.type == pygame.QUIT:
                self.runnable_stack.clear()
