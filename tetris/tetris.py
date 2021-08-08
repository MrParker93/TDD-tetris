import pyxel
import random


SCREEN_WIDTH = 120
SCREEN_HEIGHT = 180
BACKGROUND_COLOUR = pyxel.COLOR_BLACK
BLOCK_COLOUR = 


class Tetris:
    """Set up and run Tetris."""

    def __init__(self):
        """Initiate pyxel, set up game variables and run Tetris"""
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Tetris", fps=20)
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self. y = (self.y + 1) % pyxel.height

    def draw(self):
        pyxel.cls(BACKGROUND_COLOUR)
        pyxel.rect(60, 1, 12, 5, BLOCK_COLOUR)


Tetris()
