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

        data = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(data) or end_index > len(data):  # Noqa
            return []

        return self.__dataset[start_index:end_index]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """function that takes page and page size and returns a 
            dictionary
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        start, end = index_range(page, page_size)

        # estimate the next page
        if (page < total_pages):
            next_page = page + 1
        else:
            next_page = None

        # estimate prev page
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        return {
            'page_size' : len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }