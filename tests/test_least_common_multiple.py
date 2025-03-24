import pytest
from src.least_common_multiple import find_lcm

def test_find_lcm_basic():
    """Test basic LCM calculations"""
    assert find_lcm(4, 6) == 12
    assert find_lcm(21, 6) == 42
    assert find_lcm(17, 5) == 85

def test_find_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert find_lcm(7, 7) == 7

def test_find_lcm_coprime():
    """Test LCM for coprime numbers"""
    assert find_lcm(5, 7) == 35

def test_find_lcm_one_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert find_lcm(3, 9) == 9
    assert find_lcm(9, 3) == 9

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_lcm(3.5, 4)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(-1, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(5, -3)