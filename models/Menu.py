import pygame
import config.colors as color
import config.settings as c
from models.TextObject import TextObject
from models.Button import Button

class Menu:
    def __init__(self, width, height, bg_color, background = None):
        self.menu_surface = pygame.display.set_mode((width, height))
        self.is_menu_running = False
        self.menu_surface.fill(bg_color)
        self.buttons = []
        self.menu_clock = pygame.time.Clock()
        self.title = TextObject("Sourcecodester", c.font, 90, color.yellow)

    def add_button(self, caption, event):
        button = Button(c.screen_width // 2, c.screen_height // 2, c.menu_button_width, c.menu_button_height, caption, color.yellow)
        button.draw(self.menu_surface)
        self.buttons.append(button)

    def run(self):
        self.is_menu_running = True
        selected = "start"

        while self.is_menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "start"
                    elif event.key == pygame.K_DOWN:
                        selected = "quit"
                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            print("Start")
                        if selected == "quit":
                            pygame.quit()
                            quit()

            for button in self.buttons:
                button.draw(self.menu_surface)

            pygame.display.update()
            self.menu_clock.tick(c.fps)
            pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")
