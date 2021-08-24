import pyxel
import random
import pprint
import copy

#####################################
# SET GLOBAL VARIABLE GAME SETTINGS #
#####################################

# Size of the display window
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 220

# Size of the border inside display window
BORDER_HEIGHT = 168
BORDER_WIDTH = 104

# Area inside border where game is played
BOARD_GRID = [[0] * BORDER_WIDTH for _ in range(BORDER_HEIGHT)]

# Set colours for different elements of the game
BORDER_COLOUR = pyxel.COLOR_NAVY
BACKGROUND_COLOUR = pyxel.COLOR_BLACK
LABEL_COLOUR = pyxel.COLOR_YELLOW
TEXT_COLOUR = pyxel.COLOR_GRAY

# Initial starting level (can be changed to increase difficulty)
STARTING_LEVEL = 0

# Inital score
SCORE = 0

# Movement speed of blocks
MOVEMENT_SPEED = 2

# Directions
RIGHT = "right"
DOWN_RIGHT = "downRight"
DOWN = "down"
DOWN_LEFT = "downLeft"
LEFT = "left"

# Rotations
CLOCKWISE = "cw"

# Block pyxres image coordinates (u=0) this is value for v
PYXRES_VALUES = {

    "O_BLOCK": 8,
    "L_BLOCK": 24,
    "J_BLOCK": 72,
    "I_BLOCK": 88,
    "T_BLOCK": 128,
    "Z_BLOCK": 160,
    "S_BLOCK": 192
}


BLOCKS = [
    # O block
    [
        [8, 8],
        [8, 8]
    ],

    # I block
    [
        [0, 0, 0, 0],
        [88, 88, 88, 88],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],

    # S block
    [
        [0, 192, 192],
        [192, 192, 0],
        [0, 0, 0],
    ],

    # Z block
    [
        [160, 160, 0],
        [0, 160, 160],
        [0, 0, 0]
    ],

    # L block
    [
        [24, 0, 0],
        [24, 0, 0],
        [24, 24, 0],
    ],

    # J block
    [
        [0, 72, 0],
        [0, 72, 0],
        [72, 72, 0],
    ],

    # T block
    [
        [0, 128, 0],
        [128, 128, 128],
        [0, 0, 0]
    ]
]

# for blocks in BLOCKS:
#     print(blocks)
#     for section in blocks:
#         print(section)
