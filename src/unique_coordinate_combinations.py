from typing import List, Tuple

def get_unique_coordinate_combinations(coordinates: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Generate a list of unique coordinate combinations from the input list.
    
    Args:
        coordinates (List[Tuple[int, int]]): A list of coordinate pairs.
    
    Returns:
        List[Tuple[int, int]]: A sorted list of unique (x, y) coordinate combinations.
    
    Raises:
        TypeError: If input is not a list of coordinate pairs.
        ValueError: If any coordinate pair is invalid.
    """
    # Validate input
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Validate each coordinate pair
    for coord in coordinates:
        if not (isinstance(coord, tuple) and len(coord) == 2 and 
                all(isinstance(x, int) for x in coord)):
            raise ValueError("Each coordinate must be a tuple of two integers")
    
    # Create a set of unique coordinates to remove duplicates
    unique_coords = set(coordinates)
    
    # Sort the unique coordinates 
    return sorted(unique_coords)