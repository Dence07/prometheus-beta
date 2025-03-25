from typing import List, Dict
from collections import defaultdict

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagram substrings in the given string.
    
    An anagram is a substring that contains the same characters in a different order.
    
    Args:
        s (str): Input string containing only lowercase English letters.
    
    Returns:
        int: Number of distinct anagram substrings.
    
    Raises:
        ValueError: If the input string contains characters other than lowercase letters.
    
    Examples:
        >>> count_anagrams('abab')
        2
        >>> count_anagrams('aa')
        1
    """
    # Validate input
    if not s or not all(c.islower() for c in s):
        raise ValueError("Input must be a non-empty string of lowercase letters")
    
    # Use a set of sorted character tuples to count unique anagrams
    unique_anagrams = set()
    
    # Iterate through all possible substrings
    for length in range(1, len(s) + 1):
        for start in range(len(s) - length + 1):
            # Extract substring
            substring = s[start:start+length]
            
            # Create a sorted signature of characters as a tuple
            sorted_chars = tuple(sorted(substring))
            
            # Add to unique anagrams
            unique_anagrams.add(sorted_chars)
    
    # Return the count of unique anagram signatures
    return len(unique_anagrams)