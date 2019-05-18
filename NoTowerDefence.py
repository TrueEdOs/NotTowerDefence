import pygame

import Resources
import config.colors as color

from RunnableStack import RunnableStack
from runnable.ControlButton import ControlButton
from runnable.MainMenu import MainMenu
from config.settings import Settings
from runnable.TestMenu import TestMenu
from runnable.Authorization import Authorization
from units.Zombie import Zombie


#Authorization()
pygame.init()
sc = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
clock = pygame.time.Clock()
win = pygame.display.get_surface()

# Game cycle

runnable_stack = RunnableStack()
runnable_stack.push(MainMenu(Settings.screen_width, Settings.screen_height, runnable_stack, color.brick))

while not runnable_stack.is_empty():
    pygame.display.update()
    win.blit(runnable_stack.last_task().surface,
             (runnable_stack.last_task().x, runnable_stack.last_task().y))
    runnable_stack.last_task().step()
    clock.tick(Settings.fps)
