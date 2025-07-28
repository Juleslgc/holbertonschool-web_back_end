#!/usr/bin/env python3
"""
It contains the function:
sum_list()
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A function that return the sum of a list

    Args:
        a (list of float): List of float

    Return:
        The sum to the list of float
    """
    return sum(input_list)
