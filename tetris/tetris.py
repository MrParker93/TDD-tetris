import pyxel
import random
from text import Text
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, STARTING_LEVEL, SCORE, LINES, COMBOS, BLOCKS,
FALL_SPEED, DOWN, DOWN_LEFT, DOWN_RIGHT, RIGHT, LEFT, ANTICLOCKWISE, CLOCKWISE)
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
        self.bag = random.sample(BLOCKS, 7)
        self.block = Tetrominoes(block=self.bag.pop())
        self.next_block = Tetrominoes(block=self.bag.pop())
        self.board = Board(self.block, self.next_block)
        self.position_x = self.block.position[0]
        self.position_y = self.block.position[1]
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

            if pyxel.frame_count % FALL_SPEED == 0:
                self.block.block_falling(self.block.get_block_sections(self.block.position), self.board.board)

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                
                if pyxel.btnp(pyxel.KEY_DOWN and pyxel.KEY_RIGHT, 10, 2):
                    self.direction = DOWN_RIGHT
                    self.block.move_block(self.direction, self.board.board)

                elif pyxel.btnp(pyxel.KEY_DOWN and pyxel.KEY_LEFT, 10, 2):
                    self.direction = DOWN_LEFT
                    self.block.move_block(self.direction, self.board.board)
                    
                else:
                    self.direction = DOWN
                    self.block.move_block(self.direction, self.board.board)

            elif pyxel.btnp(pyxel.KEY_RIGHT, 10, 2):
                self.direction = RIGHT
                self.block.move_block(self.direction, self.board.board)

            elif pyxel.btnp(pyxel.KEY_LEFT, 10, 2):
                self.direction = LEFT
                self.block.move_block(self.direction, self.board.board)
            
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
        self.board.draw_block(self.position_x, self.position_y)
        self.board.draw_next_block()
        
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
