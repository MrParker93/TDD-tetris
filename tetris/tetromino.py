import pyxel
import random
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, STARTING_LEVEL, SCORE, LINES, COMBOS, BLOCKS,
FALL_SPEED, DOWN, DOWN_LEFT, DOWN_RIGHT, RIGHT, LEFT, ANTICLOCKWISE, CLOCKWISE)


class Tetrominoes:
    """DESCRIPTION OF CLASS"""

    def __init__(self, block=None):
        if block != None:
            self.block = block
        else:
            self.block = random.sample(BLOCKS, 7).pop()

        self.position = (0, 0)
        self.orientation = random.randint(0, len(self.block) - 1)

    def move_block(self, direction, board):
        if direction == None:
            return

        if direction == RIGHT:
            new_position = (self.position[0] + 1, self.position[1])

        elif direction == LEFT:
            new_position = (self.position[0] - 1, self.position[1])

        elif direction == DOWN:
            new_position = (self.position[0], self.position[1] + 1)

        elif direction == DOWN_RIGHT:
            new_position = (self.position[0] + 1, self.position[1] + 1)

        elif direction == DOWN_LEFT:
            new_position = (self.position[0] - 1, self.position[1] + 1)

        if self.check_block_collision(self.get_block_sections(new_position), direction, board):
            self.position = new_position
            return True

        return False

    def get_block_sections(self, position, orientation=0):
        block = self.block[orientation]
        current_block = {
            "block": block,
            "rotation": orientation,
            "x": position[0],
            "y": position[1]
        }
        return current_block

    # Check the block can move in a specified direction
    def check_block_collision(self, block, direction, board):
        """DESCRIPTION OF METHOD"""
        return True
        # for section in block_sections:
        #     if not (0 <= section[0] <= (len(board[0]) - 1) // 8) or not (0 <= section[1] <= (len(board) - 1) // 8):
        #         return False
        # return True

    def block_falling(self, block, board):
        direction = DOWN
        if self.check_block_collision(block, direction, board):
            pass
        


    def check_rotation_is_possible(self, rotation):
        """DESCRIPTION OF METHOD"""
        pass

    # Rotate the block depending on orientation
    def rotate(self, rotation, orientation, board):
        """DESCRIPTION OF METHOD"""
        pass