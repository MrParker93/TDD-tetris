import pytest 
from rotate import Rotate
from tetromino import Tetromino


class TestTetrominoRotation:
    @pytest.fixture
    def t_mino(self):
        mino = Tetromino(5)
        yield mino

    @pytest.fixture
    def o_mino(self):
        mino = Tetromino(0)
        yield mino

    @pytest.fixture
    def i_mino(self):
        mino = Tetromino(6)
        yield mino

    def test_initial_orientation_of_T_tetromino(self, t_mino):
        assert t_mino.block == [[0, 6, 0],
                                [6, 6, 6],
                                [0, 0, 0]]
    
    def test_T_tetromino_can_be_rotated_right(self, t_mino):
        assert t_mino.rotate_right() == [[0, 6, 0],
                                         [0, 6, 6],
                                         [0, 6, 0]]
    
    def test_T_tetromino_can_be_rotated_left(self, t_mino):
        assert t_mino.rotate_left() == [[0, 6, 0],
                                        [6, 6, 0],
                                        [0, 6, 0]]
                                
    def test_T_tetromino_has_four_orientations(self, t_mino):
        assert len(t_mino.orientations) == 4

    def test_initial_orientation_of_O_tetromino(self, o_mino):
        assert o_mino.block == [[1, 1],
                                [1, 1]]
    
    def test_O_tetromino_can_be_rotated_right(self, o_mino):
        assert o_mino.rotate_right() == [[1, 1],
                                         [1, 1]]
    
    def test_O_tetromino_can_be_rotated_left(self, o_mino):
        assert o_mino.rotate_left() == [[1, 1],
                                        [1, 1]]
                                
    def test_O_tetromino_has_one_orientations(self, o_mino):
        assert len(o_mino.orientations) == 1

    def test_initial_orientation_of_I_tetromino(self, i_mino):
        assert i_mino.block == [[0, 0, 0, 0],
                                [7, 7, 7, 7],
                                [0, 0, 0, 0]]
    
    def test_I_tetromino_can_be_rotated_right(self, i_mino):
        assert i_mino.rotate_right() == [[0, 7, 0],
                                         [0, 7, 0],
                                         [0, 7, 0],
                                         [0, 7, 0]]
    
    def test_I_tetromino_can_be_rotated_left(self, i_mino):
        assert i_mino.rotate_left() == [[0, 7, 0],
                                        [0, 7, 0],
                                        [0, 7, 0],
                                        [0, 7, 0]]
                                
    def test_I_tetromino_has_one_orientations(self, i_mino):
        assert len(i_mino.orientations) == 2