import pygame
import config.colors as color

from RunnableStack import RunnableStack
from runnable.ControlButton import ControlButton
from runnable.MainMenu import MainMenu
from runnable.TestMenu import TestMenu

FPS = 60
W = 800
H = 600

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
win = pygame.display.get_surface()



# Game cycle
runnable_stack = RunnableStack()
runnable_stack.push(MainMenu(W, H, runnable_stack, color.brick))

while not runnable_stack.is_empty():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    win.blit(runnable_stack.last_task().surface, (0, 0))
    runnable_stack.last_task().step()
    clock.tick(FPS)
