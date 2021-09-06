import pyxel
import random
from text import Text
from board import Board
from gamelogic import GameLogic

class App:
    WIDTH = 180
    HEIGHT = 220

    def __init__(self):
        pyxel.init(App.WIDTH, App.HEIGHT, caption="Tetris!", fps=60)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.b = Board()  # Initialise Board class that includes, blocks, board and collision checks
        self.l = GameLogic()  # Initialise GameLogic class to update level, fall speed, score, lines and combos
        self.text = Text(self.l.level, self.l.score, self.l.lines, self.l.combos)
        self.game_state = "running"
        self.is_gameover = False

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_P):
            if self.game_state == "running" and not self.is_gameover:
                self.game_state = "paused"
            else:
                self.game_state = "running"
        
        if self.game_state == "running" or self.game_state == "stopped":
            if pyxel.btn(pyxel.KEY_R):
                self.reset()

        if self.game_state == "running":
            if pyxel.frame_count % self.l.fall_speed == 0:
                self.b.falling_block()

            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                if not self.b.check_collisions():
                    self.b.generate_block.move_block_left(self.b.block)

            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                if not self.b.check_collisions():
                    self.b.generate_block.move_block_right(self.b.block)
    def draw(self):
        pyxel.cls(0)
        self.text.show()
        self.b.draw_board()
        self.b.draw_block()
        self.b.draw_next_block()
        self.draw_borders()

        if self.game_state == "paused":
            pyxel.text(App.WIDTH // 2 - 20, App.HEIGHT // 2 - 12, "PAUSED", pyxel.frame_count % 16)

    def draw_borders(self):
        
        # Create border for board
        pyxel.rectb(4, 8, 120, 184, 5)
        
        # Create border for showing the next block
        pyxel.rectb(180 * 0.75, 16, 37, 48, 5)

if __name__ == "__main__":
    App()