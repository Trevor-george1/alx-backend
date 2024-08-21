#!/usr/bin/python3
"""basic cache system that stores data in a dict"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """cache class that inherits from base caching"""
    def __init__(self):
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """must assign to dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print("Discard: {:s}".format(discard))

    def get(self, key):
        """return the value in dict linked to key"""
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        else:
            return None
