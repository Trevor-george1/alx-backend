#!/usr/bin/env python3
"""Create a class MRUCache that inherits from BaseCaching and is a caching system:"""  # Noqa


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """summary"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """store the item in dict storage"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(-2)
                del self.cache_data[discard]
                print(f"Discard: {discard}")

    def get(self, key):
        """summary"""
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
