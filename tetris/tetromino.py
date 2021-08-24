from hashlib import new
import pyxel
import random
import constants


class Tetrominoes:
    """DESCRIPTION OF CLASS"""

    def __init__(self, shape=None):

        if shape != None:
            self.shape = shape
        else:
            self.shape = random.randrange(7)

        self.position = (0, 0)

    def move_block(self, direction, board):
        if direction == None:
            return

        if direction == "right":
            new_position = (self.position[0] + 1, self.position[1])

        elif direction == "left":
            new_position = (self.position[0] - 1, self.position[1])

        elif direction == "down":
            new_position = (self.position[0], self.position[1] + 1)

        elif direction == "downRight":
            new_position = (self.position[0] + 1, self.position[1] + 1)

        elif direction == "downLeft":
            new_position = (self.position[0] - 1, self.position[1] + 1)

        if self.check_block_collision(self.get_block_sections(new_position, self.orientation), board):
            self.position = new_position
            return True
        
        return False

    def get_block_sections(self, shape):
        return constants.BLOCKS[shape]
        
    # Check the block can move in a specified direction

    def check_block_collision(self, block_sections, board):
        """DESCRIPTION OF METHOD"""
        for section in block_sections:
            if not (0 <= section[0] <= (len(board[0]) - 1) // 8) or not (0 <= section[1] <= (len(board) - 1) // 8):
                return False
        return True

    def check_rotation_is_possible(self, rotation):
        """DESCRIPTION OF METHOD"""
        return True

    # Rotate the block depending on orientation

    def rotate(self, rotation, orientation, board):
        """DESCRIPTION OF METHOD"""
        