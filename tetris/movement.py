class Move:
    def __init__(self, mino, board):
        self.mino = mino
        self.block = self.mino.block
        self.block_width = self.mino.width
        self.block_height = self.mino.height
        self.board = board
        self.board_width = len(self.board[0])
        self.board_height = len(self.board)
        self.x = self.mino.x
        self.y = self.mino.y

    def move_left(self):
        # self.x -= 1
        if self.on_grid(self.x - 1, self.y) and not self.block_collision(x=-1):
            self.x -= 1
        return self.x

    def move_right(self):
        # self.x += 1
        if self.on_grid(self.x + 1 + self.block_width - 1, self.y) and not self.block_collision(x=1):
            self.x += 1
        return self.x

    def move_down(self):
        # self.y += 1
        if self.on_grid(self.x, self.y + 1 + self.block_height - 1) and not self.block_collision(y=1):
            self.y += 1
        return self.y

    def rotate_right(self):
        self.block = self.mino.rotate_right()
        self.block_width = len(self.block[0])
        self.block_height = len(self.block)
        if self.block_collision(self.current_position):
            self.block = self.mino.rotate_left()
        return self.block
    
    def rotate_left(self):
        self.block = self.mino.rotate_left()
        self.block_width = len(self.block[0])
        self.block_height = len(self.block)
        if self.block_collision(self.current_position):
            self.block = self.mino.rotate_right()
        return self.block

    def on_grid(self, x, y):
        if self.block[1][0] == 7:
            return x >= 0 and x < self.board_width and y - 1 < self.board_height
        else:
            return x >= 0 and x < self.board_width and y < self.board_height

    def block_collision(self, x=0, y=0):
        for row in range(len(self.block)):
            for col in range(len(self.block[0])):
                is_above_board = row + self.y + y < 0
                if is_above_board or self.block[row][col] == 0:
                    continue
                if not self.on_grid(col + self.x + x, row + self.y + y):
                    return True
                if self.block[row][col] == 7:
                    if self.board[row + self.y + y - 1][col + self.x + x] != 0:
                        return True
                else:
                    if self.board[row + self.y + y][col + self.x + x] != 0:
                        return True
                # if self.block[row][col] != 0:
                #     try:
                #         if self.board[row + y][col + x] != 0:
                #             return True
                #     except IndexError:
                #         return True
        return False