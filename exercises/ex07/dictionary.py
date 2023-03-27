"""EX07 - Dictionary Functions."""

__author__ = "730406136"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of given dictionary."""
    result: dict[str, str] = {}
    for key in dict_1:
        if dict_1[key] in result:
            raise KeyError("Value is already in the resulting dictionary.")
        else:
            result[dict_1[key]] = key
    return result


def favorite_color(dict_1: dict[str, str]) -> str:
    """Returns color that appears most frequently."""
    all_keys: list[str] = []
    for key in dict_1:
        all_keys.append(dict_1[key])
    from statistics import mode
    most_common: str = mode(all_keys)
    return most_common


def count(list_1: list[str]) -> dict[str, int]:
    """Returns dictionary with keys as unique values from the input list, and values associated with number of appearances."""
    result: dict[str, int] = {}
    for item in list_1:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
    
        



    
