BOARDWIDTH = 10
BOARDHEIGHT = 20


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
                            