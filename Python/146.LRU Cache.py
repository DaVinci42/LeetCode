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


class DoubleLinkedNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = -1
        if key in self.dic:
            node = self.dic[key]
            value = node.val
            self._remove_node(node)
            self._add_node(node)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self._remove_node(node)
            self._add_node(node)
        else:
            if len(self.dic) == self.capacity:
                del self.dic[self.head.key]
                self._remove_node(self.head)
            node = DoubleLinkedNode(key, value)
            self.dic[key] = node
            self._add_node(node)

    def _remove_node(self, node):
        if node.pre is not None and node.next is not None:
            node.pre.next = node.next
            node.next.pre = node.pre
        else:
            if node is self.head:
                self.head = node.next
                if self.head is not None:
                    self.head.pre = None
            if node is self.tail:
                self.tail = node.pre
                if self.tail is not None:
                    self.tail.next = None

    def _add_node(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            self.head.pre = None
            self.tail.next = None
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
            self.tail.next = None

    def _print_self(self):
        for i in self.dic:
            print("dict: ", i, self.dic[i].val)
        node = self.head
        while node is not None:
            print("order: ", node.val)
            node = node.next
        node = self.tail
        while node is not None:
            print("reverse: ", node.val)
            node = node.pre
