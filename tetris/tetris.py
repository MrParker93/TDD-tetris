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
        self.board = constants.BOARD_GRID
        self.score = constants.SCORE
        self.game_state = "running"
        self.block = Tetrominoes(shape=random.choice(constants.BLOCK_NAME))

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

        self.block.move_block(self.direction, self.board)
        
        if pyxel.btnp(pyxel.KEY_Z, 10, 2):
            self.rotation = constants.ANTI_CLOCKWISE

        elif pyxel.btnp(pyxel.KEY_X, 10, 2):
            self.rotation = constants.CLOCKWISE

        self.block.rotate(self.rotation, self.block.orientation, self.board)
        
    def draw_border_and_blocks(self):
        """"""
        pyxel.cls(0)
        pyxel.rectb(8, 8, constants.BORDER_WIDTH, constants.BORDER_HEIGHT, constants.BORDER_COLOUR)

        current_block = self.block.get_block_sections(self.block.position, self.block.orientation)

        for section in current_block:
            pyxel.blt(
                        x=section[0] * constants.BLOCK_SIZE + 8,
                        y=section[1] * constants.BLOCK_SIZE + 8,
                        img=0,
                        u=0,
                        v=constants.PYXRES_VALUES[self.block.shape + "_BLOCK"],
                        w=8,
                        h=8,
                    )

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
