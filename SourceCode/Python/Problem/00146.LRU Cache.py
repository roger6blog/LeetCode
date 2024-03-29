
'''
Level: Medium  Tag: [Design]

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2, cache is {1=1, 3=3}
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1  cache is {4=4, 3=3}
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Constraints:

1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put
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
            #self.lstRecent.insert(0, self.lstRecent.pop(self.lstRecent.index(key)))
            self.lstRecent.remove(key)
            self.lstRecent.append(key)
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
            #self.lstRecent.insert(0, self.lstRecent.pop(self.lstRecent.index(key)))
            self.lstRecent.remove(key)
            self.lstRecent.append(key)
        else:
            if len(self.lstRecent) == self.capcity:
                removeKey = self.lstRecent[0]
                self.dicCache.pop(removeKey, None)
                self.lstRecent = self.lstRecent[1:]

            self.dicCache[key] = value
            self.lstRecent.append(key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
cache = LRUCache(2)
cache.get(2)
cache.put(2, 6)
print cache.get(1)
cache.put(1, 5)
cache.put(1, 2)
print cache.get(1)
print cache.get(2)

'''
cache = LRUCache(2)
cache.get(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

print("!!!!!!!!!")






from collections import OrderedDict
class LRUCache2(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.lru = OrderedDict()
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lru:
            return -1
        value = self.lru.pop(key)
        self.lru[key] = value
        return value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.lru:
            self.lru.pop(key)

        elif len(self.lru) == self.capacity:
            ## last = True时pop规则为FILO, last = False时pop规则为FIFO
            self.lru.popitem(last=False)

        self.lru[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# cache = LRUCache2(2)
# cache.get(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))
# cache.put(3, 3)
# print(cache.get(2))
# cache.put(4, 4)
# print(cache.get(1))
# print(cache.get(3))
# print(cache.get(4))

# print("!!!!!!")
# # ["LRUCache","put","get","put","get","get"]
# # [[1],[2,1],[2],[3,2],[2],[3]]

cache2 = LRUCache2(1)
cache2.put(2,1)
assert 1 == cache2.get(2)
cache2.put(3,2)
assert -1 == cache2.get(2)
assert 2 == cache2.get(3)

# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

cache3 = LRUCache2(2)
cache3.put(2, 1)
cache3.put(2, 2)
cache3.get(2)
cache3.put(1, 1)
cache3.put(4, 1)
cache3.get(2)
