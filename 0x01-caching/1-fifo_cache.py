#!/usr/bin/env python3
"""FIFOcache system that uses FIFO rule to replace data stored"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """fifocache class inherits from base caching"""
    def __init__(self):
        """initialization, super()"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary"""
        if key is None or item is None:
            return
        else: 
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():  # Noqa
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("Discard: {}".format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        """return the value of key from dict"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
