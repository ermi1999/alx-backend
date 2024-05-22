#!/usr/bin/python3
"""
basic MRU caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    class for creating a MRU caching system.
    """
    def __init__(self):
        """
        initializer
        """
        super().__init__()
        self.__lru_table = {}

    def put(self, key, item):
        """
        inserts an item to cache_data following the rule of MRU.
        """
        if not key or not item:
            return

        if (len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS
                and not self.cache_data.get(key)):
            key_to_delete, _ = self.__lru_table.popitem()
            print(f"DISCARD: {key_to_delete}")
            del self.cache_data[key_to_delete]
        if self.cache_data.get(key):
            del self.cache_data[key]
        if key in self.__lru_table.keys():
            del self.__lru_table[key]
        if len(self.__lru_table) > 1:
            self.__lru_table[key] = len(self.__lru_table) - 1
        else:
            self.__lru_table[key] = 0
        self.cache_data[key] = item

    def get(self, key):
        """
        gets a value associated with the key.
        """
        if key not in self.cache_data.keys():
            return None
        if key in self.__lru_table.keys():
            del self.__lru_table[key]
        if len(self.__lru_table) > 1:
            self.__lru_table[key] = len(self.__lru_table) - 1
        else:
            self.__lru_table[key] = 0
        return self.cache_data.get(key, None)
