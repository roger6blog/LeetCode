
'''

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

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


'''


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lstRecent = []
        self.dicCache = {}
        self.capcity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key:
            return -1

        if key not in self.dicCache:
            return -1
        else:
            self.lstRecent.insert(0, self.lstRecent.pop(self.lstRecent.index(key)))
            return self.dicCache[key]



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dicCache:
            # just renew the value
            self.dicCache[key] = value
            self.lstRecent.insert(0, self.lstRecent.pop(self.lstRecent.index(key)))
        if len(self.lstRecent) == self.capcity:
            removeKey = self.lstRecent.pop()
            self.dicCache.pop(removeKey, None)

        self.dicCache[key] = value
        self.lstRecent.insert(0, key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LRUCache(2)
cache.get(2)
cache.put(2, 6)
print cache.get(1)
cache.put(1, 5)
cache.put(1, 2)
print cache.get(1)
print cache.get(2)













