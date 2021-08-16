from constants import BLOCKS
import pyxel
import random
import constants



# Check the block can move in a specified direction


def check_block_collision(board, x, y, direction=constants.NEUTRAL):
    """DESCRIPTION OF METHOD"""

    if direction == "left":
        if x < 0 :
            return True

    if direction == "right":
        if x > len(board[0]):
            return True

    if direction == "down":
        if y >= len(board):
            return True

    if direction == "downRight":
        if x >= len(board[0]):
            return True
        if y >= len(board):
            return True

    if direction == "downLeft":
        if x <= 0:
            return True
        if y >= len(board):
            return True
    return False


def check_rotation_is_possible(rotation):
    """DESCRIPTION OF METHOD"""
    return True


# Rotate the block depending on orientation
def rotate(shape, rotation, orientation):
    """DESCRIPTION OF METHOD"""
    if shape == "O":
        return orientation
    elif shape == "I" or shape == "S" or shape == "Z":
        if orientation == "RIGHT" or orientation == "LEFT":
            orientation = random.choice("UP" "DOWN")
            return orientation
        else:
            orientation = random.choice("LEFT" "RIGHT")
            return orientation
    else:
        if rotation == "cw":
            if orientation == "RIGHT":
                orientation = "DOWN"
                return orientation
            elif orientation == "DOWN":
                orientation = "LEFT"
                return orientation
            elif orientation == "LEFT":
                orientation = "UP"
                return orientation
            elif orientation == "UP":
                orientation = "RIGHT"
                return orientation
        else:
            if orientation == "RIGHT":
                orientation = "UP"
                return orientation
            elif orientation == "DOWN":
                orientation = "RIGHT"
                return orientation
            elif orientation == "LEFT":
                orientation = "DOWN"
                return orientation
            elif orientation == "UP":
                orientation = "LEFT"
                return orientation


# Set colours for each block
block_colours = [
    pyxel.COLOR_DARKBLUE,
    pyxel.COLOR_ORANGE,
    pyxel.COLOR_YELLOW,
    pyxel.COLOR_LIGHTBLUE,
    pyxel.COLOR_LIME,
    pyxel.COLOR_RED,
    pyxel.COLOR_PURPLE
]

# Colours each block shape


def colour_each_block(num):
    colours = {str(index): colours for index,
               colours in enumerate(block_colours, start=1)}
    if str(num) in colours.keys():
        return colours[str(num)]


shape = (
    ("O", "X", "O"),
    ("X", "X", "X"),
    ("O", "O", "O")
)

# print(shape[0])
# print(shape[1])
# print(shape[2])
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# face_right = tuple(zip(*shape[::-1]))
# print(face_right[0])
# print(face_right[1])
# print(face_right[2])
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# face_down = tuple(zip(*face_right[::-1]))
# print(face_down[0])
# print(face_down[1])
# print(face_down[2])
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# face_left = tuple(zip(*shape[::1]))
# print(face_left[0])
# print(face_left[1])
# print(face_left[2])

# print(random.choice("a" "b"))
