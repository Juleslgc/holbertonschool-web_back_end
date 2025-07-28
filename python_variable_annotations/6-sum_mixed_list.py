#!/usr/bin/env python3
"""
It contains the function:
sum_mixed_list()
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A function that return a sum to float

    Args:
        mxd_lst: A list of integer and float


    Return:
        The sum to float
    """
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum
