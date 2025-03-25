import pytest
from src.alternating_title_case import convert_to_alternating_title_case

def test_alternating_title_case_basic():
    """Test basic functionality of alternating title case."""
    assert convert_to_alternating_title_case("hello world python programming") == \
           "Hello world Python programming"

def test_alternating_title_case_single_word():
    """Test single word conversion."""
    assert convert_to_alternating_title_case("hello") == "Hello"

def test_alternating_title_case_empty_string():
    """Test empty string handling."""
    assert convert_to_alternating_title_case("") == ""

def test_alternating_title_case_multiple_words():
    """Test conversion with multiple words."""
    assert convert_to_alternating_title_case("a b c d e") == \
           "A b C d E"

def test_alternating_title_case_mixed_case():
    """Test conversion with mixed case input."""
    assert convert_to_alternating_title_case("HELLO world PYTHON programming") == \
           "Hello world Python programming"

def test_alternating_title_case_single_character():
    """Test single character conversion."""
    assert convert_to_alternating_title_case("a") == "A"

def test_alternating_title_case_error_non_string():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_title_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_title_case(None)

def test_alternating_title_case_whitespace():
    """Test handling of extra whitespace."""
    assert convert_to_alternating_title_case("  hello   world  ") == \
           "Hello world"