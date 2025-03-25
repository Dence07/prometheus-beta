def find_median_index(arr):
    """
    Find the median index or value in a sorted array of integers.
    
    Args:
        arr (list): A sorted list of integers.
    
    Returns:
        float or int: For odd-length arrays, returns the index of the median.
                      For even-length arrays, returns the average of the two middle indices.
    
    Raises:
        ValueError: If the input array is empty.
    """
    # Check for empty array
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Get the length of the array
    n = len(arr)
    
    # If the array has an odd number of elements
    if n % 2 == 1:
        # Return the index of the middle element
        return n // 2
    
    # If the array has an even number of elements
    else:
        # Return the average of the two middle indices
        left_mid = (n // 2) - 1
        right_mid = n // 2
        return (left_mid + right_mid) / 2