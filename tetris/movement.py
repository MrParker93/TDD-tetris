class Move:
    def __init__(self, mino, board):
        self.mino = mino
        self.block = self.mino.block
        self.wallkicks = self.mino.wallkicks
        self.board = board
        self.board_width = len(self.board[0])
        self.board_height = len(self.board)
        self.x = self.mino.x
        self.y = self.mino.y

    def move_left(self):
        print(f"x before: {self.x}")
        self.x -= 1
        print(f"x after: {self.x}")
        if not self.block_collision(self.block, x=-1):
            return self.x
        self.x += 1
        return self.x

    def move_right(self):
        print(f"x before: {self.x}")
        self.x += 1
        print(f"x after: {self.x}")
        if not self.block_collision(self.block, x=1):
            return self.x
        self.x -= 1
        return self.x

    def move_down(self):
        print(f"y before: {self.y}")
        self.y += 1
        print(f"y after: {self.y}")
        if not self.block_collision(self.block, y=1):
            return self.y
        self.y -= 1
        return self.y

    def hard_drop(self):
        for row in reversed(range(self.board_height)):
            print(f"y: {self.y}")
            drop = row - self.y if self.y >=0 else row + self.y
            self.y += drop
            if not self.block_collision(self.block, y=drop):
                return self.y
        self.y -= drop
        return self.y

    def rotate_right(self):
        self.block = self.mino.rotate_right()
        if self.can_rotate_right(self.block):
            return self.block
        self.block = self.mino.rotate_left()
        return self.block
    
    def rotate_left(self):
        self.block = self.mino.rotate_left()
        if self.can_rotate_left(self.block):
            return self.block 
        self.block = self.mino.rotate_right()
        return self.block

    def block_collision(self, block, x=0, y=0):
        for row in range(len(block)):
            for col in range(len(block[0])):
                is_above_board = row + self.y< 0
                if is_above_board:
                    continue
                if block[row][col] != 0:
                    if col + self.x < 0 or col + self.x > self.board_width - 1:
                        print(f"col {col} + x {self.x}: {self.x + col}")
                        return True

                    if row + self.y > self.board_height - 1:
                        return True

                    if self.board[row + self.y][col + self.x] != 0:
                        return True
        return False

    def can_rotate_right(self, block):
        wallkicks = self.wallkicks[4:]
        rotation = self.mino.current_orientation % self.mino.rotations
        each_variation = self.get_each_rotation_position(wallkicks, rotation)
        # if self.y < 0:
        #     new_y = self.y + 1
        # else:
        #     new_y = self.y
            
        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] != 0:
                    for x, y in each_variation:
                        if col + self.x + x < 0 or col + self.x + x >= self.board_width \
                             or row + self.y + y >= self.board_height:
                            continue

                        if self.block_collision(block, x, y):
                            continue

                        if 0 <= col + self.x + x < self.board_width and row + self.y + y < self.board_height:
                            self.x += x
                            self.y += y
                            return True
        return False

    def can_rotate_left(self, block):
        wallkicks = self.wallkicks[:4]
        rotation = self.mino.current_orientation % self.mino.rotations
        each_variation = self.get_each_rotation_position(wallkicks, rotation)
        # if self.mino.y < 0:
        #     new_y = self.mino.y + 1
        # else:
        #     new_y = self.mino.y
            
        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] != 0:
                    for x, y in each_variation:
                        if col + self.x + x < 0 or col + self.x + x >= self.board_width \
                             or row + self.y + y >= self.board_height:
                            continue

                        if self.block_collision(block, x, y):
                            continue

                        if 0 <= col + self.x + x < self.board_width and row + self.y + y < self.board_height:
                            self.x += x
                            self.y += y
                            return True
        return False

    def get_each_rotation_position(self, wallkicks, curr_rotation):
        for _ in range(len(wallkicks)):
            return wallkicks[curr_rotation]