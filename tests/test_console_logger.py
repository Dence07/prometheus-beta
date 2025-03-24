import pytest
import sys
from io import StringIO

from src.console_logger import log_message

def test_log_message_prints_correctly():
    """Test that log_message prints the correct message."""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    # Log a test message
    test_message = "Hello, world!"
    log_message(test_message)

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check the captured output
    assert captured_output.getvalue().strip() == test_message

def test_log_message_with_empty_string():
    """Test logging an empty string."""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    # Log an empty string
    log_message("")

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check the captured output
    assert captured_output.getvalue().strip() == ""

def test_log_message_raises_type_error_for_non_string():
    """Test that log_message raises TypeError for non-string inputs."""
    # Test with various non-string types
    non_string_inputs = [
        42,
        3.14,
        None,
        [],
        {},
        True
    ]

    for invalid_input in non_string_inputs:
        with pytest.raises(TypeError, match="Message must be a string"):
            log_message(invalid_input)