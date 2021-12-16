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
    def bigger_board(self):
        board = Board(10, 8)
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
                              [0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
                              [0, 6, 6, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_mino_rotates_left_correctly_whilst_falling(self, board, t_mino, move_T):
        for _ in range(2):
            board.block.x = move_T.move_left()
            board.block.y = move_T.move_down()
        board.block.block = move_T.rotate_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 6, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_mino_performs_wallkick_on_top_boundary_of_board_if_rotation_moves_block_out_of_bounds(self, board, t_mino, move_T):
        board.block.block = move_T.rotate_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 6, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_mino_performs_wallkick_on_right_boundary_if_rotation_moves_block_out_of_bounds_whilst_falling(self, board, t_mino, move_T):
        board.block.block = move_T.rotate_right()
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
        board.block.block = move_T.rotate_left()
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

    def test_T_mino_performs_wallkick_into_valid_position_when_blocks_on_board_occupy_other_valid_positions(self, board):
        board.generate_block(4)
        move = Move(board.block, board.board)
        for _ in range(10):
            board.block.y = move.move_down()
        board.block.x = move.move_right()
        board.block.block = move.rotate_left()
        board.drop_block()
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 5, 5, 0, 0, 0]]
        board.falling()
        assert board.is_falling() == False
        
        board.generate_block(3)
        move = Move(board.block, board.board)
        board.block.block = move.rotate_right()
        for _ in range(10):
            board.block.x = move.move_right()
        for _ in range(10):
            board.block.y = move.move_down()
        board.drop_block()
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 5, 0, 0, 0, 4],
                              [0, 0, 0, 0, 0, 5, 0, 0, 0, 4],
                              [0, 0, 0, 0, 0, 5, 5, 0, 4, 4]]
                              
        board.falling()
        assert board.is_falling() == False
        
        board.generate_block(3)
        move = Move(board.block, board.board)
        for _ in range(1):
            board.block.x = move.move_right()
        for _ in range(2):
            board.block.y = move.move_down()
        board.drop_block()
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 4, 4, 4, 0, 0, 0],
                              [0, 0, 0, 0, 0, 5, 4, 0, 0, 4],
                              [0, 0, 0, 0, 0, 5, 0, 0, 0, 4],
                              [0, 0, 0, 0, 0, 5, 5, 0, 4, 4]]
        board.falling()
        assert board.is_falling() == False

        board.generate_block(5)
        move = Move(board.block, board.board)
        for _ in range(3):
            board.block.x = move.move_right()
        board.block.block = move.rotate_right()
        for _ in range(1):
            board.block.x = move.move_right()
        for _ in range(3):
            board.block.y = move.move_down()
        board.block.block = move.rotate_left()
        board.drop_block()
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 4, 4, 4, 0, 0, 0],
                              [0, 0, 0, 0, 0, 5, 4, 0, 0, 4],
                              [0, 0, 0, 0, 0, 5, 6, 6, 6, 4],
                              [0, 0, 0, 0, 0, 5, 5, 6, 4, 4]]
        board.falling()
        assert board.is_falling() == False
