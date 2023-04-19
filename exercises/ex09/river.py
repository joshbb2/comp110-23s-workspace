"""File to define River class."""

__author__ = "730406136"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River class definition."""

    day: int  # tells what day of river's lifecycle you are modeling.
    bears: list[Bear]  # stores the river's bear population
    fish: list[Fish]  # stores the river's fish population
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of all bears and fish."""
        alive_fish: list[Fish] = []
        for fishy in self.fish:
            if fishy.age <= 3:
                alive_fish.append(fishy)
        self.fish = alive_fish
        alive_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                alive_bears.append(bear)
        self.bears = alive_bears
        return None
    
    def remove_fish(self, amount: int):
        """Removes amount many Fish from the River."""
        for x in range(0, amount):
            self.fish.pop(x)
        return None

    def bears_eating(self):
        """Simulates each bear eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)  
        return None

    def check_hunger(self):
        """Checks which bears are fed and which starve."""
        fed_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                fed_bears.append(bear)
        self.bears = fed_bears
        return None
        
    def repopulate_fish(self):
        """Simulates fish reproduction."""
        num_fish: int = len(self.fish)
        fish_born: int = (num_fish // 2 * 4)
        fish_to_add: list[Fish] = []
        while len(fish_to_add) < fish_born:
            fish_to_add.append(Fish())
        self.fish += fish_to_add
        return None
    
    def repopulate_bears(self):
        """Simulates bear reproduction."""
        bears_born: int = (len(self.bears) // 2)
        # bears_to_add: list[Bear] = []
        j: int = 0
        while j < bears_born:
            self.bears.append(Bear())
            j += 1
        return None
    
    def view_river(self):
        """Prints the river status."""
        x = self.day
        y = len(self.fish)
        z = len(self.bears)
        print(f"~~~ Day {x}: ~~~\nFish population: {y}\nBear population: {z}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bearss
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day() 7 times."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()