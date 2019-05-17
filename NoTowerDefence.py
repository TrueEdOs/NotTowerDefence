import pygame

import Resources
import config.colors as color

from RunnableStack import RunnableStack
from runnable.ControlButton import ControlButton
from runnable.MainMenu import MainMenu
from runnable.TestMenu import TestMenu
from runnable.Authorization import Authorization
from units.Zombie import Zombie

FPS = 60
W = Resources.Constants.display_width
H = Resources.Constants.display_height

Authorization()
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
win = pygame.display.get_surface()

# Game cycle

runnable_stack = RunnableStack()
runnable_stack.push(MainMenu(W, H, runnable_stack, color.brick))

while not runnable_stack.is_empty():
    pygame.display.update()
    win.blit(runnable_stack.last_task().surface, (0, 0))
    runnable_stack.last_task().step()
    clock.tick(FPS)
