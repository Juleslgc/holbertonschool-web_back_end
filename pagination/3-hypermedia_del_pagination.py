#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None, page_size: int = 10
                        ) -> Dict[str, Any]:
        """
        Returns a data page with delete-resilient pagination.

        Args:
        index (Optional[int]): Starting position in the dataset (default is 0).
        Can be None to start at the beginning.
        page_size (int): Number of elements to include
        in the page (must be > 0).

        Returns:
        Dict[str, Any]: Dictionary containing:
        - index (int): Starting index.
        - data (List[Any]): The page data.
        - page_size (int): Actual size of the returned page.
        - next_index (int): Index to use for the next page.
        """
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        max_index = max(indexed_dataset.keys())
        assert index <= max_index

        data = []
        current = index
        while len(data) < page_size and current <= max_index:
            if current in indexed_dataset:
                data.append(indexed_dataset[current])
            current += 1

        # Skip deleted indices to find the next valid index
        while current <= max_index and current not in indexed_dataset:
            current += 1

        next_index = current if current <= max_index else None

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
