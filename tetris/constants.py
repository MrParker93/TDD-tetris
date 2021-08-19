import pyxel
import random
import pprint

#####################################
# SET GLOBAL VARIABLE GAME SETTINGS #
#####################################

# Size of the display window
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 220

# Size of each block
BLOCK_SIZE = 8

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

# Spawning position of blocks
STARTING_POSITION_X = (SCREEN_WIDTH // 12)
STARTING_POSITION_Y = (SCREEN_HEIGHT // 22)

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
ANTI_CLOCKWISE = "acw"

# Block pyxres image coordinates (u=0) this is value for v
PYXRES_VALUES = {

    "O_BLOCK": 0,
    "L_BLOCK": 24,
    "J_BLOCK": 72,
    "I_BLOCK": 88,
    "T_BLOCK": 128,
    "Z_BLOCK": 160,
    "S_BLOCK": 192
}

# Names of each block
BLOCK_NAME = ["O", "I", "S", "Z", "L", "J", "T"]

BLOCKS = {
    # Each orientation for O block
    "O_RIGHT": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "O_DOWN": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "O_LEFT": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "O_UP": [(0, 0), (0, 1), (1, 0), (1, 1)],

    # Each orientation for I block
    "I_RIGHT": [(0, 0), (0, 1), (0, 2), (0, 3)],
    "I_DOWN": [(0, 0), (1, 0), (2, 0), (3, 0)],
    "I_LEFT": [(0, 3), (0, 2), (0, 1), (0, 0)],
    "I_UP": [(3, 0), (2, 0), (1, 0), (0, 0)],

    # Each orientation for S block
    "S_RIGHT": [(2, 0), (1, 0), (1, 1), (0, 1)],
    "S_DOWN": [(0, 0), (0, 1), (1, 1), (1, 2)],
    "S_LEFT": [(0, 1), (1, 1), (1, 0), (2, 0)],
    "S_UP": [(1, 2), (1, 1), (0, 1), (0, 0)],

    # Each orientation for Z block
    "Z_RIGHT": [(0, 0), (1, 0), (1, 1), (2, 1)],
    "Z_DOWN": [(1, 0), (1, 1), (0, 1), (0, 2)],
    "Z_LEFT": [(2, 1), (1, 1), (1, 0), (0, 0)],
    "Z_UP": [(0, 2), (0, 1), (1, 1), (1, 0)],

    # Each orientation for L block
    "L_RIGHT": [(0, 0), (0, 1), (0, 2), (1, 2)],
    "L_DOWN": [(0, 0), (0, 1), (1, 0), (2, 0)],
    "L_LEFT": [(0, 0), (1, 0), (1, 1), (1, 2)],
    "L_UP": [(0, 1), (1, 1), (2, 1), (2, 0)],

    # Each orientation for J block
    "J_RIGHT": [(0, 2), (1, 2), (1, 1), (1, 0)],
    "J_DOWN": [(0, 0), (0, 1), (1, 1), (2, 1)],
    "J_LEFT": [(0, 0), (1, 0), (0, 1), (0, 2)],
    "J_UP": [(0, 0), (1, 0), (2, 0), (2, 1)],

    # Each orientation for T block
    "T_RIGHT": [(0, 0), (0, 1), (1, 1), (0, 2)],
    "T_DOWN": [(0, 0), (1, 1), (2, 0), (1, 0)],
    "T_LEFT": [(0, 1), (1, 0), (1, 1), (1, 2)],
    "T_UP": [(0, 1), (1, 1), (1, 0), (2, 1)]
}

# List of all the keys in blocks
BLOCK_OPTIONS = [blocks for blocks in BLOCKS.keys()]

# Randomly choose from all blocks facing right only
RANDOM_BLOCK = BLOCK_OPTIONS[random.randrange(0, 28, 4)]

