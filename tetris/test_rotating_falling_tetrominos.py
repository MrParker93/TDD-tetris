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
        board.mino = Tetromino(5)
        yield board.mino

    @pytest.fixture
    def i_mino(self, board):
        board.mino = Tetromino(6)
        yield board.mino

    @pytest.fixture
    def move_T(self, board, t_mino):
        move_T = Move(t_mino, board.board, board.current_position)
        yield move_T

    @pytest.fixture
    def move_I(self, board, i_mino):
        move_I = Move(i_mino, board.board, board.current_position)
        yield move_I

    def test_T_mino_rotates_right_correctly_whilst_falling(self, board, t_mino, move_T):
        board.block = t_mino.block
        for _ in range(2):
            board.current_position = move_T.move_left()
            board.current_position = move_T.move_down()
        board.block = move_T.rotate_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 6, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_mino_rotates_left_correctly_whilst_falling(self, board, t_mino, move_T):
        board.block = t_mino.block
        for _ in range(2):
            board.current_position = move_T.move_left()
            board.current_position = move_T.move_down()
        board.block = move_T.rotate_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 6, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_mino_cannot_rotate_if_no_room_to_rotate_whilst_falling(self, board, t_mino, move_T):
        board.block = t_mino.block
        for _ in range(10):
            board.current_position = move_T.move_down()
        board.block = move_T.rotate_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 6, 6, 0, 0, 0]]

    def test_T_mino_cannot_rotate_if_no_room_to_rotate_part2_whilst_falling(self, board, t_mino, move_T):
        board.block = t_mino.block
        board.block = move_T.rotate_right()
        for _ in range(10):
            board.current_position = move_T.move_left()
        # board.block = move_T.rotate_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [6, 6, 0, 0, 0, 0, 0, 0, 0, 0],
                              [6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]