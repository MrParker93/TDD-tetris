import pytest
from board import Board
from movement import Move
from tetromino import Tetromino


class TestRotatingFallingTetrominos:
    @pytest.fixture
    def board(self):
        board = Board(10, 6)
        yield board

    @pytest.fixture
    def t_mino(self, board):
        board.block = Tetromino(5).block
        yield board.block

    @pytest.fixture
    def move(self, board, t_mino):
        move = Move(t_mino, board.board, board.current_position)
        yield move

    