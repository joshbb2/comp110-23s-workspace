"""EX08 - Data Wrangling (Functions)"""

from csv import DictReader

__author__ = "730406136"


def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header"""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys"""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(original_dict: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    smaller_data_set: dict[str, list[str]] = {}
    for key in original_dict:
            sub_list: list[str] = []
            data_to_get: list[str] = original_dict[key]
            j: int = 0
            while j < rows:
                sub_list.append(data_to_get[j])
                j += 1
            smaller_data_set[key] = sub_list
    return smaller_data_set


def select(subset_columns: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    smaller_data_set_2: dict[str, list[str]] = {}
    # while len(smaller_data_set_2) < 10:
    for column in column_names:
        smaller_data_set_2[column] = subset_columns[column]
    return smaller_data_set_2


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in dict_1:
        result[key] = dict_1[key]
    for column in dict_2:
        if column in result:
            result[column] += dict_2[column]
        else:
            result[column] = dict_2[column]
    return result


def count(list_1: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in list_1:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
        