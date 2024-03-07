import pytest

@pytest.fixture
def basic_block_array():
    return [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1], "123 1378 167"

@pytest.fixture
def double_zero_block_array():
    return [2, 1, 0, 0, 3, 4], "12 X 34"

@pytest.fixture
def empty_elements_block_array():
    return [2, 1, 0], "X"

@pytest.fixture
def empty_elements_block_array_v2():
    return [0, 2, 1], "X"