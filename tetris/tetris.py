import pyxel
import pprint
import random
import constants
from functions import colour_each_block


class Tetrominoes:
    """DESCRIPTION OF CLASS"""

    def __init__(self):
        pass


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
        self.game_state = "running"
        self.board = constants.BOARD_GRID
        self.movement_speed = constants.MOVEMENT_SPEED
        self.score = constants.SCORE
        self.x = constants.STARTING_POSITION_X
        self.y = constants.STARTING_POSITION_Y
        self.current_shape = None
        self.block_orientation = None

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

        self.direction = constants.NEUTRAL
        self.rotation = None

        if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):

            if pyxel.btnp(pyxel.KEY_DOWN and pyxel.KEY_RIGHT, 10, 2):
                if self.check_block_collision(constants.DOWN_RIGHT) == False:
                    self.direction = constants.DOWN_RIGHT
                    self.x = self.x + self.movement_speed
                    self.y = self.y + self.movement_speed

            elif pyxel.btnp(pyxel.KEY_DOWN and pyxel.KEY_LEFT, 10, 2):
                if self.check_block_collision(constants.DOWN_LEFT) == False:
                    self.direction = constants.DOWN_LEFT
                    self.x = self.x - self.movement_speed
                    self.y = self.y + self.movement_speed
            else:
                if self.check_block_collision(constants.DOWN):
                  self.direction = constants.DOWN
                  self.y = self.y + self.movement_speed

        if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2):
            if self.check_block_collision(constants.RIGHT) == False:
                self.direction = constants.RIGHT
                self.x = self.x + self.movement_speed

        if pyxel.btnp(pyxel.KEY_LEFT, 10, 2):
            if self.check_block_collision(constants.LEFT) == False:
                self.direction = constants.LEFT
                self.x = self.x - self.movement_speed

        if pyxel.btnp(pyxel.KEY_Z, 10, 2):
            if self.check_rotation_is_possible(constants.ANTI_CLOCKWISE) == True:
                self.rotation = constants.ANTI_CLOCKWISE
                self.rotate(self.current_shape, self.rotation, self.block_orientation)

        if pyxel.btnp(pyxel.KEY_X, 10, 2):
            if self.check_rotation_is_possible(constants.CLOCKWISE) == True:
                self.rotation = constants.CLOCKWISE
                self.rotate(self.current_shape, self.rotation, self.block_orientation)

    def check_block_collision(self, direction=constants.NEUTRAL):
        """DESCRIPTION OF METHOD"""
        board = self.board
        left_edge_of_the_board = constants.SCREEN_WIDTH - constants.BORDER_WIDTH
        if left_edge_of_the_board <= self.x >= len(board[0]):
            pass

    def check_rotation_is_possible(self, rotation):
        """DESCRIPTION OF METHOD"""
        pass

    def rotate(self, shape, rotation, orientation):
        """DESCRIPTION OF METHOD"""
        if shape == "O":
            return
        elif shape == "I" or shape == "S" or shape == "Z":
            if orientation == "RIGHT" or orientation == "LEFT":
                self.block_orientation = random.choice("UP" "DOWN")
            else:
                self.block_orientation = random.choice("LEFT" "RIGHT")
        else:
            if rotation == "cw":
                if orientation == "RIGHT":
                    self.block_orientation = "DOWN"
                elif orientation == "DOWN":
                    self.block_orientation = "LEFT"
                elif orientation == "LEFT":
                    self.block_orientation = "UP"
                elif orientation == "UP":
                    self.block_orientation = "RIGHT"
            else:
                if orientation == "RIGHT":
                    self.block_orientation = "UP"
                elif orientation == "DOWN":
                    self.block_orientation = "RIGHT"
                elif orientation == "LEFT":
                    self.block_orientation = "DOWN"
                elif orientation == "UP":
                    self.block_orientation = "LEFT"
        pass

    def draw_border_and_blocks(self):
        """"""
        pyxel.cls(0)
        pyxel.rectb(constants.SCREEN_WIDTH // 12, constants.SCREEN_HEIGHT // 22,
                    constants.BORDER_WIDTH, constants.BORDER_HEIGHT, constants.BORDER_COLOUR)

        for k, v in constants.BLOCKS.items():
            if k == constants.RANDOM_BLOCK:
                for coords in v:
                    pyxel.blt(
                        x=coords[0] * constants.BLOCK_SIZE + self.x,
                        y=coords[1] * constants.BLOCK_SIZE + self.y,
                        img=0,
                        u=0,
                        v=constants.T_BLOCK,
                        w=8,
                        h=8
                    )
                self.current_shape = k[:1]
                self.block_orientation = k[2:]

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
