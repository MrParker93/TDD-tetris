import pytest
from board import Board
from tetromino import Tetromino


class TestFallingTetromino:
    @pytest.fixture
    def board(self):
        board = Board(10, 6)
        yield board

    def test_T_tetromino_generates_to_the_top_middle_of_the_board(self, board):
        board.block = Tetromino(5)
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_stops_when_it_hits_the_bottom_of_the_board(self, board):
        board.block = Tetromino(5)
        for _ in range(4):
            board.falling()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0]]
        board.falling()
        assert board.grid == board.board
        assert board.is_falling() == False

    def test_new_T_tetromino_generates_to_the_top_middle_of_the_board(self, board):
        board.block = Tetromino(5)
        for _ in range(4):
            board.falling()
        board.drop_block()
        assert board.is_falling() == True
        board.falling()
        assert board.grid == board.board
        assert board.is_falling() == False

        board.block = Tetromino(5)
        assert board.is_falling() == True
        board.drop_block()
        assert board.grid == [[0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0]]

    def test_new_T_tetromino_stops_when_it_hits_another_block(self, board):
        board.block = Tetromino(5)
        for _ in range(4):
            board.falling()
        board.drop_block()
        assert board.is_falling() == True
        board.falling()
        assert board.grid == board.board
        assert board.is_falling() == False
        
        board.block = Tetromino(5)
        assert board.is_falling() == True
        for _ in range(2):
            board.falling()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0]]
        board.falling()
        assert board.is_falling() == False

    def test_I_tetromino_generates_to_the_top_middle_of_the_board(self, board):
        board.block = Tetromino(6)
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 7, 7, 7, 7, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]