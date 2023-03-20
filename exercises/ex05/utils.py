"""EX05 - `list` Utility Functions."""

__author__ = '730406136'

evens_list: list[int]
sub_list: list[int]


def only_evens(int_list: list[int]) -> list[int]:
    """Given a list of ints, returns only the even elements."""
    idx: int = 0
    evens_list: list[int] = []
    stop: int = len(int_list)
    for idx in range(0, stop):
        if int_list[idx] % 2 == 0:
            evens_list.append(int_list[idx])
        else:
            idx += 1
    return evens_list
    

def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists of ints, returns all elements of the first list, followed by all elements of the second list."""
    return list1 + list2


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints, a start index, and an end index, returns a list which is a subset of the given list."""
    j: int = 0
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if start >= len(a_list) or end <= 0 or len(a_list) == 0:
        return []
    sub_list: list[int] = []
    for j in range(start, end):
        sub_list.append(a_list[j])
    return sub_list