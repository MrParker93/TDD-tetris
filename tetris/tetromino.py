import pyxel
import random
from constants import *



class Tetrominoes:
    """DESCRIPTION OF CLASS"""

    def __init__(self, shape=None):
        if shape != None:
            self.shape = shape
        else:
            self.shape = random.sample(BLOCKS, 7).pop()

        self.position = (0, 3)
        self.orientation = random.randrange(0, len(shape))

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

        if self.check_block_collision(self.get_block_sections(new_position, self.orientation), board):
            self.position = new_position
            return True
        
        return False

    def get_block_sections(self, position, orientation):
        current_shape = self.shape[orientation]
        for index, tile in enumerate(current_shape):
            if tile[index] != 0:
                return
            
        
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
        