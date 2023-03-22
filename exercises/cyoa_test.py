"""Tests functions for EX06 - Choose Your Own Adventure."""

__author__ = "730406136"

from exercises.cyoa import generate_int
from random import randint

def test_generate_int() -> None:
    assert generate_int() in range(1,10)