#!/usr/bin/python3
"""basic cache system that stores data in a dict"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """cache class that inherits from base caching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """must assign to dictionary """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, last_value = self.cache_data.popitem()
                print("Discard: {}".format(last_key))
            self.cache_data[key] = item

    def get(self, key):
        """return the value in dict linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
