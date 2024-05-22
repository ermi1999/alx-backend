#!/usr/bin/python3
"""
this module implements a basic caching mechanism.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    basic caching.
    """
    def put(self, key, item):
        """
        method for setting a value.
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        method for getting a value.
        """
        return self.cache_data.get(key)
