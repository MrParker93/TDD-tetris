import pytest 
from board import Board
from movement import Move
from copy import deepcopy
from tetromino import Tetromino


class TestTetrominoMovement:
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

    def test_T_tetromino_can_move_left(self, board, move_T, t_mino):
        board.block.x = move_T.move_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 6, 6, 6, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_can_move_right(self, board, move_T, t_mino):
        board.block.x = move_T.move_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 6, 6, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_can_move_down(self, board, move_T, t_mino):
        board.block.y = move_T.move_down()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 6, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_stops_when_it_hits_the_left_boundary_of_the_board(self, board, move_T, t_mino):
        for _ in range(10):
            board.block.x = move_T.move_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[6, 6, 6, 0, 0, 0, 0, 0, 0, 0],
                              [0, 6, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_stops_when_it_hits_the_right_boundary_of_the_board(self, board, move_T, t_mino):
        for _ in range(10):
            board.block.x = move_T.move_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 6, 6, 6],
                              [0, 0, 0, 0, 0, 0, 0, 0, 6, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_T_tetromino_stops_when_it_hits_the_bottom_of_the_board(self, board, move_T, t_mino):
        for _ in range(10):
            board.block.y = move_T.move_down()
        board.drop_block()
        print(board.block.x, board.block.y)
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 6, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]
        board.falling()
        assert board.board == board.grid
        assert board.is_falling() == False

    def test_T_tetromino_cannot_move_left_through_another_block(self, board, move_T, t_mino):
        for _ in range(10):
            board.block.y = move_T.move_down()
        board.drop_block()
        assert board.is_falling() == True
        board.falling()
        assert board.board == board.grid
        assert board.is_falling() == False

        board.generate_block(5, 1)
        move_T = Move(board.block, board.board)
        for _ in range(2):
            board.block.x = move_T.move_right()
        for _ in range(10):
            board.block.y = move_T.move_down()
        board.block.x = move_T.move_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 6, 6, 0, 0],
                              [0, 0, 0, 6, 6, 6, 6, 0, 0, 0],
                              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]
        
    def test_T_tetromino_cannot_move_right_through_another_block(self, board, move_T, t_mino):
        for _ in range(10):
            board.block.y = move_T.move_down()
        board.drop_block()
        assert board.is_falling() == True
        board.falling()
        assert board.board == board.grid
        assert board.is_falling() == False

        board.generate_block(5, 1)
        move_T = Move(board.block, board.board)
        for _ in range(2):
            board.block.x = move_T.move_left()
        for _ in range(10):
            board.block.y = move_T.move_down()
        board.block.x = move_T.move_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 6, 6, 6, 0, 0, 0, 0, 0, 0],
                              [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]

    def test_T_tetromino_cannot_move_down_through_another_block_and_stops_falling_once_it_stops(self, board, move_T, t_mino):
        for _ in range(10):
            board.block.y = move_T.move_down()
        board.drop_block()
        assert board.is_falling() == True
        board.falling()
        assert board.board == board.grid
        assert board.is_falling() == False

        board.generate_block(5, 1)
        move_T = Move(board.block, board.board)
        for _ in range(10):
            board.block.y = move_T.move_down()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 6, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 6, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]
        board.falling()
        assert board.is_falling() == False

    def test_I_tetromino_can_move_left(self, board, move_I, i_mino):
        board.block.x = move_I.move_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 7, 7, 7, 7, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_I_tetromino_can_move_right(self, board, move_I, i_mino):
        board.block.x = move_I.move_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 7, 7, 7, 7, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_I_tetromino_can_move_down(self, board, move_I, i_mino):
        board.block.y = move_I.move_down()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 7, 7, 7, 7, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_I_tetromino_stops_when_it_hits_the_left_boundary_of_the_board(self, board, move_I, i_mino):
        for _ in range(10):
            board.block.x = move_I.move_left()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[7, 7, 7, 7, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_I_tetromino_stops_when_it_hits_the_right_boundary_of_the_board(self, board, move_I, i_mino):
        for _ in range(10):
            board.block.x = move_I.move_right()
        print(board.block.x, board.block.y)
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 7, 7, 7, 7],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_I_tetromino_stops_when_it_hits_the_bottom_of_the_board(self, board, move_I, i_mino):
        for _ in range(10):
            board.block.y = move_I.move_down()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 7, 7, 7, 7, 0, 0, 0]]
        board.falling()
        assert board.is_falling() == False

    def test_I_tetromino_cannot_move_left_through_another_block(self, board, move_I, move_T, t_mino, i_mino):
        for _ in range(10):
            board.block.y = move_T.move_down()
        board.drop_block()
        assert board.is_falling() == True
        board.falling()
        assert board.board == board.grid
        assert board.is_falling() == False

        board.generate_block(6, 1)
        move_T = Move(board.block, board.board)
        for _ in range(3):
            board.block.x = move_I.move_right()
        for _ in range(4):
            board.block.y = move_I.move_down()
        board.block.x = move_I.move_left()
        print(board.block.x, board.block.y)
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 6, 6, 7, 7, 7, 7],
                              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]
        
    def test_I_tetromino_cannot_move_right_through_another_block(self, board, move_I, move_T, t_mino, i_mino):
        board.block.x = move_T.move_right()
        for _ in range(10):
            board.block.y = move_T.move_down()
        board.drop_block()
        assert board.is_falling() == True
        board.falling()
        assert board.board == board.grid
        assert board.is_falling() == False

        board.generate_block(6, 1)
        move_T = Move(board.block, board.board)
        for _ in range(3):
            board.block.x = move_I.move_left()
        for _ in range(4):
            board.block.y = move_I.move_down()
        board.block.x = move_I.move_right()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [7, 7, 7, 7, 6, 6, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 6, 0, 0, 0, 0]]

    def test_I_tetromino_cannot_move_down_through_another_block_and_stops_falling_once_it_stops(self, board, move_I, i_mino):
        for _ in range(10):
            board.block.y = move_I.move_down()
        board.drop_block()
        assert board.is_falling() == True
        board.falling()
        assert board.board == board.grid
        assert board.is_falling() == False

        board.generate_block(6, 1)
        move_I = Move(board.block, board.board)
        for _ in range(10):
            board.block.y = move_I.move_down()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 7, 7, 7, 7, 0, 0, 0],
                              [0, 0, 0, 7, 7, 7, 7, 0, 0, 0]]
        board.falling()
        assert board.board == board.grid
        assert board.is_falling() == False
    
    def test_T_mino_hard_drops_to_bottom_of_the_board_and_stops_when_it_hits_the_floor(self, board):
        board.generate_block(5, 1)
        move = Move(board.block, board.board)
        board.block.y = move.hard_drop()
        board.drop_block()
        assert board.is_falling() == True
        assert board.grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 6, 6, 0, 0, 0, 0],
                              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]
        board.falling()
        assert board.is_falling() == False
        assert board.board == board.grid
