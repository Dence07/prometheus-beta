import pytest
from src.unique_coordinate_combinations import get_unique_coordinate_combinations

def test_basic_unique_coordinates():
    """Test basic functionality with unique coordinates"""
    input_coords = [(1, 2), (3, 4), (5, 6)]
    expected = [(1, 2), (3, 4), (5, 6)]
    assert get_unique_coordinate_combinations(input_coords) == expected

def test_duplicate_coordinates():
    """Test removal of duplicate coordinates"""
    input_coords = [(1, 2), (1, 2), (3, 4), (3, 4), (5, 6)]
    expected = [(1, 2), (3, 4), (5, 6)]
    assert get_unique_coordinate_combinations(input_coords) == expected

def test_sorting_coordinates():
    """Test sorting of coordinates"""
    input_coords = [(5, 6), (1, 2), (3, 4)]
    expected = [(1, 2), (3, 4), (5, 6)]
    assert get_unique_coordinate_combinations(input_coords) == expected

def test_empty_list():
    """Test with an empty list"""
    assert get_unique_coordinate_combinations([]) == []

def test_invalid_input_not_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_type():
    """Test raising ValueError for invalid coordinate types"""
    with pytest.raises(ValueError, match="Each coordinate must be a tuple of two integers"):
        get_unique_coordinate_combinations([(1, 2), "invalid", (3, 4)])

def test_invalid_coordinate_length():
    """Test raising ValueError for coordinate tuples of incorrect length"""
    with pytest.raises(ValueError, match="Each coordinate must be a tuple of two integers"):
        get_unique_coordinate_combinations([(1, 2), (1, 2, 3), (3, 4)])

def test_invalid_coordinate_values():
    """Test raising ValueError for non-integer coordinate values"""
    with pytest.raises(ValueError, match="Each coordinate must be a tuple of two integers"):
        get_unique_coordinate_combinations([(1, 2), (1.5, 3), (3, 4)])