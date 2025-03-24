import pytest
from src.timestamp_difference import calculate_timestamp_difference


def test_basic_timestamp_difference():
    """Test basic timestamp difference calculation"""
    result = calculate_timestamp_difference(
        "2023-01-01 10:00:00", 
        "2023-01-01 11:00:00"
    )
    assert result == 3600  # 1 hour = 3600 seconds


def test_same_timestamp():
    """Test timestamp difference when times are identical"""
    result = calculate_timestamp_difference(
        "2023-01-01 10:00:00", 
        "2023-01-01 10:00:00"
    )
    assert result == 0


def test_negative_time_difference():
    """Test time difference works regardless of order of timestamps"""
    result = calculate_timestamp_difference(
        "2023-01-01 11:00:00", 
        "2023-01-01 10:00:00"
    )
    assert result == 3600  # 1 hour = 3600 seconds


def test_different_date_timestamp_difference():
    """Test timestamp difference across different dates"""
    result = calculate_timestamp_difference(
        "2023-01-01 00:00:00", 
        "2023-01-02 00:00:00"
    )
    assert result == 86400  # 1 day = 86400 seconds


def test_custom_format():
    """Test timestamp difference with custom format"""
    result = calculate_timestamp_difference(
        "01/01/2023 10:00:00", 
        "01/01/2023 11:00:00", 
        format="%m/%d/%Y %H:%M:%S"
    )
    assert result == 3600  # 1 hour = 3600 seconds


def test_invalid_timestamp_format():
    """Test error handling for invalid timestamp format"""
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference(
            "invalid-timestamp", 
            "2023-01-01 10:00:00"
        )


def test_empty_timestamp():
    """Test error handling for empty timestamps"""
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference(
            "", 
            "2023-01-01 10:00:00"
        )