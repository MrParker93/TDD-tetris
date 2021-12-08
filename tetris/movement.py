class Move:
    def __init__(self, current_position):
        self.current_position = current_position

    def move_left(self):
        self.current_position = (self.current_position[0] - 1, self.current_position[1])
        return self.current_position

    def move_right(self):
        self.current_position = (self.current_position[0] + 1, self.current_position[1])
        return self.current_position

    def move_down(self):
        self.current_position = (self.current_position[0], self.current_position[1] + 1)
        return self.current_position
