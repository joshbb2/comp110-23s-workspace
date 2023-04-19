"""File to define Fish class."""

__author__ = "730406136"


class Fish:
    """Fish class definition."""

    age: int
    
    def __init__(self):
        """Initializes a new fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Simulates one day for each fish."""
        self.age += 1
        return None