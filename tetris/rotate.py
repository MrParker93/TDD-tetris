class Rotate:
    def __init__(self, block):
        self.block = block

    def rotate_right(self):
        return self.rotate().block

    def rotate_left(self):
        return self.rotate().rotate().rotate().block

    def rotate(self):
        return Rotate(list(map(list, zip(*self.block[::-1]))))