#!/usr/bin/python3
"""
basic LFU caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    class for creating a LFU caching system.
    """
    def __init__(self):
        """
        initializer
        """
        super().__init__()
        self.__lfu_table = {}

    def put(self, key, item):
        """
        inserts an item to cache_data following the rule of LFU.
        """
        if not key or not item:
            return

        if (len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS
                and not self.cache_data.get(key)):

            key_to_delete = None
            for k, value in self.__lfu_table.items():
                if key_to_delete is None:
                    key_to_delete = (k, value)
                else:
                    if value < key_to_delete[1]:
                        key_to_delete = (k, value)
            print(f"DISCARD: {key_to_delete[0]}")
            del self.cache_data[key_to_delete[0]]
            del self.__lfu_table[key_to_delete[0]]
        prev_value = 0
        if self.cache_data.get(key):
            prev_value = self.__lfu_table[key]
            del self.cache_data[key]
            del self.__lfu_table[key]
        if key in self.__lfu_table.keys():
            del self.__lfu_table[key]
        self.__lfu_table[key] = prev_value + 1
        self.cache_data[key] = item

    def get(self, key):
        """
        gets a value associated with the key.
        """
        if key not in self.cache_data.keys():
            return None
        if key in self.__lfu_table.keys():
            prev_value = self.__lfu_table[key]
            del self.__lfu_table[key]
            self.__lfu_table[key] = prev_value + 1
        return self.cache_data.get(key, None)
