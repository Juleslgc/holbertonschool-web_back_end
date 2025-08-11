#!/usr/bin/env python
"""
Simple pagination for a CSV dataset of popular first names.
"""
import csv
import math
from typing import List, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a page of data along with hypermedia metadata.

        Args:
        page (int): Page number to retrieve (default 1).
        page_size (int): Number of elements per page (default 10).

        Returns:
        Dict[str, Any]: Dictionary containing:
        - page_size (int): Actual size of the returned page,
        - page (int): Current page number,
        - data (List[List]): The page data,
        - next_page (int | None): Next page number or None,
        - prev_page (int | None): Previous page number or None,
        - total_pages (int): Total number of available pages.
        """
        data: List[List] = self.get_page(page, page_size)
        total_pages: int = math.ceil(len(self.dataset()) / page_size)
        next_page: int | None = page + 1 if page < total_pages else None
        prev_page: int | None = page - 1 if page > 1 else None

        return {'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages}
