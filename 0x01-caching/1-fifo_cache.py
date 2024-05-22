#!/usr/bin/python3
"""
basic FIFO caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    class for creating a FIFO caching system.
    """
    def __init__(self):
        """
        initializer
        """
        super().__init__()

    def put(self, key, item):
        """
        inserts an item to cache_data following the rule of FIFO.
        """
        if not key or not item:
            return

        if (len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS
                and not self.cache_data.get(key)):
            key_to_delete = next(iter(self.cache_data))
            print(f"DISCARD: {key_to_delete}")
            del self.cache_data[key_to_delete]

        self.cache_data[key] = item

    def get(self, key):
        """
        gets a value associated with the key.
        """
        return self.cached_data.get(key)
