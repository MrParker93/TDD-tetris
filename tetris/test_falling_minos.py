from board import Board
from mino import (Mino, MinoO, MinoS, MinoZ,
                    MinoJ, MinoL, MinoT, MinoI)

class TestFallingMinos:
    def test_minos_are_generated_to_the_board(self):
        b = Board(6, 8)
        b.block = MinoT()
        b.start_falling()
        assert b.generate_block_on_board() == [[0, 0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 1, 1, 1, 0 ,0],
                                               [0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0]]