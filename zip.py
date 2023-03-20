"""Dict Function Writing."""

__author__ = "730406136"

def zip(list1: list[str], list2: list[int]) -> dict():
    result: dict[str, int] = {}
    j: int = 0
    while j < len(list2):
        for key in list1:
            result[key] = list2[j]
            j += 1
    if len(list1) != len(list2):
        return {}
    if list1 and list2 == []:
        return {}
    else:
        return result