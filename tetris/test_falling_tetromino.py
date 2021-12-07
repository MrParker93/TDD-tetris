import pytest
from board import Board
from tetromino import Tetromino


class TestFallingTetromino:
    @pytest.fixture
    def board(self):
        board = Board(10, 6)
        yield board

    @pytest.fixture
    def t_mino(self, board):
        board.block = Tetromino(5).block
        yield board.block

    def test_T_tetromino_generates_to_the_top_middle_of_the_board(self, board, t_mino):
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_stops_when_it_hits_the_bottom_of_the_board(self, board, t_mino):
        for _ in range(10):
            board.falling()
        board.drop_block()
        print(board.current_position[0], board.current_position[1])
        # assert board.is_falling() == False
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0]]
        assert board.board == board.grid