"""EX07 - Dictionary Functions."""

__author__ = "730406136"

def invert(dict_1: dict[str,str]) -> dict[str,str]:
    """Inverts the keys and values of given dictionary."""
    result: dict[str,str] = {}
    for key in dict_1:
        if key in result:
            raise KeyError
        else:
            result[dict_1[key]] = key
    return result

def favorite_color(dict_1: dict[str,str]) -> str:
    """Returns color that appears most frequently."""
    all_keys: list[str] = []
    for key in dict_1:
        all_keys.append(dict_1[key])
    from statistics import mode
    most_common: str = mode(all_keys)
    return most_common

def count(list_1: list[str]) -> dict[str,int]:
    result: dict[str,int] = {}
    counter: int = 0
    for item in list_1:
        if item in result:
            counter += 1
            result[item] = counter
        else:
            counter = 1
            result[item] = counter
    return result
    
        



    
