from runnable.ControlButton import ControlButton
from runnable.Game import Game
from runnable.Runnable import Runnable
from runnable.TestMenu import TestMenu


class MainMenu(Runnable):
    def __init__(self, width, height, runnable_stack):
        Runnable.__init__(self, width, height, runnable_stack)
        new_game_button = ControlButton("New game", "newgame", 200, 100, 200, 100,
                                        lambda: runnable_stack.push(Game(width, height, runnable_stack)))
        quit_button = ControlButton("Quit", "quit", 200, 250, 200, 100, lambda: runnable_stack.pop())
        self.add_control_button(new_game_button)
        self.add_control_button(quit_button)
