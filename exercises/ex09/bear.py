"""File to define Bear class."""

__author__ = "730406136"


class Bear:
    """Bear class definition."""
    
    age: int
    hunger_score: int

    def __init__(self):
        """Initializes a new bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Simulates one day for each bear."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Updates Bear's hunger_score so that it increases by num_fish."""
        self.hunger_score += num_fish