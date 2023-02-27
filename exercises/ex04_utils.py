"""EX04 - Utility Functions."""

__author__ = "730406136"


def all(list_all: list[int], integer: int) -> bool:
    i = 0
    if len(list_all) == 0:
            return False
    while i < len(list_all) - 1:
        if list_all[i] == integer:
            i += 1
        else:
            return False
    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    j = 1
    max: int = input[0]
    while j < len(input) - 1:
        if max < input[j]:
            max = input[j]
        else:
            max: int = input[0]
        j += 1
    return max

def is_equal(list1: list[int], list2: list[int]) -> bool:
    k = 0
    while k < len(list1) - 1:
        if list1[k] == list2[k]:
            k += 1
        else:
            return False
    return True

        
    
