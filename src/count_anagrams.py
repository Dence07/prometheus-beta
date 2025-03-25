from typing import List, Set

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagram substrings in the given string.
    
    An anagram is considered distinct based on its sorted character signature,
    with additional constraint that only the first unique signature for each 
    substring length is counted.
    
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
    
    # Track unique signatures, with additional tracking for each length
    unique_anagrams: Set[str] = set()
    
    # For each possible substring length
    for length in range(1, len(s) + 1):
        # Track unique signatures for this specific length
        unique_for_length: Set[str] = set()
        
        # Check all substrings of current length
        for start in range(len(s) - length + 1):
            # Extract substring
            substring = s[start:start+length]
            
            # Create sorted signature
            signature = ''.join(sorted(substring))
            
            # Only count if this is the first time we've seen this signature
            if signature not in unique_for_length:
                unique_for_length.add(signature)
                unique_anagrams.add(signature)
    
    # Return the count of unique anagram signatures
    return len(unique_anagrams)