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
        pyxel.init(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                   caption="Tetris!", fps=60)
        pyxel.load("assets/shapes.pyxres")
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.game_state = "running"
        self.score = constants.SCORE
        self.x = constants.FALL_POSITION
        # self.y =
        pass

    def update(self):

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
                if self.check_block_collision() == False:
                    self.direction = constants.DOWN_RIGHT
            elif pyxel.btnp(pyxel.KEY_DOWN and pyxel.KEY_LEFT, 10, 2):
                if self.check_block_collision() == False:
                    self.direction = constants.DOWN_LEFT
            else:
                self.direction = constants.DOWN

        if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2):
            if self.check_block_collision() == False:
                self.direction = constants.RIGHT

        if pyxel.btnp(pyxel.KEY_LEFT, 10, 2):
            if self.check_block_collision() == False:
                self.direction = constants.LEFT

        if pyxel.btnp(pyxel.KEY_Z, 10, 2):
            if self.check_rotation_is_possible() == True:
                self.rotation = constants.ANTI_CLOCKWISE

        if pyxel.btnp(pyxel.KEY_X, 10, 2):
            if self.check_rotation_is_possible() == True:
                self.rotation = constants.CLOCKWISE

    def check_block_collision(self, direction=constants.NEUTRAL):
        pass

    def check_rotation_is_possible(self, rotation_direction):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.rectb(constants.SCREEN_WIDTH // 12, constants.SCREEN_HEIGHT // 22,
                    constants.BORDER_WIDTH, constants.BORDER_HEIGHT, constants.BORDER_COLOUR)

        for k, v in constants.BLOCKS.items():
            if k == "T_DOWN":
                for coords in v:
                    pyxel.blt(
                        x=coords[0] * constants.BLOCK_SIZE * self.x,
                        y=coords[1] * constants.BLOCK_SIZE * self.x,
                        img=0,
                        u=0,
                        v=constants.T_BLOCK,
                        w=8,
                        h=8
                    )

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
