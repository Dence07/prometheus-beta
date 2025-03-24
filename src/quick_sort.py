def quick_sort(arr):
    """
    Implement the Quick Sort algorithm to sort a list in ascending order.
    
    Quick Sort is an efficient, in-place sorting algorithm that uses a divide-and-conquer strategy.
    It works by selecting a 'pivot' element and partitioning the array around the pivot,
    such that elements smaller than the pivot are moved to the left, and 
    elements larger than the pivot are moved to the right.
    
    Args:
        arr (list): The list to be sorted. Can contain elements of comparable types.
    
    Returns:
        list: A new sorted list with elements in ascending order.
    
    Time Complexity: 
        - Average and Best Case: O(n log n)
        - Worst Case (rare): O(n^2)
    Space Complexity: O(log n) due to recursive calls
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Handle edge cases
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Empty or single-element lists are already sorted
    if len(arr) <= 1:
        return arr
    
    def _quick_sort(low, high):
        """
        Internal recursive helper function to perform quick sort.
        
        Args:
            low (int): Starting index of the subarray
            high (int): Ending index of the subarray
        """
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = _partition(low, high)
            
            # Recursively sort the left and right subarrays
            _quick_sort(low, pivot_index - 1)
            _quick_sort(pivot_index + 1, high)
    
    def _partition(low, high):
        """
        Partition the subarray and return the pivot index.
        
        Uses the last element as the pivot and places it in its correct position.
        
        Args:
            low (int): Starting index of the subarray
            high (int): Ending index of the subarray
        
        Returns:
            int: The index of the pivot after partitioning
        """
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Index of smaller element
        i = low - 1
        
        # Traverse through the array
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                # Increment index of smaller element
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Place pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Start the sorting process
    _quick_sort(0, len(arr) - 1)
    
    return arr