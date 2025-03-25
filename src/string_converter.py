def to_kebab_case(s: str) -> str:
    """
    Convert a given string to kebab-case.
    
    Converts different string formats (camelCase, snake_case, PascalCase, 
    space-separated) to kebab-case (lowercase with hyphens).
    
    Args:
        s (str): The input string to convert
    
    Returns:
        str: The string converted to kebab-case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_kebab_case("helloWorld")
        'hello-world'
        >>> to_kebab_case("Hello World")
        'hello-world'
        >>> to_kebab_case("hello_world")
        'hello-world'
        >>> to_kebab_case("HelloWorld")
        'hello-world'
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not s:
        return ""
    
    # Replace non-alphanumeric characters with hyphens
    import re
    import unicodedata
    
    # Normalize unicode characters
    s = unicodedata.normalize('NFKD', s)
    
    # Convert camelCase and PascalCase to hyphen-separated
    s = re.sub(r'(?<!^)(?=[A-Z])', '-', s)
    
    # Replace underscores, non-letter characters with spaces first
    s = re.sub(r'[_\W]', ' ', s)
    
    # Split on multiple whitespaces and filter meaningful parts 
    words = [word for word in s.split() if word]
    
    # Convert to lowercase 
    return '-'.join(word.lower() for word in words)