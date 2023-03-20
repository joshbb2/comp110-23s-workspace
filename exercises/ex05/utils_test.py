"""Unit tests for EX05 functions - only_evens, sub, concat."""

__author__ = '730406136'

from exercises.ex05.utils import only_evens, sub, concat


def test_all_odds() -> None:
    """Tests only_evens with an empty list."""
    test_list: list[int] = [-3, -5, -7, -9]
    assert only_evens(test_list) == []


def test_all_evens() -> None:
    """Tests only_evens with a list consisting of all even ints."""
    test_list: list[int] = [-2, -4, -6, -8]
    assert only_evens(test_list) == test_list


def test_empty_list() -> None:
    """Tests only_evens with a list consisting of all odd ints."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_use1() -> None:
    """Tests use case of concat, with two lists of positive ints."""
    test_list1: list[int] = [1, 1, 1]
    test_list2: list[int] = [2, 2, 2]
    assert concat(test_list1, test_list2) == [1, 1, 1, 2, 2, 2]


def test_use2() -> None:
    """Tests use case of concat, with two lists of negative ints."""
    test_list1: list[int] = [-5, -7, -2, -8]
    test_list2: list[int] = [-4, -2, -6, -10]
    assert concat(test_list1, test_list2) == [-5, -7, -2, -8, -4, -2, -6, -10]


def test_both_empty_lists() -> None:
    """Tests edge case of concat, with arguments of the incorrect type."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_subset_use1() -> None:
    """Tests use case of sub, to return a subset of the given list."""
    test_list: list[int] = [0, 45, -100, 33, -51, 12]
    start_at_idx: int = 0
    end_at_idx: int = len(test_list)
    assert sub(test_list, start_at_idx, end_at_idx)


def test_subset_use2() -> None:
    """Tests use case of sub, to return a subset of the given list."""
    the_list: list[int] = [5, 10, 15, 20, 25, 30]
    start_idx: int = 2
    end_idx: int = 5
    assert sub(the_list, start_idx, end_idx) == [15, 20, 25]


def test_edge_idx() -> None:
    """Tests sub edge cases, with a negative start index and an end index greater than the length of the list."""
    test_list: list[int] = [-10, -9, -8, -7, -6]
    begin_at_idx: int = -5
    stop_at_idx: int = 10
    assert sub(test_list, begin_at_idx, stop_at_idx) == [-10, -9, -8, -7, -6]