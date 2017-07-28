"""
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class LRUCache(object):

    capacity, k_v_dict, keys = 0, {}, []

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.k_v_dict = {}
        self.keys = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = 0
        if key in self.k_v_dict:
            value = self.k_v_dict[key]
            index = 0
            for i, k in enumerate(self.keys):
                if k == key:
                    index = i
                    break
            del self.keys[index]
            self.keys.append(key)
        else:
            value = -1
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.k_v_dict:
            index = 0
            for i, k in enumerate(self.keys):
                if key == k:
                    index = i
                    break
            del self.keys[index]
            self.keys.append(key)
            self.k_v_dict[key] = value
        else:
            self.k_v_dict[key] = value
            self.keys.append(key)
            length = len(self.keys)
            if length > self.capacity:
                del_keys = self.keys[:length - self.capacity]
                for k in del_keys:
                    if k in self.k_v_dict:
                        del self.k_v_dict[k]
                self.keys = self.keys[length - self.capacity:]
