from datetime import datetime, timedelta


def calculate_timestamp_difference(timestamp1: str, timestamp2: str, format: str = "%Y-%m-%d %H:%M:%S") -> float:
    """
    Calculate the time difference between two timestamps in seconds.

    Args:
        timestamp1 (str): First timestamp string
        timestamp2 (str): Second timestamp string
        format (str, optional): Datetime format string. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        float: Absolute time difference in seconds

    Raises:
        ValueError: If timestamps cannot be parsed or are invalid
    """
    try:
        # Parse timestamps using the specified format
        dt1 = datetime.strptime(timestamp1, format)
        dt2 = datetime.strptime(timestamp2, format)

        # Calculate absolute time difference
        time_diff = abs(dt2 - dt1)

        # Return total seconds
        return time_diff.total_seconds()
    except ValueError as e:
        # Raise a descriptive error if parsing fails
        raise ValueError(f"Invalid timestamp format. {str(e)}")