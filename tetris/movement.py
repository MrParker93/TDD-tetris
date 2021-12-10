class Move:
    def __init__(self, block, board, current_position):
        self.block = block
        self.block_width = len(self.block[0])
        self.block_height = len(self.block)
        self.board = board
        self.board_width = len(self.board[0])
        self.board_height = len(self.board)
        self.current_position = current_position

    def move_left(self):
        self.current_position = (self.current_position[0] - 1, self.current_position[1])
        if self.current_position[0] - int(self.block_width / 2) < 0 or self.block_collision(self.current_position):
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
        return self.current_position

    def move_right(self):
        self.current_position = (self.current_position[0] + 1, self.current_position[1])
        if self.current_position[0] > self.board_width - 1 or \
            self.block_collision(self.current_position):
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
        return self.current_position

    def move_down(self):
        self.current_position = (self.current_position[0], self.current_position[1] + 1)
        if self.current_position[1] + int(self.block_height / 2) >= self.board_height or \
            self.block_collision(self.current_position):
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
        return self.current_position

    def block_collision(self, check_position):
        for row in range(self.block_height):
            for col in range(self.block_width):
                if self.block[row][col] != 0:
                    try:
                        if self.board[row + check_position[1]][col + check_position[0] - int(self.block_width / 2)] != 0:
                            return True
                    except IndexError:
                        return True
        return False