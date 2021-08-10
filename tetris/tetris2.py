import pyxel
import pprint
import random
from functions import colours

#####################################
# SET GLOBAL VARIABLE GAME SETTINGS #
#####################################

# Size of the display window
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 180

# Size of the border inside display window
BORDER_HEIGHT = 140
BORDER_WIDTH = 100

# Area inside border where game is played
GAMEPLAY_AREA_WIDTH = random.randrange(
    ((SCREEN_WIDTH / BORDER_WIDTH) + (SCREEN_WIDTH - BORDER_WIDTH)) // 2, (BORDER_WIDTH - 3))
print(GAMEPLAY_AREA_WIDTH)
GAMEPLAY_AREA_HEIGHT = random.randrange(
    ((SCREEN_HEIGHT / BORDER_HEIGHT) + (SCREEN_HEIGHT - BORDER_HEIGHT)) // 8, (BORDER_HEIGHT - 9))
print(GAMEPLAY_AREA_HEIGHT)
# Width and height of the blocks
BLOCK_WIDTH_AND_HEIGHT = (BORDER_WIDTH // 8)

# Set colours for different elements of the game
BORDER_COLOUR = pyxel.COLOR_NAVY
BACKGROUND_COLOUR = pyxel.COLOR_BLACK
LABEL_COLOUR = pyxel.COLOR_YELLOW
TEXT_COLOUR = pyxel.COLOR_GRAY

# Initial starting level (can be changed to increase difficulty)
STARTING_LEVEL = 0

# Movement speed of blocks
MOVEMENT_SPEED = 4


class Tetris:
    """"DESCRIPTION OF CLASS"""

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

    # Build each block using matrix
    blocks = [
        [[1, 1],
         [1, 1]],

        [[2, 0, 0],
         [2, 2, 2]],

        [[0, 0, 3],
         [3, 3, 3]],

        [[0, 4, 0],
         [4, 4, 4]],

        [[5, 5, 0],
         [0, 5, 5]],

        [[0, 6, 6],
         [6, 6, 0]],

        [[7, 7, 7, 7]]
    ]

    def __init__(self):
        """DESCRIPTION OF METHOD"""

        # Initialise Pyxel module with settings
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Tetris!", fps=50)

        # Creates a list from 0 - 7 (length of blocks list)
        self.block_supply = list(range(len(self.blocks)))

        # Shuffle the block supply to make it unordered
        random.shuffle(self.block_supply)

        # Select the last element from the shuffled list
        self.index = self.block_supply.pop()
        self.block = [row[:] for row in self.blocks[self.index]]
        pyxel.run(self.update, self.draw)

    def update(self):
        """DESCRIPTION OF METHOD"""

        # If 'Q' key is pressed, quit the application
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_R):
            pass

    def create_block(self):
        """DESCRIPTION OF METHOD"""

        for index, block in enumerate(self.block):
            if block != 0:
                pyxel.rect(GAMEPLAY_AREA_WIDTH, GAMEPLAY_AREA_HEIGHT, BLOCK_WIDTH_AND_HEIGHT,
                           BLOCK_WIDTH_AND_HEIGHT, self.block_colours[index])

    def draw(self):
        """DESCRIPTION OF METHOD"""

        pyxel.cls(BACKGROUND_COLOUR)
        pyxel.rectb(10, 5, BORDER_WIDTH, BORDER_HEIGHT, BORDER_COLOUR)
        self.create_block()


if __name__ == "__main__":
    Tetris()
