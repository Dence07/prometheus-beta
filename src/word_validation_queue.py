class Queue:
    """
    A simple Queue implementation using a list.
    
    This Queue supports basic operations like enqueue, dequeue, 
    peek, and checking if the queue is empty.
    """
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self._items = []
    
    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Args:
            item: The item to be added to the queue.
        """
        self._items.append(item)
    
    def dequeue(self):
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item in the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)
    
    def peek(self):
        """
        Return the first item in the queue without removing it.
        
        Returns:
            The first item in the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty queue")
        return self._items[0]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: Number of items in the queue.
        """
        return len(self._items)

def is_word_valid(word, rules):
    """
    Determine if a given word is valid based on a set of rules.
    
    Args:
        word (str): The word to validate.
        rules (dict): A dictionary of validation rules.
    
    Returns:
        bool: True if the word is valid, False otherwise.
    
    Rules can include:
    - 'min_length': Minimum allowed word length
    - 'max_length': Maximum allowed word length
    - 'allowed_chars': List of allowed characters
    - 'start_with': List of allowed starting characters
    - 'end_with': List of allowed ending characters
    """
    # Handle empty input
    if not word or not isinstance(word, str):
        return False
    
    # Check minimum length
    if 'min_length' in rules:
        if len(word) < rules['min_length']:
            return False
    
    # Check maximum length
    if 'max_length' in rules:
        if len(word) > rules['max_length']:
            return False
    
    # Check allowed characters
    if 'allowed_chars' in rules:
        if not all(char in rules['allowed_chars'] for char in word):
            return False
    
    # Check starting characters
    if 'start_with' in rules:
        if word[0] not in rules['start_with']:
            return False
    
    # Check ending characters
    if 'end_with' in rules:
        if word[-1] not in rules['end_with']:
            return False
    
    return True