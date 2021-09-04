import pyxel
import random

#####################################
# SET GLOBAL VARIABLE GAME SETTINGS #
#####################################

# Size of the display window
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 220

# Area inside border where game is played
BOARD_GRID = [[1] * 10 for _ in range(20)]

# Height and width of the grid
BOARD_HEIGHT = len(BOARD_GRID)
BOARD_WIDTH = len(BOARD_GRID[0])

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

    "O_BLOCK": 56,
    "L_BLOCK": 80,
    "J_BLOCK": 128,
    "I_BLOCK": 144,
    "T_BLOCK": 184,
    "Z_BLOCK": 216,
    "S_BLOCK": 248
}

# Every block and every orientation for each
O_BLOCK = [
    [[56, 56],
     [56, 56]]
]

I_BLOCK = [
    [[0, 144, 0, 0],
     [0, 144, 0, 0],
     [0, 144, 0, 0],
     [0, 144, 0, 0]],

    [[0, 0, 0, 0],
     [144, 144, 144, 144],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

]

S_BLOCK = [
    [[248, 0, 0],
     [248, 248, 0],
     [0, 248, 0]],

    [[0, 248, 248],
     [248, 248, 0],
     [0, 0, 0]]
]

Z_BLOCK = [
    [[0, 216, 0],
     [216, 216, 0],
     [216, 0, 0]],

    [[216, 216, 0],
     [0, 216, 216],
     [0, 0, 0]]
]

L_BLOCK = [
    [[0, 80, 0],
     [0, 80, 0],
     [0, 80, 80]],

    [[0, 0, 0],
     [80, 80, 80],
     [80, 0, 0]],

    [[80, 80, 0],
     [0, 80, 0],
     [0, 80, 0]],

    [[0, 0, 80],
     [80, 80, 80],
     [0, 0, 0]]
]

J_BLOCK = [
    [[0, 128, 0],
     [0, 128, 0],
     [128, 128, 0]],

    [[128, 0, 0],
     [128, 128, 128],
     [0, 0, 0]],

    [[0, 128, 128],
     [0, 128, 0],
     [0, 128, 0]],

    [[0, 0, 0],
     [128, 128, 128],
     [0, 0, 128]],
]

T_BLOCK = [
    [[0, 184, 0],
     [0, 184, 184],
     [0, 184, 0]],

    [[0, 0, 0],
     [184, 184, 184],
     [0, 184, 0]],

    [[0, 184, 0],
     [184, 184, 0],
     [0, 184, 0]],

    [[0, 184, 0],
     [184, 184, 184],
     [0, 0, 0]]
]

BLOCKS = [O_BLOCK, I_BLOCK, S_BLOCK, Z_BLOCK, L_BLOCK, J_BLOCK, T_BLOCK]

print(f"This is black {int(pyxel.COLOR_BLACK)}")
print(f"This is brown {int(pyxel.COLOR_BROWN)}")
print(f"This is cyan {int(pyxel.COLOR_CYAN)}")
print(f"This is darkblue {int(pyxel.COLOR_DARKBLUE)}")
print(f"This is gray {int(pyxel.COLOR_GRAY)}")
print(f"This is green {int(pyxel.COLOR_GREEN)}")
print(f"This is lightblue {int(pyxel.COLOR_LIGHTBLUE)}")
print(f"This is lime {int(pyxel.COLOR_LIME)}")
print(f"This is navy {int(pyxel.COLOR_NAVY)}")
print(f"This is orange {int(pyxel.COLOR_ORANGE)}")
print(f"This is yellow {int(pyxel.COLOR_YELLOW)}")
print(f"This is peach {int(pyxel.COLOR_PEACH)}")
print(f"This is pink {int(pyxel.COLOR_PINK)}")
print(f"This is purple {int(pyxel.COLOR_PURPLE)}")
print(f"This is red {int(pyxel.COLOR_RED)}")
print(f"This is white {int(pyxel.COLOR_WHITE)}")
print(f"This is font width {int(pyxel.FONT_WIDTH)}")
print(f"This is font height {int(pyxel.FONT_HEIGHT)}")
