import pytest
from mino import (MinoO, MinoS, MinoZ,
                    MinoJ, MinoL, MinoT, MinoI)

class TestMinoRotation:
    def test_all_minos_exist(self):
        """"""
        assert MinoO().block == [[1, 1, 0],
                                 [1, 1, 0],
                                 [0, 0, 0]]

        assert MinoS().block == [[0, 1, 1],
                                 [1, 1, 0],
                                 [0, 0, 0]]

        assert MinoZ().block == [[1, 1, 0],
                                 [0, 1, 1],
                                 [0, 0, 0]]

        assert MinoJ().block == [[0, 1, 0],
                                 [0, 1, 0],
                                 [1, 1, 0]]

        assert MinoL().block == [[0, 1, 0],
                                 [0, 1, 0],
                                 [0, 1, 1]]

        assert MinoT().block == [[0, 1, 0],
                                 [1, 1, 1],
                                 [0, 0, 0]]

        assert MinoI().block == [[0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0]]

    def test_J_block_can_be_rotated_three_times(self):
        """"""
        block = MinoJ()
        shape = block.block
        curr_rotation = block.current_rotation
        
        assert shape == [[0, 1, 0],
                         [0, 1, 0],
                         [1, 1, 0]]

        rotated = block.rotate_right()
        assert block.new_block().block == [[1, 0, 0],
                                           [1, 1, 1],
                                           [0, 0, 0]]

        rotated_twice = block.rotate_right()
        assert block.new_block().block == [[0, 1, 1],
                                           [0, 1, 0],
                                           [0, 1, 0]]

        rotated_thrice = block.rotate_right()
        assert block.new_block().block == [[0, 0, 0],
                                           [1, 1, 1],
                                           [0, 0, 1]]

        rotated_left = block.rotate_left()
        assert block.new_block().block == [[0, 1, 1],
                                           [0, 1, 0],
                                           [0, 1, 0]]

    def test_L_block_can_be_rotated_three_times(self):
        """"""
        block = MinoL()
        shape = block.block
        curr_rotation = block.current_rotation
        
        assert shape == [[0, 1, 0],
                         [0, 1, 0],
                         [0, 1, 1]]

        rotated = block.rotate_right()
        assert block.new_block().block == [[0, 0, 0],
                                           [1, 1, 1],
                                           [1, 0, 0]]

        rotated_twice = block.rotate_right()
        assert block.new_block().block == [[1, 1, 0],
                                           [0, 1, 0],
                                           [0, 1, 0]]

        rotated_thrice = block.rotate_right()
        assert block.new_block().block == [[0, 0, 1],
                                           [1, 1, 1],
                                           [0, 0, 0]]

        rotated_left = block.rotate_left()
        assert block.new_block().block == [[1, 1, 0],
                                           [0, 1, 0],
                                           [0, 1, 0]]

    def test_T_block_can_be_rotated_three_times(self):
        """"""
        block = MinoT()
        shape = block.block
        curr_rotation = block.current_rotation
        
        assert shape == [[0, 1, 0],
                         [1, 1, 1],
                         [0, 0, 0]]

        rotated = block.rotate_right()
        assert block.new_block().block == [[0, 1, 0],
                                           [0, 1, 1],
                                           [0, 1, 0]]

        rotated_twice = block.rotate_right()
        assert block.new_block().block == [[0, 0, 0],
                                           [1, 1, 1],
                                           [0, 1, 0]]

        rotated_thrice = block.rotate_right()
        assert block.new_block().block == [[0, 1, 0],
                                           [1, 1, 0],
                                           [0, 1, 0]]

        rotated_left = block.rotate_left()
        assert block.new_block().block == [[0, 0, 0],
                                           [1, 1, 1],
                                           [0, 1, 0]]
                                
    def test_rotating_J_block_four_times_results_in_original_block(self):
        """"""
        block = MinoJ()
        shape = block.block
        rotated = block.rotate_right()
        rotated_twice = block.rotate_right()
        rotated_thrice = block.rotate_right()
        original_block = block.rotate_right()

        assert block.new_block().block == shape      
        
        rotated = block.rotate_left()
        rotated_twice = block.rotate_left()
        rotated_thrice = block.rotate_left()
        original_block = block.rotate_left()

        assert block.new_block().block == shape

    def test_I_block_only_has_two_rotations_(self):
        """"""
        block = MinoI()
        shape = block.block
        
        assert shape == [[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [1, 1, 1, 1, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]]

        rotate_right = block.rotate_right()
        assert block.new_block().block == [[0, 0, 0, 0, 0],
                                           [0, 0, 1, 0, 0],
                                           [0, 0, 1, 0, 0],
                                           [0, 0, 1, 0, 0],
                                           [0, 0, 1, 0, 0]]

        rotate_left = block.rotate_left()
        assert block.new_block().block == shape

    def test_rotating_I_block_two_times_in_any_direction_results_in_the_original_block(self):
        """"""
        block = MinoI()
        shape = block.block
        block.rotate_right()
        block.rotate_right()
        assert block.new_block().block == shape
        block.rotate_left()
        block.rotate_left()
        assert block.new_block().block == shape
                   
    def test_O_block_has_same_orientation_when_rotated_in_any_direction(self):
        """"""
        block = MinoO()
        shape = block.block

        assert shape == [[1, 1, 0],
                         [1, 1, 0],
                         [0, 0, 0]]

        rotate_right = block.rotate_right()
        assert block.new_block().block == [[1, 1, 0],
                                           [1, 1, 0],
                                           [0, 0, 0]]

        rotate_left = block.rotate_left()
        assert block.new_block().block == [[1, 1, 0],
                                           [1, 1, 0],
                                           [0, 0, 0]]
        
        rotate_left = block.rotate_left()
        rotate_left = block.rotate_left()
        assert block.new_block().block == shape
