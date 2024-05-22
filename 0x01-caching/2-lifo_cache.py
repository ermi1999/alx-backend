#!/usr/bin/python3
"""
basic LIFO caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class for creating a LIFO caching system.
    """
    def __init__(self):
        """
        initializer
        """
        super().__init__()

    def put(self, key, item):
        """
        inserts an item to cache_data following the rule of LIFO.
        """
        if not key or not item:
            return

        if (len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS
                and not self.cache_data.get(key)):
            key_to_delete, _ = self.cache_data.popitem()
            print(f"DISCARD: {key_to_delete}")
        if self.cache_data.get(key):
            del self.cache_data[key]
        self.cache_data[key] = item

    def get(self, key):
        """
        gets a value associated with the key.
        """
        return self.cache_data.get(key, None)
