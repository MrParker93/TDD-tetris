class Block:
    def __init__(self, block):
        self.block = block    

    def width(self):
        return len(self.block[0])

    def height(self):
        return len(self.block)

    def grid_position(self, row, col):
        return self.block[row][col]
