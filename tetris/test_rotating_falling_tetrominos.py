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
        board.block = Tetromino(5)
        yield board.block

    @pytest.fixture
    def i_mino(self, board):
        board.block = Tetromino(6)
        yield board.block

    @pytest.fixture
    def move_T(self, board, t_mino):
        move_T = Move(t_mino, board.board)
        yield move_T

    @pytest.fixture
    def move_I(self, board, i_mino):
        move_I = Move(i_mino, board.board)
        yield move_I

    def test_T_mino_rotates_right_correctly_whilst_falling(self, board, t_mino, move_T):
        for _ in range(2):
            board.block.x = move_T.move_left()
            board.block.y = move_T.move_down()
        board.block.block = move_T.rotate_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 6, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_mino_rotates_left_correctly_whilst_falling(self, board, t_mino, move_T):
        for _ in range(2):
            board.block.x = move_T.move_left()
            board.block.y = move_T.move_down()
        board.block.block = move_T.rotate_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 6, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_mino_cannot_rotate_if_no_room_to_rotate_whilst_falling(self, board, t_mino, move_T):
        for _ in range(10):
            board.block.y = move_T.move_down()
        board.block.block = move_T.rotate_right()
        # print(f"x: {board.block.x}, y: {board.block.y}")
        # print(f"w: {board.block.width}, h: {board.block.height}")
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0]]

    def test_T_mino_performs_wallkick_on_right_boundary_if_rotation_moves_block_out_of_bounds_whilst_falling(self, board, t_mino, move_T):
        board.block.block = move_T.rotate_left()
        for _ in range(10):
            board.block.x = move_T.move_right()
        board.block.block = move_T.rotate_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 6, 0],
                              [0, 0, 0, 0, 0, 0, 0, 6, 6, 6],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_mino_performs_wallkick_on_left_boundary_if_rotation_moves_block_out_of_bounds_whilst_fallings(self, board, t_mino, move_T):
        board.block.block = move_T.rotate_right()
        for _ in range(10):
            board.block.x = move_T.move_left()
        board.block.block = move_T.rotate_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 6, 0, 0, 0, 0, 0, 0, 0, 0],
                              [6, 6, 6, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]