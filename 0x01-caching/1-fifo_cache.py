
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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("Discard: {}".format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        """return the value in dict linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
