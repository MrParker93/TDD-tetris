import pytest
from mino import (Mino, MinoO, MinoS, MinoZ,
                    MinoJ, MinoL, MinoT, MinoI)

class TestMinoRotation:
    def test_all_minos_exist(self):
        """"""
        assert MinoO().shape == [[1, 1, 0],
                                 [1, 1, 0],
                                 [0, 0, 0]]

        assert MinoS().shape == [[0, 1, 1],
                                 [1, 1, 0],
                                 [0, 0, 0]]

        assert MinoZ().shape == [[1, 1, 0],
                                 [0, 1, 1],
                                 [0, 0, 0]]

        assert MinoJ().shape == [[0, 1, 0],
                                 [0, 1, 0],
                                 [1, 1, 0]]

        assert MinoL().shape == [[0, 1, 0],
                                 [0, 1, 0],
                                 [0, 1, 1]]

        assert MinoT().shape == [[0, 1, 0],
                                 [1, 1, 1],
                                 [0, 0, 0]]

        assert MinoI().shape == [[0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0]]

    def test_J_shape_can_be_rotated_three_times(self):
        """"""
        shape = MinoJ()
        assert shape.shape == [[0, 1, 0],
                               [0, 1, 0],
                               [1, 1, 0]]

        assert shape.rotate_right() == [[1, 0, 0],
                                        [1, 1, 1],
                                        [0, 0, 0]]

        assert shape.rotate_right() == [[0, 1, 1],
                                        [0, 1, 0],
                                        [0, 1, 0]]

        assert shape.rotate_right() == [[0, 0, 0],
                                        [1, 1, 1],
                                        [0, 0, 1]]

    def test_L_shape_can_be_rotated_three_times(self):
        """"""
        shape = MinoL()
        assert shape.shape == [[0, 1, 0],
                               [0, 1, 0],
                               [0, 1, 1]]

        assert shape.rotate_right() == [[0, 0, 0],
                                        [1, 1, 1],
                                        [1, 0, 0]]

        assert shape.rotate_right() == [[1, 1, 0],
                                        [0, 1, 0],
                                        [0, 1, 0]]

        assert shape.rotate_right() == [[0, 0, 1],
                                        [1, 1, 1],
                                        [0, 0, 0]]

    def test_T_shape_can_be_rotated_three_times(self):
        """"""
        shape = MinoT()
        assert shape.shape == [[0, 1, 0],
                               [1, 1, 1],
                               [0, 0, 0]]

        assert shape.rotate_right() == [[0, 1, 0],
                                        [0, 1, 1],
                                        [0, 1, 0]]

        assert shape.rotate_right() == [[0, 0, 0],
                                        [1, 1, 1],
                                        [0, 1, 0]]

        assert shape.rotate_right() == [[0, 1, 0],
                                        [1, 1, 0],
                                        [0, 1, 0]]

    def test_rotating_J_shape_four_times_results_in_original_shape(self):
        """"""
        shape = MinoJ()
        four_rotations = shape.rotate_right().rotate_right().rotate_right().rotate_right()
        assert four_rotations == shape
        four_rotations = shape.rotate_left().rotate_left().rotate_left().rotate_left()
        assert four_rotations == shape                                 