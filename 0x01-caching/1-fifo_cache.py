#!/usr/bin/python3
"""basic cache system that stores data in a dict"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """cache class that inherits from base caching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """must assign to dictionary """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data.keys()))
                self.cache_data.pop(first_key)
                print(f"Discard: {first_key}")
            return

    def get(self, key):
        """return the value in dict linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
