import pyxel
from text import Text
from board import Board
from gamelogic import GameLogic
from tetrimino import TetriminoGenerator, Tetrimino

class App:
    WIDTH = 140
    HEIGHT = 200

    def __init__(self):
        pyxel.init(App.WIDTH, App.HEIGHT, caption="Tetris!", fps=60)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.l = GameLogic()  # Initialise GameLogic class to update level, fall speed, score, lines and combos
        self.t = TetriminoGenerator()  # Initialise Block Generator class to create new blocks
        self.tetrimino = Tetrimino()  # Initialise Tetrimino class for access to block functions
        self.text = Text(self.l.level, self.l.score, self.l.lines, self.l.combos)  # Initialise Text class to display all text
        self.game_state = "running"  # Set the game to run
        self.is_gameover = False  # Set the gameover variable to false to run the game
        self.get_block = self.t.generate()  # Generate a new block
        self.get_next_block = self.t.next_block.pop(0)  # Generate the next block
        self.current_block = self.get_block.block  # Get the current block
        self.pos_x = self.get_block.x  # The current x position of the current block
        self.pos_y = self.get_block.y  # The current y position of the current block
        self.width = self.tetrimino.block_size(self.current_block)[1]  # Gets the width of the current block
        self.height = self.tetrimino.block_size(self.current_block)[0]  # Gets the height of the current block
        self.rotation = self.get_block.rotation
        self.b = Board(self.current_block, self.pos_x, self.pos_y)  # Initialise Board class that includes, blocks, board and collision checks
        print(f"{self.current_block}, x: {self.pos_x}, y: {self.pos_y}, width: {self.width}, height: {self.height}")

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        
        if self.game_state == "running" or self.game_state == "stopped":
            if pyxel.btn(pyxel.KEY_R):
                self.reset()
        
        if pyxel.btn(pyxel.KEY_P):
            if self.game_state == "running" and not self.is_gameover:
                self.game_state = "paused"
            else:
                self.game_state = "running"

        if self.game_state == "running":
            if pyxel.frame_count % self.l.fall_speed == 2:
                pass
                # if self.any_collisions(self.pos_x, self.pos_y, self.width, self.height):
                #     self.falling_block()
            
            if pyxel.btnp(pyxel.KEY_LEFT, 10, 2) and not pyxel.btn(pyxel.KEY_RIGHT):
                new_x = self.get_block.move_block_left()
                if not self.b.any_collisions(new_x, self.pos_y, self.width, self.height):
                    self.pos_x = new_x

            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 2) and not pyxel.btn(pyxel.KEY_LEFT):
                new_x = self.get_block.move_block_right()
                if not self.b.any_collisions(new_x, self.pos_y, self.width, self.height):
                    self.pos_x = new_x

            if pyxel.btnp(pyxel.KEY_DOWN, 10, 2):
                new_y = self.get_block.move_block_down()
                if not self.b.any_collisions(self.pos_x, new_y, self.width, self.height):
                    self.pos_y = new_y

            if pyxel.btn(pyxel.KEY_SPACE):
                if not self.any_collisions():
                    self.position = self.get_block.place_block()

            if pyxel.btnp(pyxel.KEY_X, 10, 2) and not pyxel.btn(pyxel.KEY_Z):
                self.rotation = 1
                new_block = self.tetrimino.rotate_block(self.current_block)
                if not self.any_collisions(self.pos_x, self.pos_y, new_block):
                    self.current_block = new_block

            if pyxel.btnp(pyxel.KEY_Z, 10, 2) and not pyxel.btn(pyxel.KEY_X):
                self.rotation = -1
                new_block = self.tetrimino.rotate_block(self.current_block)
                if not self.any_collisions(self.pos_x, self.pos_y, new_block):
                    self.current_block = new_block

    def draw(self):
        pyxel.cls(0)
        self.text.show()
        self.b.draw_board()
        self.draw_borders()
        self.b.draw_block()
        self.draw_next_block()

        if self.game_state == "paused":
            pyxel.text(App.WIDTH // 2 - 20, App.HEIGHT // 2 - 12, "PAUSED", pyxel.frame_count % 16)

    def draw_borders(self):
        
        # Create border for board
        pyxel.rectb(4, 8, self.b.WIDTH * 8, self.b.HEIGHT * 8, 5)
        
        # Create border for showing the next block
        pyxel.rectb(App.WIDTH * 0.66, 16, 37, 48, 5)

    def draw_next_block(self):

        for row in range(len(self.get_next_block.block)):
            for col in range(len(self.get_next_block.block[row])):
                colour = self.get_next_block.block[row][col]
                if colour == 6:
                    pyxel.rect((col * 8) + 140 * 0.77,
                               24 + (row * 8), 8, 8, colour)
                elif colour == 5:
                    pyxel.rect((col * 8) + 140 * 0.74,
                               40 + (row * 8), 8, 8, colour)
                elif colour == 1 or colour == 2 or colour == 9:
                    pyxel.rect((col * 8) + 140 * 0.75,
                               32 + (row * 8), 8, 8, colour)
                else:
                    pyxel.rect((col * 8) + 140 * 0.74,
                               32 + (row * 8), 8, 8, colour)
if __name__ == "__main__":
    a = App()
    