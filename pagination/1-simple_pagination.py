#!/usr/bin/env python3
"""

"""

import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a portion (page) of the dataset.

        Args:
        page (int): Number of the page to retrieve (1 = first page).
        page_size (int): Number of elements per page.

        Returns:
        List[List]: The elements corresponding to the requested page.

        Raises:
        AssertionError: If `page` or `page_size` are not positive integers.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()
        start: int
        end: int
        start, end = index_range(page, page_size)
        return data[start:end]
