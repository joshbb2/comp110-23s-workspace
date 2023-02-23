"""Utility Functions."""

__author__ = "730406136"

list_all: list[int] = list()

def all(list_all, integer: int) -> bool:
    i = 0
    while i < len(list_all) - 1:
        if list_all[i] == integer:
            i += 1
        else:
            return False
    return True
