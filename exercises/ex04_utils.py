"""EX04 - Utility Functions."""

__author__ = "730406136"


def all(list_all: list[int], integer: int) -> bool:
    #Determines if all ints in a list are equal to a given int.
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
    #Given a list of ints, returns the largest int.
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    j = 1
    max: int = input[0]
    while j < len(input):
        if max < input[j]:
            max = input[j]
        else:
            j += 1
        j += 1
    return max

def is_equal(list1: list[int], list2: list[int]) -> bool:
    #Given two lists of ints, returns True if every element at every index is equal in both lists.
    k = 0
    if len(list1) != len(list2):
        return False
    while k < (len(list1) and len(list2)) - 1:
        if list1[k] == list2[k]:
            k += 1
        else:
            return False
    return True

        
    
