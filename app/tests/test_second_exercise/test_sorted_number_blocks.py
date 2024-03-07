import pytest

from app.second_exercise.sort_number_blocks import sort_numbers_blocks

def test_sorted_blocks(basic_block_array):
    
    array, array_result = basic_block_array
    ordered_blocks = sort_numbers_blocks(array=array)
    assert ordered_blocks == array_result

def test_sorted_blocks_double_zero(double_zero_block_array):
    
    array, array_result = double_zero_block_array
    ordered_blocks = sort_numbers_blocks(array=array)
    assert ordered_blocks == array_result

def test_sorted_blocks_without_elements(empty_elements_block_array):
    
    array, array_result = empty_elements_block_array
    ordered_blocks = sort_numbers_blocks(array=array)
    assert ordered_blocks == array_result

def test_sorted_blocks_without_elements_v2(empty_elements_block_array_v2):
    
    array, array_result = empty_elements_block_array_v2
    ordered_blocks = sort_numbers_blocks(array=array)
    assert ordered_blocks == array_result