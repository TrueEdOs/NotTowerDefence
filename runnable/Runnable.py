import pygame
from pygame.surface import Surface

import Utils


class Runnable:
    def __init__(self, width, height, runnable_stack):
        self.controls = []
        self.surface = Surface((width, height))
        self.runnable_stack = runnable_stack
        self.events = []

    def handle_player_events(self):
        pass

    def handle_control_button_events(self):
        for button in self.controls:
            for event in self.events:
                if event.type is pygame.MOUSEBUTTONDOWN and event.button == 1 \
                        and Utils.is_inside(event.pos, (button.x, button.y),
                                            (button.x + button.width, button.y + button.height)):
                    button.pushed()

    def update_state(self):
        pass

    def update_surface(self):
        pass

    def add_control_button(self, control_button):
        self.controls.append(control_button)
        self.surface.blit(control_button.surface, (control_button.x, control_button.y))
        pass

    def step(self):
        self.events = pygame.event.get()
        self.handle_control_button_events()
        self.handle_player_events()
        self.update_state()
        self.update_surface()
        self.events.clear()
