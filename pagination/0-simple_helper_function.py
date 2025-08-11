#!/usr/bin/env python3
"""
Utility function to calculate the index range of a page.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end indices for a given page.

    Args:
    page (int): Page number (starts at 1).
    page_size (int): Number of elements per page.

    Returns:
    tuple: (start, end)
    """
    start: int = (page - 1) * page_size
    end: int = page_size * page
    return (start, end)
