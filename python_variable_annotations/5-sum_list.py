#!/usr/bin/python3
"""
type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float

"""

from typing import list


def sum_list(input_list: list[float]) -> float:
    """return sum of floats"""
    return sum(input_list)
