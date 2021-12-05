import pytest
from rotate import Rotate


class TestRotatingBlocks:
    @pytest.fixture
    def three(self):
        block1 = Rotate(
            [[0, 1, 0],
             [1, 1, 0],
             [0, 0, 0]]
        )
        yield block1

    @pytest.fixture
    def five(self):
        block2 = Rotate(
            [[0, 0, 1, 0, 0],
             [0, 1, 1, 0, 0],
             [1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
        )
        yield block2

    def test_block_can_rotate_right(self, three, five):
        assert three.rotate_right() == [[0, 1, 0],
                                        [0, 1, 1],
                                        [0, 0, 0]]

        assert five.rotate_right() == [[0, 0, 1, 0, 0],
                                       [0, 0, 1, 1, 0],
                                       [0, 0, 1, 1, 1],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0]]

    def test_block_can_rotate_left(self, three, five):
        assert three.rotate_left() == [[0, 0, 0],
                                       [1, 1, 0],
                                       [0, 1, 0]]

        assert five.rotate_left() == [[0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0],
                                      [1, 1, 1, 0, 0],
                                      [0, 1, 1, 0, 0],
                                      [0, 0, 1, 0, 0]]

    def test_four_rotations_equal_initial_orientation(self, three, five):
        
        assert three.rotate().rotate().rotate().rotate().block == [[0, 1, 0],
                                                                   [1, 1, 0],
                                                                   [0, 0, 0]]

        assert five.rotate().rotate().rotate().rotate().block == [[0, 0, 1, 0, 0],
                                                                  [0, 1, 1, 0, 0],
                                                                  [1, 1, 1, 0, 0],
                                                                  [0, 0, 0, 0, 0],
                                                                  [0, 0, 0, 0, 0]]
        