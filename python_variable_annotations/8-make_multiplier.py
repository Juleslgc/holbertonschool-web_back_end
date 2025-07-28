#!/usr/bin/env python3
"""
It contains the function:
make_multiplier()
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function that create a multiplier function

    Arg:
        multiplier (float): The float to multiply

    Return:
        The result to the function that multiply a float by 'multiplier'
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
