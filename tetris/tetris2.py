import pyxel
import pprint
import random
from functions import colour_each_block, game_text

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
BOARD_GRID = [[0] * BORDER_WIDTH for _ in range(BORDER_HEIGHT)]

# Width and height of the blocks
BLOCK_WIDTH_AND_HEIGHT = (BORDER_WIDTH // 8)

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
MOVEMENT_SPEED = 4


class Tetris:
    """"DESCRIPTION OF CLASS"""

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

        # Reset the game settings
        self.reset()

        # Run the game
        pyxel.run(self.update, self.draw)

    def reset(self):
        """DESCRIPTION OF METHOD"""
        self.board = BOARD_GRID
        self.score = SCORE
        self.level = STARTING_LEVEL
        self.gameover = False

        # Creates a list from 0 - 7 (number of blocks)
        self.block_supply = list(range(len(self.blocks)))

        # Shuffle the block supply to make it unordered
        random.shuffle(self.block_supply)

        # Select random block from supply
        self.index = self.block_supply.pop()

        # Create a list of selected block
        self.block = [row[:] for row in self.blocks[self.index]]

    def update(self):
        """DESCRIPTION OF METHOD"""

        # If 'Q' key is pressed, quit the application
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        # If 'R' key is pressed, reset the application
        if pyxel.btn(pyxel.KEY_R):
            pass

    def create_block(self):
        """DESCRIPTION OF METHOD"""

        board = self.board
        for each_row in range(len(self.block)):
            for each_element in range(len(self.block[each_row])):
                board[each_row + 0][each_element + BORDER_WIDTH // 2 -
                                    len(self.block[0])] = self.block[each_row][each_element]
        
        # for block in self.block:
        #     #     print(f"This/these are the block(s): {block}")
        #     for section in block:
        #         #         print(f"This is the index: {index}")
        #         print(f"This is each section: {section}")
        #         if section != 0:
        #             pyxel.rect(
        #                 x=80,
        #                 y=10,
        #                 w=8,
        #                 h=8,
        #                 col=colour_each_block(section)
        #             )
        #             pyxel.rect(
        #                 x=60,
        #                 y=50,
        #                 w=4,
        #                 h=4,
        #                 col=colour_each_block(section)
        #             )

    def draw_score_and_options(self):
        """DESCRIPTION OF METHOD"""

        # Show current score
        pyxel.text(SCREEN_WIDTH // 3, (SCREEN_HEIGHT / 18) *
                   15.5, game_text["score_label"], LABEL_COLOUR)
        pyxel.text((SCREEN_WIDTH // 3) * 1.8, (SCREEN_HEIGHT / 18)
                   * 15.5, str(self.score), TEXT_COLOUR)

        # Show what key quits the game
        pyxel.text((SCREEN_WIDTH // 10), (SCREEN_HEIGHT / 18) * 16.5,
                   game_text["quit_label"], LABEL_COLOUR)
        pyxel.text((SCREEN_WIDTH // 10) * 2.5, (SCREEN_HEIGHT / 18) * 16.5,
                   game_text["quit_string"], TEXT_COLOUR)

        # Show what key resets the game
        pyxel.text((SCREEN_WIDTH // 2), (SCREEN_HEIGHT / 18) * 16.5,
                   game_text["restart_label"], LABEL_COLOUR)
        pyxel.text((SCREEN_WIDTH // 7) * 5, (SCREEN_HEIGHT / 18) * 16.5,
                   game_text["restart_string"], TEXT_COLOUR)

    def draw(self):
        """DESCRIPTION OF METHOD"""

        pyxel.cls(BACKGROUND_COLOUR)
        # pyxel.rectb(SCREEN_WIDTH / 12, SCREEN_HEIGHT / 18,
        #             BORDER_WIDTH, BORDER_HEIGHT, BORDER_COLOUR)
        pyxel.rectb(20, 20, 82, 162, 3)
        self.draw_score_and_options()
        self.create_block()


if __name__ == "__main__":
    Tetris()
