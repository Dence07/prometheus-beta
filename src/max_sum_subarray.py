def max_sum_subarray(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    This function uses Kadane's algorithm to find the maximum sum subarray, 
    which can include elements from the beginning, middle, or end of the array.
    
    Args:
        arr (list): A list of integers to find the maximum sum subarray from.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input array.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> max_sum_subarray([1, -2, 3, 4, -1, 5])
        11
        >>> max_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3])
        7
    """
    # Check input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_ending_here = max_so_far = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Kadane's algorithm: choose between extending the current subarray 
        # or starting a new subarray from the current element
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum sum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far