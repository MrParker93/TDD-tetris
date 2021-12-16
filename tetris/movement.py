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
        if not self.block_collision(self.block, x=-1):
            self.x -= 1
            return self.x
        return self.x

    def move_right(self):
        if not self.block_collision(self.block, x=1):
            self.x += 1
            return self.x
        return self.x

    def move_down(self):
        if not self.block_collision(self.block, y=1):
            self.y += 1
            return self.y
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
        collision = False
        for row in range(len(block)):
            for col in range(len(block[0])):
                is_above_board = row + self.y + y < 0
                if is_above_board:
                    continue
                if block[row][col] != 0:
                    if col + self.x + x < 0 or col + self.x + x >= self.board_width:
                        collision = True

                    if row + self.y + y >= self.board_height:
                        collision = True
                    try:
                        if self.board[row + self.y + y][col + self.x + x] != 0:
                            collision = True
                    except IndexError:
                        collision = True
        if collision:
            return True
        return False

    def can_rotate_right(self, block):
        wallkicks = self.wallkicks[4:]
        rotation = self.mino.current_orientation % self.mino.rotations
        each_variation = self.get_each_rotation_position(wallkicks, rotation)
        if self.mino.y < 0:
            new_y = self.mino.y + 1
        else:
            new_y = self.mino.y
            
        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] != 0:
                    for x, y in each_variation:
                        if col + self.x + x < 0 or col + self.x + x >= self.board_width \
                             or row + new_y + y >= self.board_height:
                            print("-------------------------------------EACH EDGE-------------------------------------")
                            print(f"Invalid position ({x}, {y}), out of bounds. Either {col + self.x + x} < 0 or {col + self.x + x} >= {self.board_width} or {row + new_y + y} >= {self.board_height}")
                            print()
                            continue
                        if self.block_collision(block, x, y):
                            print(f"Invalid position ({x}, {y}), block collision detected at ({col + self.x + x}, {row + new_y + y}), ({col + self.x + x}, {row + new_y + y + 1}), ({col + self.x + x + 1}, {row + new_y + y + 1}), ({col + self.x + x}, {row + new_y + y + 2})")
                            print()
                            continue
                        if 0 <= col + self.x + x < self.board_width and row + new_y + y < self.board_height:
                            print(f"Valid position ({x}, {y}), block can rotate right. 0 <= {col + self.x + x} < {self.board_width} and {row + new_y + y} < {self.board_height}")
                            self.mino.x += x
                            self.mino.y = new_y + y
                            return True

        print("Block cannot rotate right.")
        return False

    def can_rotate_left(self, block):
        wallkicks = self.wallkicks[:4]
        rotation = self.mino.current_orientation % self.mino.rotations
        each_variation = self.get_each_rotation_position(wallkicks, rotation)
        if self.mino.y < 0:
            new_y = self.mino.y + 1
        else:
            new_y = self.mino.y
            
        for row in range(len(block)):
            for col in range(len(block[0])):
                if block[row][col] != 0:
                    for x, y in each_variation:
                        if col + self.x + x < 0 or col + self.x + x >= self.board_width \
                             or row + new_y + y >= self.board_height:
                            print("-------------------------------------EACH EDGE-------------------------------------")
                            print(f"Invalid position ({x}, {y}), out of bounds. Either {col + self.x + x} < 0 or {col + self.x + x} >= {self.board_width} or {row + new_y + y} >= {self.board_height}")
                            print()
                            continue
                        if self.block_collision(block, x, y):
                            print(f"Invalid position ({x}, {y}), block collision detected at ({col + self.x + x}, {row + new_y + y}), ({col + self.x + x}, {row + new_y + y + 1}), ({col + self.x + x + 1}, {row + new_y + y + 1}), ({col + self.x + x}, {row + new_y + y + 2})")
                            print()
                            continue
                        if 0 <= col + self.x + x < self.board_width and row + new_y + y < self.board_height:
                            print(f"Valid position ({x}, {y}), block can rotate right. 0 <= {col + self.x + x} < {self.board_width} and {row + new_y + y} < {self.board_height}")
                            self.mino.x += x
                            self.mino.y = new_y + y
                            return True

        print("Block cannot rotate right.")
        return False

    def get_each_rotation_position(self, wallkicks, curr_rotation):
        for _ in range(len(wallkicks)):
            return wallkicks[curr_rotation]