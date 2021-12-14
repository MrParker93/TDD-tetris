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

        self.block = self.mino.rotate_left()
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
        if self.mino.rotations == 4:
            for row in range(len(block)):
                for col in range(len(block[0])):
                    if block[row][col] != 0:

                        if self.mino.current_orientation % self.mino.rotations == 0:

                            # Wall Kick Test 1 (x:0, y:0)
                            if self.board[row + self.y][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y):  # and not self.block_collision(block):

                                return True
                                
                            # Wall Kick Test 2 (x:-1, y:0)
                            elif self.board[row + self.y][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1, row + self.y):  # and not self.block_collision(block, x=-1):

                                print("dont get here1")
                                self.x -= 1
                                return True
                                
                            # Wall Kick Test 3 (x:-1, y:1)
                            elif self.board[row + self.y + 1][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1, row + self.y + 1 + self.block_height - 1):  # and not self.block_collision(block, x=-1, y=1):

                                print("dont get here2")
                                self.y += 1
                                self.x -= 1
                                return True
                                
                            # Wall Kick Test 4 (x:0, y:-2)
                            elif self.board[row + self.y - 2][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y - 2):  # and not self.block_collision(block, y=-2):

                                print("dont get here3")
                                self.y -= 2
                                return True
                                
                            # Wall Kick Test 4 (x:-1, y:-2)
                            elif self.board[row + self.y - 2][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1, row + self.y - 2):  # and not self.block_collision(block, x=-1, y=-2):

                                print("dont get here4")
                                self.y -= 2
                                self.x -= 1
                                return True

                            print("dont get here5")
                            return False
                            
                        elif self.mino.current_orientation % self.mino.rotations == 1:

                            # Wall Kick Test 1 (x:0, y:0)
                            if self.board[row + self.y][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y):  # and not self.block_collision(block):

                                return True

                            # Wall Kick Test 2 (x:-1, y:0)
                            elif self.board[row + self.y][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1, row + self.y):  # and not self.block_collision(block, x=-1):

                                print("dont get here1 mod 1")
                                self.x -= 1
                                return True

                            # Wall Kick Test 3 (x:-1, y:-1)
                            elif self.board[row + self.y - 1][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1, row + self.y - 1):  # and not self.block_collision(block, x=-1, y=-1):

                                print(f"w: {self.block_width}, h: {self.block_height}")
                                self.y -= 1
                                self.x -= 1
                                return True

                            # Wall Kick Test 4 (x:0, y:2)
                            elif self.board[row + self.y + 2][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y + 2 + self.block_height - 1):  # and not self.block_collision(block, y=2):

                                print("dont get here3 mod 1")
                                self.y += 2
                                return True

                            # Wall Kick Test 5 (x:-1, y:2)
                            elif self.board[row + self.y + 2][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1, row + self.y + 2 + self.block_height - 1):  # and not self.block_collision(block, x=-1, y=2):

                                print("dont get here4 mod 1")
                                self.y += 2
                                self.x -= 1
                                return True

                            print("dont get here5 mod 1")
                            return False

                        elif self.mino.current_orientation % self.mino.rotations == 2:

                            # Wall Kick Test 1 (x:0, y:0)
                            if self.board[row + self.y][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y):  # and not self.block_collision(block):

                                return True

                            # Wall Kick Test 2 (x:1, y:0)
                            elif self.board[row + self.y][col + self.x + 1] == 0 and \
                                self.on_grid(col + self.x + 1 + self.block_width - 1, row + self.y):  # and not self.block_collision(block, x=1):

                                print("dont get here1 mod 2")
                                self.x += 1
                                return True

                            # Wall Kick Test 3 (x:1, y:1)
                            elif self.board[row + self.y + 1][col + self.x + 1] == 0 and \
                                self.on_grid(col + self.x + 1 + self.block_width - 1, row + self.y + 1 + self.block_height - 1):  # and not self.block_collision(block, x=1, y=1):

                                print("dont get here2 mod 2")
                                self.y += 1
                                self.x += 1
                                return True

                            # Wall Kick Test 4 (x:0, y:-2)
                            elif self.board[row + self.y - 2][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y - 2):  # and not self.block_collision(block, y=-2):

                                print("dont get here3 mod 2")
                                self.y -= 2
                                return True

                            # Wall Kick Test 5 (x:1, y:-2)
                            elif self.board[row + self.y - 2][col + self.x + 1] == 0 and \
                                self.on_grid(col + self.x + 1 + self.block_width - 1, row + self.y - 2):  # and not self.block_collision(block, x=1, y=-2):

                                print("dont get here4 mod 2")
                                self.y -= 2
                                self.x += 1
                                return True

                            print("dont get here5 mod 2")
                            return False

                        elif self.mino.current_orientation % self.mino.rotations == 3:

                            # Wall Kick Test 1 (x:0, y:0)
                            if self.board[row + self.y][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y):  # and not self.block_collision(block):

                                return True

                            # Wall Kick Test 2 (x:1, y:0)
                            elif self.board[row + self.y][col + self.x + 1] == 0 and \
                                self.on_grid(col + self.x + 1 + self.block_width - 1, row + self.y):  # and not self.block_collision(block, x=1):

                                print("dont get here1 mod 3")
                                self.x += 1
                                return True

                            # Wall Kick Test 3 (x:1, y:-1)
                            elif self.board[row + self.y - 1][col + self.x + 1] == 0 and \
                                self.on_grid(col + self.x + 1 + self.block_width - 1, row + self.y - 1):  # and not self.block_collision(block, x=1, y=-1):

                                print("dont get here2 mod 3")
                                self.y -= 1
                                self.x += 1
                                return True

                            # Wall Kick Test 4 (x:0, y:2)
                            elif self.board[row + self.y + 2][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y + 2 + self.block_height - 1):  # and not self.block_collision(block, y=2):

                                print("dont get here3 mod 3")
                                self.y += 2
                                return True

                            # Wall Kick Test 5 (x:1, y:2)
                            elif self.board[row + self.y + 2][col + self.x + 1] == 0 and \
                                self.on_grid(col + self.x + 1 + self.block_width - 1, row + self.y + 2 + self.block_height - 1):  # and not self.block_collision(block, x=1, y=2):

                                print("dont get here4 mod 3")
                                self.y += 2
                                self.x += 1
                                return True

                            print("dont get here5 mod 3")
                            return False

    def can_rotate_left(self, block):
        if self.mino.rotations == 4:
            for row in range(len(block)):
                for col in range(len(block[0])):
                    if block[row][col] != 0:

                        if self.mino.current_orientation % self.mino.rotations == 0:

                            # Wall Kick Test 1 (x:0, y:0)
                            if self.board[row + self.y][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y):  # and not self.block_collision(block):

                                return True

                            # Wall Kick Test 2 (x:-1, y:0)
                            elif self.board[row + self.y][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1 + self.block_width - 1, row + self.y):  # and not self.block_collision(block, x=1):

                                print("dont get here1 mod 2")
                                self.x -= 1
                                return True

                            # Wall Kick Test 3 (x:-1, y:1)
                            elif self.board[row + self.y + 1][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1 + self.block_width - 1, row + self.y + 1 + self.block_height - 1):  # and not self.block_collision(block, x=1, y=1):

                                print("dont get here2 mod 2")
                                self.y += 1
                                self.x -= 1
                                return True

                            # Wall Kick Test 4 (x:0, y:-2)
                            elif self.board[row + self.y - 2][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y - 2):  # and not self.block_collision(block, y=-2):

                                print("dont get here3 mod 2")
                                self.y -= 2
                                return True

                            # Wall Kick Test 5 (x:-1, y:-2)
                            elif self.board[row + self.y - 2][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1 + self.block_width - 1, row + self.y - 2):  # and not self.block_collision(block, x=1, y=-2):

                                print("dont get here4 mod 2")
                                self.y -= 2
                                self.x -= 1
                                return True

                            print("dont get here5 mod 2")
                            return False

                        elif self.mino.current_orientation % self.mino.rotations == 1:
                            
                            # Wall Kick Test 1 (x:0, y:0)
                            if self.board[row + self.y][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y):  # and not self.block_collision(block):

                                return True
                                
                            # Wall Kick Test 2 (x:-1, y:0)
                            elif self.board[row + self.y][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1 + self.block_width - 1, row + self.y):  # and not self.block_collision(block, x=1):

                                print("dont get here1")
                                self.x -= 1
                                return True
                                
                            # Wall Kick Test 3 (x:-1, y:-1)
                            elif self.board[row + self.y - 1][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1 + self.block_width - 1, row + self.y - 1):  # and not self.block_collision(block, x=1, y=-1):

                                print("dont get here2")
                                self.y -= 1
                                self.x -= 1
                                return True
                                
                            # Wall Kick Test 4 (x:0, y:2)
                            elif self.board[row + self.y + 2][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y + 2 + self.block_height - 1):  # and not self.block_collision(block, y=2):

                                print("dont get here3")
                                self.y += 2
                                return True
                                
                            # Wall Kick Test 5 (x:-1, y:2)
                            elif self.board[row + self.y + 2][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1 + self.block_width - 1, row + self.y + 2 + self.block_height - 1):  # and not self.block_collision(block, x=1, y=2):
                                
                                print("dont get here4")
                                self.y += 2
                                self.x -= 1
                                return True

                            print("dont get here5")
                            return False
                        
                        elif self.mino.current_orientation % self.mino.rotations == 2:

                            # Wall Kick Test 1 (x:0, y:0)
                            if self.board[row + self.y][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y):  # and not self.block_collision(block):

                                return True

                            # Wall Kick Test 2 (x:-1, y:0)
                            elif self.board[row + self.y][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1, row + self.y):  # and not self.block_collision(block, x=-1):

                                print("dont get here1")
                                self.x -= 1
                                return True

                            # Wall Kick Test 3 (x:-1, y:1)
                            elif self.board[row + self.y + 1][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1, row + self.y + 1 + self.block_height - 1):  # and not self.block_collision(block, x=-1, y=1):

                                print("dont get here2")
                                self.y += 1
                                self.x -= 1
                                return True

                            # Wall Kick Test 4 (x:0, y:-2)
                            elif self.board[row + self.y - 2][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y - 2):  # and not self.block_collision(block, y=-2):

                                print("dont get here3")
                                self.y -= 2
                                return True
                                
                            # Wall Kick Test 4 (x:-1, y:-2)
                            elif self.board[row + self.y - 2][col + self.x - 1] == 0 and \
                                self.on_grid(col + self.x - 1, row + self.y - 2):  # and not self.block_collision(block, x=-1, y=-2):

                                print("dont get here4")
                                self.y -= 2
                                self.x -= 1
                                return True

                            print("dont get here5")
                            return False
                           
                        elif self.mino.current_orientation % self.mino.rotations == 3:

                            # Wall Kick Test 1 (x:0, y:0)
                            if self.board[row + self.y][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y):  # and not self.block_collision(block):

                                return True

                            # Wall Kick Test 2 (x:1, y:0)
                            elif self.board[row + self.y][col + self.x + 1] == 0 and \
                                self.on_grid(col + self.x + 1, row + self.y):  # and not self.block_collision(block, x=-1):

                                print("dont get here1 mod 1")
                                self.x += 1
                                return True

                            # Wall Kick Test 3 (x:1, y:-1)
                            elif self.board[row + self.y - 1][col + self.x + 1] == 0 and \
                                self.on_grid(col + self.x + 1, row + self.y - 1):  # and not self.block_collision(block, x=-1, y=-1):

                                print("dont get here2 mod 1")
                                self.y -= 1
                                self.x += 1
                                return True

                            # Wall Kick Test 4 (x:0, y:2)
                            elif self.board[row + self.y + 2][col + self.x] == 0 and \
                                self.on_grid(col + self.x, row + self.y + 2 + self.block_height - 1):  # and not self.block_collision(block, y=2):

                                print("dont get here3 mod 1")
                                self.y += 2
                                return True

                            # Wall Kick Test 5 (x:1, y:2)
                            elif self.board[row + self.y + 2][col + self.x + 1] == 0 and \
                                self.on_grid(col + self.x + 1, row + self.y + 2 + self.block_height - 1):  # and not self.block_collision(block, x=-1, y=2):

                                print("dont get here4 mod 1")
                                self.y += 2
                                self.x += 1
                                return True

                            print("dont get here5 mod 1")
                            return False