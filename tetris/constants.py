import pyxel
import random

#####################################
# SET GLOBAL VARIABLE GAME SETTINGS #
#####################################

# Size of the display window
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 220

# Size of each block
BLOCK_SIZE = 8

# Size of the border inside display window
BORDER_HEIGHT = 165
BORDER_WIDTH = 100

# Area inside border where game is played
BOARD_GRID = [[0] * BORDER_WIDTH for _ in range(BORDER_HEIGHT)]
print(len(BOARD_GRID[0]))
print(len(BOARD_GRID))

# Set colours for different elements of the game
BORDER_COLOUR = pyxel.COLOR_NAVY
BACKGROUND_COLOUR = pyxel.COLOR_BLACK
LABEL_COLOUR = pyxel.COLOR_YELLOW
TEXT_COLOUR = pyxel.COLOR_GRAY

# Initial starting level (can be changed to increase difficulty)
STARTING_LEVEL = 0

# Spawning position of blocks
STARTING_POSITION_X = (SCREEN_WIDTH // BORDER_WIDTH) * (BORDER_WIDTH // 2)
STARTING_POSITION_Y = (SCREEN_HEIGHT // BORDER_HEIGHT) * 4

# Inital score
SCORE = 0

# Movement speed of blocks
MOVEMENT_SPEED = 4

# Directions
NEUTRAL = None
RIGHT = "right"
DOWN_RIGHT = "downRight"
DOWN = "down"
DOWN_LEFT = "downLeft"
LEFT = "left"

# Rotations
CLOCKWISE = "cw"
ANTI_CLOCKWISE = "acw"

# Block pyxres image coordinates (u=0) this is value for v
O_BLOCK = 0
L_BLOCK = 24
J_BLOCK = 72
I_BLOCK = 88
T_BLOCK = 128
Z_BLOCK = 160
S_BLOCK = 192

# Names of each block
BLOCK_NAME = ["O", "I", "S", "Z", "L", "J", "T"]

BLOCKS = {
    # Each orientation for O block
    "O_RIGHT": {(0, 1), (1, 1), (0, 2), (1, 2)},
    "O_DOWN": {(0, 1), (1, 1), (0, 2), (1, 2)},
    "O_LEFT": {(0, 1), (1, 1), (0, 2), (1, 2)},
    "O_UP": {(0, 1), (1, 1), (0, 2), (1, 2)},

    # Each orientation for I block
    "I_RIGHT": {(1, 0), (1, 1), (1, 2), (1, 3)},
    "I_DOWN": {(0, 2), (1, 2), (2, 2), (3, 2)},
    "I_LEFT": {(1, 0), (1, 1), (1, 2), (1, 3)},
    "I_UP": {(0, 2), (1, 2), (2, 2), (3, 2)},

    # Each orientation for S block
    "S_RIGHT": {(2, 0), (1, 0), (1, 1), (0, 1)},
    "S_DOWN": {(1, 0), (1, 1), (2, 1), (2, 2)},
    "S_LEFT": {(2, 0), (1, 0), (1, 1), (0, 1)},
    "S_UP": {(1, 0), (1, 1), (2, 1), (2, 2)},

    # Each orientation for Z block
    "Z_RIGHT": {(0, 0), (1, 0), (1, 1), (2, 1)},
    "Z_DOWN": {(1, 0), (1, 1), (0, 1), (0, 2)},
    "Z_LEFT": {(0, 0), (1, 0), (1, 1), (2, 1)},
    "Z_UP": {(1, 0), (1, 1), (0, 1), (0, 2)},

    # Each orientation for L block
    "L_RIGHT": {(1, 0), (1, 1), (1, 2), (2, 2)},
    "L_DOWN": {(3, 2), (2, 2), (1, 2), (1, 3)},
    "L_LEFT": {(1, 1), (2, 1), (2, 2), (2, 3)},
    "L_UP": {(0, 2), (1, 2), (2, 2), (2, 1)},

    # Each orientation for J block
    "J_RIGHT": {(2, 0), (1, 0), (1, 1), (1, 2)},
    "J_DOWN": {(0, 1), (1, 1), (2, 1), (2, 2)},
    "J_LEFT": {(1, 0), (1, 1), (1, 2), (0, 2)},
    "J_UP": {(1, 0), (1, 1), (2, 1), (3, 1)},

    # Each orientation for T block
    "T_RIGHT": {(1, 0), (1, 1), (2, 1), (1, 2)},
    "T_DOWN": {(0, 1), (1, 1), (2, 1), (1, 2)},
    "T_LEFT": {(1, 0), (1, 1), (0, 1), (1, 2)},
    "T_UP": {(0, 1), (1, 1), (1, 0), (2, 1)}
}

BLOCK_OPTIONS = [blocks for blocks in BLOCKS.keys()]
RANDOM_BLOCK = BLOCK_OPTIONS[random.randrange(0, 28, 4)]
