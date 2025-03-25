from typing import List, Dict

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
    
    # Set to store unique sorted anagram signatures
    unique_anagrams = set()
    
    # Generate all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            # Get current substring
            substring = s[i:j]
            
            # Create a sorted signature to identify anagrams
            sorted_substring = ''.join(sorted(substring))
            
            # Add to set of unique anagram signatures
            unique_anagrams.add(sorted_substring)
    
    # Return the count of unique anagram signatures
    return len(unique_anagrams)