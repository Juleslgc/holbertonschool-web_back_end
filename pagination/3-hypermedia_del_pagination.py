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
        page_size (int): Number of elements to include in the page (must be > 0).

        Returns:
        Dict[str, Any]: Dictionary containing:
        - index (int): Starting index.
        - data (List[Any]): The page data.
        - page_size (int): Actual size of the returned page.
        - next_index (int): Index to use for the next page.
        """
        assert isinstance(index, int) or index is None
        assert isinstance(page_size, int) and page_size > 0

        if index is None:
            index = 0

        data_list: List[Any] = self.dataset()
        assert 0 <= index < len(data_list)

        data: List[Any] = []
        next_index: int = index

        for i in range(index, len(data_list)):
            if data_list[i] is not None:
                data.append(data_list[i])
                if len(data) == page_size:
                    next_index = i + 1
                    break
        else:
            next_index = len(data_list)

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
