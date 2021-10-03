import pyxel
import random
from text import Text
from board import Board
from gamelogic import GameLogic

class App:
    WIDTH = 140
    HEIGHT = 200

    def __init__(self):
        pyxel.init(App.WIDTH, App.HEIGHT, caption="Tetris!", fps=60)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.b = Board()  # Initialise Board class that includes, blocks, board and collision checks
        self.l = GameLogic()  # Initialise GameLogic class to update level, fall speed, score, lines and combos
        self.text = Text(self.l.level, self.l.score, self.l.lines, self.l.combos)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
        if self.b.game_state == "running" or self.b.game_state == "stopped":
            if pyxel.btn(pyxel.KEY_R):
                self.reset()

        self.b.update()

    def draw(self):
        pyxel.cls(0)
        self.text.show()
        self.b.draw_board()
        self.b.draw_block()
        self.b.draw_next_block()
        self.draw_borders()

        if self.b.game_state == "paused":
            pyxel.text(App.WIDTH // 2 - 20, App.HEIGHT // 2 - 12, "PAUSED", pyxel.frame_count % 16)

    def draw_borders(self):
        
        # Create border for board
        pyxel.rectb(4, 8, self.b.WIDTH * 8, self.b.HEIGHT * 8, 5)
        
        # Create border for showing the next block
        pyxel.rectb(App.WIDTH * 0.66, 16, 37, 48, 5)

if __name__ == "__main__":
    App()