"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    values: list[float]

    def __init__(self, list1: list[float]):
        """Initializes value attribute of newly constructed Simpy object to list1."""
        self.values = list1
    
    def __str__(self) -> str:
        """Represents Simpy object as a string."""
        return f"Simpy({self.values})"
    
    def fill(self, float_val: float, num_vals: int):
        """Fills a Simpy's values with a specific number of repeating float values."""
        while len(self.values) < num_vals:
            self.values.append(float_val)
        return None
    
    def arange(self, start: float, stop: float, step: float = 1.0):
        """Fills in the values attribute with range of float values."""
        assert step != 0.0
        x: float = start
        while x != stop:
            self.values.append(x)
            x += step
        return None
    
    def sum(self) -> float:
        """Computes and returns the sum of all items in the values attribute."""
        sum_total: float = sum(self.values)
        return sum_total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        is_float: bool = False
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            summed_vals: list[float] = []
            j: int = 0
            for item in rhs.values:
                add_items: float = self.values[j] + item
                summed_vals.append(add_items)
                j += 1
            new_object_simpy: Simpy = Simpy(summed_vals)
        if type(rhs) == float:
            is_float = True
            added_vals: list[float] = []
            for value in self.values:
                sum_items: float = value + rhs
                added_vals.append(sum_items)
            new_object_float: Simpy = Simpy(added_vals)
        if not is_float:
            return new_object_simpy
        else:
            return new_object_float
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        is_float: bool = False
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            power_vals: list[float] = []
            i: int = 0
            for item in rhs.values:
                pow_items: float = self.values[i] ** item
                power_vals.append(pow_items)
                i += 1
            new_object_simpy: Simpy = Simpy(power_vals)
        if type(rhs) == float:
            is_float = True
            exp_vals: list[float] = []
            for value in self.values:
                exp_items: float = value ** rhs
                exp_vals.append(exp_items)
            new_object_float: Simpy = Simpy(exp_vals)
        if not is_float:
            return new_object_simpy
        else:
            return new_object_float
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        is_float: bool = False
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            bool_list_simpy: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if rhs.values[i] == self.values[i]:
                    bool_list_simpy.append(True)
                else:
                    bool_list_simpy.append(False)
                i += 1
        if type(rhs) == float:
            is_float = True
            bool_list_float: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if rhs == self.values[i]:
                    bool_list_float.append(True)
                else:
                    bool_list_float.append(False)
                i += 1
        if not is_float:
            return bool_list_simpy
        else:
            return bool_list_float


        







    # TODO: Your constructor and methods will go here.