"""River simulation function calling document."""

__author__ = "730406136"

from exercises.ex09.river import River

my_river: River = River(10, 2)

my_river.view_river()
my_river.repopulate_bears()
my_river.one_river_week()
