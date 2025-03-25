import pytest
from src.word_validation_queue import Queue, is_word_valid

def test_queue_basic_operations():
    """Test basic Queue operations."""
    q = Queue()
    
    # Test initial state
    assert q.is_empty() == True
    assert q.size() == 0
    
    # Test enqueue
    q.enqueue(1)
    assert q.is_empty() == False
    assert q.size() == 1
    
    # Test peek
    assert q.peek() == 1
    
    # Test dequeue
    assert q.dequeue() == 1
    assert q.is_empty() == True

def test_queue_error_handling():
    """Test Queue error handling."""
    q = Queue()
    
    # Test dequeue on empty queue
    with pytest.raises(IndexError):
        q.dequeue()
    
    # Test peek on empty queue
    with pytest.raises(IndexError):
        q.peek()

def test_is_word_valid_basic():
    """Test basic word validation scenarios."""
    # Test minimum length
    rules = {'min_length': 3}
    assert is_word_valid('cat', rules) == True
    assert is_word_valid('hi', rules) == False
    
    # Test maximum length
    rules = {'max_length': 5}
    assert is_word_valid('hello', rules) == True
    assert is_word_valid('python', rules) == False

def test_is_word_valid_allowed_chars():
    """Test allowed characters rule."""
    rules = {'allowed_chars': ['a', 'b', 'c']}
    assert is_word_valid('abc', rules) == True
    assert is_word_valid('abd', rules) == False
    
def test_is_word_valid_start_end():
    """Test start and end with rules."""
    rules = {
        'start_with': ['a', 'b'],
        'end_with': ['x', 'y']
    }
    assert is_word_valid('ax', rules) == True
    assert is_word_valid('by', rules) == True
    assert is_word_valid('cx', rules) == False
    assert is_word_valid('ay', rules) == True

def test_is_word_valid_combined_rules():
    """Test multiple validation rules together."""
    rules = {
        'min_length': 3,
        'max_length': 5,
        'allowed_chars': ['a', 'b', 'c'],
        'start_with': ['a'],
        'end_with': ['b']
    }
    assert is_word_valid('acb', rules) == True
    assert is_word_valid('ab', rules) == False   # Too short
    assert is_word_valid('abcde', rules) == False  # Too long
    assert is_word_valid('axc', rules) == False  # Invalid start/end
    
def test_is_word_valid_edge_cases():
    """Test edge cases for word validation."""
    # Empty input
    assert is_word_valid('', {}) == False
    assert is_word_valid(None, {}) == False
    
    # No rules
    assert is_word_valid('hello', {}) == True