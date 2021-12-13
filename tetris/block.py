class Block:
    def __init__(self, block):
        self.block = block
        self.x = self.width()
        self.y = 0
        self.width = self.width()
        self.height = self.height()

    def width(self):
        return len(self.block[0])

    def height(self):
        return len(self.block)
