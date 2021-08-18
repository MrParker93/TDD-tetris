from hashlib import new
import pyxel
import random
import constants


class Tetrominoes:
    """DESCRIPTION OF CLASS"""

    def __init__(self, shape=None):
        self.orientation = "RIGHT"

        if shape != None:
            self.shape = shape
        else:
            self.shape = random.choice(constants.BLOCK_NAME)

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

    def get_block_sections(self, position, orientation):
        block_name = self.shape + "_" + orientation
        block_sections = constants.BLOCKS[block_name]
        return {(section[0] + position[0], section[1] + position[1]) for section in block_sections}

    # Check the block can move in a specified direction

    def check_block_collision(self, block_sections, board):
        """DESCRIPTION OF METHOD"""
        for section in block_sections:
            if not (0 <= section[0] <= 12) or not (0 <= section[1] <= 20):
                return False
        return True

    def check_rotation_is_possible(self, rotation):
        """DESCRIPTION OF METHOD"""
        return True

    # Rotate the block depending on orientation

    def rotate(self, rotation, orientation, board):
        """DESCRIPTION OF METHOD"""
        if rotation == None:
            return

        o = orientation
        if rotation == "cw":
            if o == "RIGHT":
                new_orientation = "DOWN"
            elif o == "DOWN":
                new_orientation = "LEFT"
            elif o == "LEFT":
                new_orientation = "UP"
            elif o == "UP":
                new_orientation = "RIGHT"
        
        if rotation == "acw":
            if o == "RIGHT":
                new_orientation = "UP"
            elif o == "DOWN":
                new_orientation = "RIGHT"
            elif o == "LEFT":
                new_orientation = "DOWN"
            elif o == "UP":
                new_orientation = "LEFT"

        if self.check_block_collision(self.get_block_sections(self.position, new_orientation), board):
            self.orientation = new_orientation
            return True

        return False
