import pytest 
from piece import Piece

p = Piece()
class TestRotatingPieces:
    def test__piece_exists_on_3_by_3_board(self):
        """"""
        assert p.piece == [[0, 2, 0],
                           [0, 2, 0],
                           [0, 0, 0]]