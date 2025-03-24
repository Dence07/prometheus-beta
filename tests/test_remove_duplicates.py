import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    assert remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]

def test_remove_duplicates_preserves_order():
    """Ensure first occurrence of each element is preserved"""
    assert remove_duplicates([3, 1, 2, 1, 3, 4]) == [3, 1, 2, 4]

def test_remove_duplicates_empty_list():
    """Test behavior with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_remove_duplicates_with_strings():
    """Test duplicate removal with string elements"""
    assert remove_duplicates(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']

def test_remove_duplicates_mixed_types():
    """Test duplicate removal with mixed types"""
    assert remove_duplicates([1, '1', 1, 'a', 'a']) == [1, '1', 'a']

def test_remove_duplicates_invalid_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
        remove_duplicates(123)
        remove_duplicates(None)