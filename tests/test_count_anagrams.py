import pytest
from src.count_anagrams import count_anagrams

def test_count_anagrams_basic():
    """Test basic anagram counting scenarios."""
    assert count_anagrams('abab') == 2  # Unique anagram signatures: 'a', 'ab'
    assert count_anagrams('aa') == 1    # Unique anagram signatures: 'a'
    assert count_anagrams('abc') == 3   # Unique anagram signatures: 'a', 'b', 'ab'

def test_count_anagrams_edge_cases():
    """Test edge cases for the function."""
    # Single character string
    assert count_anagrams('a') == 1
    
    # String with repeated characters
    assert count_anagrams('aaa') == 1

def test_count_anagrams_invalid_input():
    """Test error handling for invalid inputs."""
    # Empty string
    with pytest.raises(ValueError):
        count_anagrams('')
    
    # Non-lowercase letters
    with pytest.raises(ValueError):
        count_anagrams('AbC')
    
    # String with non-letter characters
    with pytest.raises(ValueError):
        count_anagrams('ab1c')