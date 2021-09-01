import pyxel
import random
from text import Text
from constants import *
from board import Board
from tetromino import Tetrominoes



class Tetris:
    """DESCRIPTION OF CLASS"""

    def __init__(self):
        """DESCRIPTION OF METHOD"""
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Tetris!", fps=60)
        pyxel.load("assets/shapes.pyxres")
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        """DESCRIPTION OF METHOD"""
        self.level = STARTING_LEVEL
        self.score = SCORE
        self.lines = LINES
        self.combos = COMBOS
        self.is_gameover = False
        self.game_state = "running"
        self.board = Board()
        self.bag = random.sample(BLOCKS, 7)
        self.block = Tetrominoes(shape=self.bag.pop())
        self.next_block = Tetrominoes(shape=self.bag.pop())
        self.direction = None
        self.rotation = None

    def update(self):
        """DESCRIPTION OF METHOD"""
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

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):

                if pyxel.btnp(pyxel.KEY_DOWN and pyxel.KEY_RIGHT, 10, 2):
                    self.direction = DOWN_RIGHT

                elif pyxel.btnp(pyxel.KEY_DOWN and pyxel.KEY_LEFT, 10, 2):
                    self.direction = DOWN_LEFT
                    
                else:
                    self.direction = DOWN

            elif pyxel.btnp(pyxel.KEY_RIGHT, 10, 2):
                self.direction = RIGHT

            elif pyxel.btnp(pyxel.KEY_LEFT, 10, 2):
                self.direction = LEFT

            if self.block.move_block(self.direction, self.board):
                if self.direction == DOWN or DOWN_LEFT or DOWN_RIGHT:
                    if self.game_over:
                        # DO SOMETHING
                        self.reset()
                        return
                    # self.set_block()
            
            if pyxel.btnp(pyxel.KEY_Z, 10, 2):
                self.rotation = ANTICLOCKWISE

            elif pyxel.btnp(pyxel.KEY_X, 10, 2):
                self.rotation = CLOCKWISE

            self.block.rotate(self.rotation, self.block.orientation, self.board)

    def draw(self):
        """DESCRIPTION OF METHOD"""
        pyxel.cls(0)
        self.board.draw_border()
        Text.show_text(self)
        self.board.draw_next_block()
        self.board.draw_block()

        if self.game_state == "paused":
            pyxel.text(50, 100, "PAUSED", pyxel.frame_count % 16)
        
        if self.is_gameover:
            self.game_state = "stopped"
            pyxel.cls(0)
            pyxel.text(45, 95, "GAMEOVER", pyxel.frame_count % 16)
            pyxel.text(45, 110, "Score: ", 6)
            pyxel.text(75, 110, str(self.score), 10)
            pyxel.text(45, 120, "Level: ", 6)
            pyxel.text(75, 120, str(self.level), 10)
            pyxel.text(45, 130, "Combos: ", 6)
            pyxel.text(75, 130, str(self.combos), 10)
            pyxel.text(45, 140, "Lines: ", 6)
            pyxel.text(75, 140, str(self.lines), 10)

            pyxel.text(12, 196, "Q: ", 10)
            pyxel.text(24, 196, "QUIT", 6)
            pyxel.text(66, 196, "R: ", 10)
            pyxel.text(78, 196, "RESTART", 6)


if __name__ == "__main__":
    Tetris()
