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
        block = shape.shape
        rotated = shape.rotate_right()
        rotated_twice = shape.rotate_right()
        rotated_thrice = shape.rotate_right()
        assert block == [[0, 1, 0],
                         [0, 1, 0],
                         [1, 1, 0]]

        assert rotated == [[1, 0, 0],
                           [1, 1, 1],
                           [0, 0, 0]]

        assert rotated_twice == [[0, 1, 1],
                                 [0, 1, 0],
                                 [0, 1, 0]]

        assert rotated_thrice == [[0, 0, 0],
                                  [1, 1, 1],
                                  [0, 0, 1]]

    def test_L_shape_can_be_rotated_three_times(self):
        """"""
        shape = MinoL()
        block = shape.shape
        rotated = shape.rotate_right()
        rotated_twice = shape.rotate_right()
        rotated_thrice = shape.rotate_right()
        assert block == [[0, 1, 0],
                         [0, 1, 0],
                         [0, 1, 1]]

        assert rotated == [[0, 0, 0],
                           [1, 1, 1],
                           [1, 0, 0]]

        assert rotated_twice == [[1, 1, 0],
                                 [0, 1, 0],
                                 [0, 1, 0]]

        assert rotated_thrice == [[0, 0, 1],
                                  [1, 1, 1],
                                  [0, 0, 0]]

    def test_T_shape_can_be_rotated_three_times(self):
        """"""
        shape = MinoT()
        block = shape.shape
        rotated = shape.rotate_right()
        rotated_twice = shape.rotate_right()
        rotated_thrice = shape.rotate_right()

        assert block == [[0, 1, 0],
                         [1, 1, 1],
                         [0, 0, 0]]

        assert rotated == [[0, 1, 0],
                           [0, 1, 1],
                           [0, 1, 0]]

        assert rotated_twice == [[0, 0, 0],
                                 [1, 1, 1],
                                 [0, 1, 0]]

        assert rotated_thrice == [[0, 1, 0],
                                  [1, 1, 0],
                                  [0, 1, 0]]

    def test_rotating_J_shape_four_times_results_in_original_shape(self):
        """"""
        shape = MinoJ()
        block = shape.shape
        rotated = shape.rotate_right()
        rotated_twice = shape.rotate_right()
        rotated_thrice = shape.rotate_right()
        original_shape = shape.rotate_right()

        assert original_shape == block      
        
        rotated = shape.rotate_left()
        rotated_twice = shape.rotate_left()
        rotated_thrice = shape.rotate_left()
        original_shape = shape.rotate_left()

        assert original_shape == block

    def test_rotating_I_shape_can_only_rotate_right_and_left_once(self):
        """"""
        shape = MinoI()
        block = shape.shape

        assert block == [[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [1, 1, 1, 1, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]]
                                  