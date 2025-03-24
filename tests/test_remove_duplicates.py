import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicate characters."""
    assert remove_duplicate_chars('hello') == 'helo'
    assert remove_duplicate_chars('aabbbccc') == 'abc'
    assert remove_duplicate_chars('python') == 'python'

def test_remove_duplicates_empty():
    """Test handling of empty string."""
    assert remove_duplicate_chars('') == ''

def test_remove_duplicates_all_same():
    """Test string with all same characters."""
    assert remove_duplicate_chars('aaaaa') == 'a'

def test_remove_duplicates_mixed_case():
    """Test handling of mixed case characters."""
    assert remove_duplicate_chars('HeLLo') == 'Helo'

def test_remove_duplicates_special_chars():
    """Test handling of special characters and spaces."""
    assert remove_duplicate_chars('a!b@c#a') == 'a!b@c#'

def test_remove_duplicates_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)
    with pytest.raises(TypeError):
        remove_duplicate_chars(['a', 'b', 'c'])