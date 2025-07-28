#!/usr/bin/env python3
"""
It contains the function:
to_kv()
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A function that create a tuple, first element a string
    and second element a float

    Args:
        k (string): First element of the tuple
        v (float or int): Second element of the tuple

    Return:
        The tuple of two elements
    """
    return (k, v * v)
