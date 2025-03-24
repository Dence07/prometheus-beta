import pytest
from src.replace_spaces import replace_spaces_with_underscores

def test_basic_string_replacement():
    """Test basic string space replacement."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_multiple_spaces():
    """Test replacement of multiple spaces."""
    assert replace_spaces_with_underscores("hello  world  test") == "hello__world__test"

def test_spaces_at_edges():
    """Test replacement of spaces at the beginning and end."""
    assert replace_spaces_with_underscores("  spaces at edges  ") == "__spaces_at_edges__"

def test_empty_string():
    """Test replacement with an empty string."""
    assert replace_spaces_with_underscores("") == ""

def test_no_spaces_string():
    """Test string with no spaces."""
    assert replace_spaces_with_underscores("nospaces") == "nospaces"

def test_only_spaces():
    """Test string with only spaces."""
    assert replace_spaces_with_underscores("   ") == "___"

def test_none_input():
    """Test that None input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(None)