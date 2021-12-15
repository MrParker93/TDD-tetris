class Move:
    def __init__(self, mino, board):
        self.mino = mino
        self.block = self.mino.block
        self.block_width = self.mino.width
        self.block_height = self.mino.height
        self.wallkicks = self.mino.wallkicks
        self.board = board
        self.board_width = len(self.board[0])
        self.board_height = len(self.board)
        self.x = self.mino.x
        self.y = self.mino.y

    def move_left(self):
        # self.x -= 1
        if self.on_grid(self.x - 1, self.y) and not self.block_collision(self.block, x=-1):
            self.x -= 1
        return self.x

    def move_right(self):
        # self.x += 1
        if self.on_grid(self.x + 1 + self.block_width - 1, self.y) and not self.block_collision(self.block, x=1):
            self.x += 1
        return self.x

    def move_down(self):
        # self.y += 1
        if self.on_grid(self.x, self.y + 1 + self.block_height - 1) and not self.block_collision(self.block, y=1):
            self.y += 1
        return self.y

    def rotate_right(self):
        self.block = self.mino.rotate_right()
        if self.can_rotate_right(self.block):
            return self.block
        # self.block = self.mino.rotate_left()
        return self.block
    
    def rotate_left(self):
        self.block = self.mino.rotate_left()

        if self.can_rotate_left(self.block):
            return self.block
        self.block = self.mino.rotate_right()
        return self.block

    def on_grid(self, x, y):
        if len(self.block[0]) == 4:
            return x >= 0 and x < self.board_width and y - 1 < self.board_height
        else:
            return x >= 0 and x < self.board_width and y < self.board_height

    def block_collision(self, block, x=0, y=0):
        for row in range(len(block)):
            for col in range(len(block[0])):
                is_above_board = row + self.y + y < 0
                if is_above_board or block[row][col] == 0:
                    continue
                if not self.on_grid(col + self.x + x, row + self.y + y):
                    return True
                if block[row][col] == 7:
                    if self.board[row + self.y + y - 1][col + self.x + x] != 0:
                        return True
                else:
                    if self.board[row + self.y + y][col + self.x + x] != 0:
                        return True
        return False

    def can_rotate_right(self, block):
        wallkicks = self.wallkicks[:4]
        rotation = self.mino.current_orientation % self.mino.rotations
        each_variation = self.test_each_rotation_position(wallkicks, rotation)
        # variation_possible = False
        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] != 0:
                    for x, y in each_variation:
                        if self.block_collision(block, x, y):
                            print(f"if collision x: {x}, y: {y}")
                            continue
                        elif self.on_grid(col + self.x + x + self.block_width - 1, row + self.y + y + self.block_height - 1):
                            print(f"if no collision x: {x}, y: {y}")
                            print("TRUE")
                            self.x + x
                            self.y + y
                            return True
            # if self.on_grid(col + self.x + x + self.block_width - 1, row + self.y + y + self.block_height - 1) and \
            #     not self.block_collision(block, x, y):
            #     variation_possible = True
            #     print(self.x, self.y)
            # else:
            #     variation_possible = False
            #     print(self.x, self.y)

    def can_rotate_left(self, block):
        wallkicks = self.wallkicks[4:]
        rotation = self.mino.current_orientation % self.mino.rotations
        each_variation = self.test_each_rotation_position(wallkicks, rotation)

        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] != 0:
                    for x, y in each_variation:
                        if self.on_grid(col + self.x + x + self.block_width - 1, row + self.y + y + self.block_height - 1) and \
                            self.board[row + self.y + y][col + self.x + x] == 0:
                            return True
        return False

    def test_each_rotation_position(self, wallkicks, curr_rotation):
        for _ in range(len(wallkicks)):
            return wallkicks[curr_rotation]