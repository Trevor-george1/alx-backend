#!/usr/bin/env python3
"""server to paginate a database"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """function returns a tuple"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        """function that takes 2 integers args and gets page"""
        assert isinstance(page, int), "Page must be an integer"
        assert isinstance(page_size, int), "Page size must be an integer"
        assert page > 0, "Page must be greater than 0"
        assert page_size > 0, "Page size must be greater than 0"

        start_index, end_index = index_range(page, page_size)

        if self.__dataset is None:
            raise ValueError("dataset is not loaded")
        if start_index >= len(self.__dataset) or end_index > len(self.__dataset):  # Noqa
            return []

        return self.__dataset[start_index:end_index]
