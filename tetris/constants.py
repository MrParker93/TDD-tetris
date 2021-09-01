import pyxel
import random

#####################################
# SET GLOBAL VARIABLE GAME SETTINGS #
#####################################

# Size of the display window
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 220

# Area inside border where game is played
BOARD_GRID = [[0] * 10 for _ in range(20)]

# Height and width of the grid
BOARD_HEIGHT = len(BOARD_GRID)
BOARD_WIDTH = len(BOARD_GRID[0])

# Area displaying the next block
NEXT_GRID = [[4] * 4 for _ in range(6)]

# Set colours for different elements of the game
BORDER_COLOUR = pyxel.COLOR_NAVY
BACKGROUND_COLOUR = pyxel.COLOR_BLACK
LABEL_COLOUR = pyxel.COLOR_YELLOW
TEXT_COLOUR = pyxel.COLOR_GRAY

# Initial starting level (can be changed to increase difficulty)
STARTING_LEVEL = 0

# Inital score, lines and combos
SCORE = 0
LINES = 0
COMBOS = 0

# Movement speed of blocks, fall speed of blocks
MOVEMENT_SPEED = 2
FALL_SPEED = 10

# Directions
RIGHT = "RIGHT"
DOWN_RIGHT = "DOWNRIGHT"
DOWN = "DOWN"
DOWN_LEFT = "DOWNLEFT"
LEFT = "LEFT"

# Rotations
CLOCKWISE = "CW"
ANTICLOCKWISE = "ACW"

# Block pyxres image coordinates (u=0) this is value for v in pyxel.blt()
PYXRES_VALUES = {

    "O_BLOCK": 8,
    "L_BLOCK": 24,
    "J_BLOCK": 72,
    "I_BLOCK": 88,
    "T_BLOCK": 128,
    "Z_BLOCK": 160,
    "S_BLOCK": 192
}

# Every block and every orientation for each
O_BLOCK = [
    [[8, 8],
     [8, 8]]
]

I_BLOCK = [
    [[0, 88, 0, 0],
     [0, 88, 0, 0],
     [0, 88, 0, 0],
     [0, 88, 0, 0]],

    [[0, 0, 0, 0],
     [88, 88, 88, 88],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

]

S_BLOCK = [
    [[0, 192, 192],
     [192, 192, 0],
     [0, 0, 0]],

    [[192, 0, 0],
     [192, 192, 0],
     [0, 192, 0]]
]

Z_BLOCK = [
    [[160, 160, 0],
     [0, 160, 160],
     [0, 0, 0]],

    [[0, 160, 0],
     [160, 160, 0],
     [160, 0, 0]]
]

L_BLOCK = [
    [[0, 24, 0],
     [0, 24, 0],
     [0, 24, 24]],

    [[0, 0, 0],
     [24, 24, 24],
     [24, 0, 0]],

    [[24, 24, 0],
     [0, 24, 0],
     [0, 24, 0]],

    [[0, 0, 24],
     [24, 24, 24],
     [0, 0, 0]]
]

J_BLOCK = [
    [[0, 72, 0],
     [0, 72, 0],
     [72, 72, 0]],

    [[72, 0, 0],
     [72, 72, 72],
     [0, 0, 0]],

    [[0, 72, 72],
     [0, 72, 0],
     [0, 72, 0]],

    [[0, 0, 0],
     [72, 72, 72],
     [0, 0, 72]],
]

T_BLOCK = [
    [[0, 128, 0],
     [128, 128, 128],
     [0, 0, 0]],

    [[0, 128, 0],
     [0, 128, 128],
     [0, 128, 0]],

    [[0, 0, 0],
     [128, 128, 128],
     [0, 128, 0]],

    [[0, 128, 0],
     [128, 128, 0],
     [0, 128, 0]]
]

BLOCKS = [O_BLOCK, I_BLOCK, S_BLOCK, Z_BLOCK, L_BLOCK, J_BLOCK, T_BLOCK]
