#!/usr/bin/env python3
"""
It contains the function:
element_lenght()
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that return a list of tuple

    Arg:
        lst: An iterable of sequence

    Return:
        A list of tuple of sequence
    """
    return [(i, len(i)) for i in lst]
