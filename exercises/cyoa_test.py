"""Tests functions for EX06 - Choose Your Own Adventure."""

__author__ = "730406136"

from exercises.cyoa import random_num

def test_value() -> None:
    assert random_num()