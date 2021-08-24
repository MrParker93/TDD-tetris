import pyxel
import pprint
import random
import constants
from tetromino import Tetrominoes



class Tetris:
    """DESCRIPTION OF CLASS"""

    def __init__(self):
        """DESCRIPTION OF METHOD"""
        pyxel.init(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                   caption="Tetris!", fps=60)
        pyxel.load("assets/shapes.pyxres")
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        """DESCRIPTION OF METHOD"""
        self.score = constants.SCORE
        self.game_state = "running"
        self.game_over = False
        self.board = [[0] * 12 for _ in range(21)]
        self.bag = random.sample(range(7), 7)

        self.block = Tetrominoes(shape=self.bag.pop())

    def update(self):
        """DESCRIPTION OF METHOD"""
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
            
        if pyxel.btn(pyxel.KEY_R):
            self.reset()

        if pyxel.btn(pyxel.KEY_P):
            if self.game_state == "running":
                self.game_state == "paused"
            else:
                self.game_state == "running"

        if self.game_state == "paused":
            return
        
        self.direction = None
        self.rotation = None
    
        if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):

            if pyxel.btnp(pyxel.KEY_DOWN and pyxel.KEY_RIGHT, 10, 2):
                self.direction = constants.DOWN_RIGHT

            elif pyxel.btnp(pyxel.KEY_DOWN and pyxel.KEY_LEFT, 10, 2):
                self.direction = constants.DOWN_LEFT
                   
            else:
                self.direction = constants.DOWN

        elif pyxel.btnp(pyxel.KEY_RIGHT, 10, 2):
            self.direction = constants.RIGHT

        elif pyxel.btnp(pyxel.KEY_LEFT, 10, 2):
            self.direction = constants.LEFT

        if self.block.move_block(self.direction, self.board):
            if self.direction == constants.DOWN or constants.DOWN_LEFT or constants.DOWN_RIGHT:
                if self.game_over:
                    # DO SOMETHING
                    self.reset()
                    return
                # self.set_block()
        
        if pyxel.btnp(pyxel.KEY_Z, 10, 2):
            self.rotation = constants.ANTI_CLOCKWISE

        elif pyxel.btnp(pyxel.KEY_X, 10, 2):
            self.rotation = constants.CLOCKWISE

        self.block.rotate(self.rotation, self.block.orientation, self.board)
        
    def draw_border_and_blocks(self):
        """"""
        pyxel.cls(0)
        
        pyxel.rectb(8, 8, constants.BORDER_WIDTH, constants.BORDER_HEIGHT, constants.BORDER_COLOUR)

        current_block = self.block.get_block_sections(self.block.shape)

        for row in range(21):
            for col in range(12):
                if self.board[row][col] != 0:
                    pyxel.blt((row * 8) + 8, (col * 8) + 8, 0, 0, self.board[row][col])
    
    def set_block(self):
        for section in self.block.get_block_sections(self.block.position, self.block.orientation):
            self.board[section[1]][section[0]] = 1



    def draw(self):
        """DESCRIPTION OF METHOD"""
        self.draw_border_and_blocks()

        # Show current score
        pyxel.text(constants.SCREEN_WIDTH // 3, (constants.SCREEN_HEIGHT / 18) *
                   15.5, "SCORE :", constants.LABEL_COLOUR)
        pyxel.text((constants.SCREEN_WIDTH // 3) * 1.8, (constants.SCREEN_HEIGHT / 18)
                   * 15.5, str(self.score), constants.TEXT_COLOUR)

        # How to quit the application
        pyxel.text((constants.SCREEN_WIDTH // 18), (constants.SCREEN_HEIGHT / 18) * 16.5,
                   "Q:", constants.LABEL_COLOUR)
        pyxel.text((constants.SCREEN_WIDTH // 18) * 2.5, (constants.SCREEN_HEIGHT / 18) * 16.5,
                   "QUIT", constants.TEXT_COLOUR)

        # How to pause the application
        pyxel.text((constants.SCREEN_WIDTH // 6) * 2, (constants.SCREEN_HEIGHT / 18) * 16.5,
                   "P:", constants.LABEL_COLOUR)
        pyxel.text((constants.SCREEN_WIDTH // 6) * 2.5, (constants.SCREEN_HEIGHT / 18) * 16.5,
                   "PAUSE", constants.TEXT_COLOUR)

        # How to restart the application
        pyxel.text((constants.SCREEN_WIDTH // 9) * 6, (constants.SCREEN_HEIGHT / 18) * 16.5,
                   "R:", constants.LABEL_COLOUR)
        pyxel.text((constants.SCREEN_WIDTH // 9) * 6.8, (constants.SCREEN_HEIGHT / 18) * 16.5,
                   "RESTART", constants.TEXT_COLOUR)


if __name__ == "__main__":
    Tetris()
