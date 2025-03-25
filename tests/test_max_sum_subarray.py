import pytest
from src.max_sum_subarray import max_sum_subarray

def test_basic_positive_array():
    """Test a basic array with positive and negative numbers."""
    assert max_sum_subarray([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test an array with all negative numbers."""
    assert max_sum_subarray([-1, -2, -3, -4]) == -1

def test_single_element_array():
    """Test an array with a single element."""
    assert max_sum_subarray([5]) == 5

def test_mixed_numbers():
    """Test an array with mixed positive and negative numbers."""
    assert max_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3]) == 7

def test_zero_sum_array():
    """Test an array where elements can sum to zero."""
    assert max_sum_subarray([1, -1, 2, -2, 3]) == 3

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_sum_subarray([])

def test_invalid_input_non_list():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_sum_subarray("not a list")

def test_large_numbers():
    """Test an array with large numbers."""
    assert max_sum_subarray([1000000, -500000, 700000, -200000]) == 1000000

def test_alternating_signs():
    """Test an array with alternating positive and negative signs."""
    assert max_sum_subarray([1, -1, 1, -1, 1]) == 1