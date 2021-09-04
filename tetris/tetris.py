import pyxel
import random
from text import Text
from board import Board
from gamelogic import GameLogic
from tetrimino import Tetrimino

class App:
    WIDTH = 180
    HEIGHT = 220

    def __init__(self):
        pyxel.init(App.WIDTH, App.HEIGHT, caption="Tetris!", fps=60)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.b = Board()  # Initialise Board class that includes, blocks, board and collision checks
        self.l = GameLogic()  # Initialise GameLogic class to update level, score, lines and combos
        self.text = Text(self.l.level, self.l.score, self.l.lines, self.l.combos)
        
    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_R):
            self.reset()

    def draw(self):
        pyxel.cls(0)
        self.text.show()
        self.b.draw_board()
        self.b.create_board()
        self.b.draw_next_block()
        self.draw_borders()

    def draw_borders(self):
        
        # Create border for board
        pyxel.rectb(4, 8, 120, 184, 5)
        
        # Create border for showing the next block
        pyxel.rectb(180 * 0.75, 16, 37, 48, 5)

if __name__ == "__main__":
    App()