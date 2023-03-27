"""EX07 Function Tests."""

__author__ = "730406136"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count

def test_invert_use_1() -> None:
    assert invert({'hello': 'world', 'ice': 'cream', 'sun': 'screen'}) == {'world': 'hello', 'cream': 'ice', 'screen': 'sun'}

def test_invert_use_2() -> None:
    assert invert({'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'}) == {'b': 'a', 'd': 'c', 'f': 'e', 'h':'g'}

def test_invert_edge() -> None:
    assert invert({'monday': 'tuesday', 'wednesday': 'thursday', 'monday': 'friday'}) == KeyError

def test_favorite_color_use_1() -> None:
    assert favorite_color({'josh': 'blue', 'gabriel': 'red', 'betty': 'blue', 'sam': 'green'}) == 'blue'

def test_favorite_color_use_2() -> None:
    assert favorite_color({'hello': 'pink', 'sunny': 'purple', 'sunny': 'pink', 'entire': 'pink', 'goodbye': 'yellow'}) == 'pink'

def test_favorite_color_edge() -> None:
    assert favorite_color({'apple': 'green', 'pear': 'yellow', 'peach': 'red', 'kiwi': 'green', 'pineapple': 'yellow'}) == 'green'

def test_count_use_1() -> None:
    assert count(['josh', 'gabriel', 'betty', 'trevor', 'josh', 'gabriel', 'josh']) == {'josh': 3, 'gabriel': 2, 'betty': 1, 'trevor': 1}

def test_count_use_2() -> None:
    assert count(['chocolate', 'vanilla', 'strawberry', 'vanilla', 'strawberry', 'mint', 'vanilla']) == {'chocolate': 1, 'vanilla': 3, 'strawberry': 2, 'mint': 1}

def test_count_edge() -> None:
    assert count([]) == {}




