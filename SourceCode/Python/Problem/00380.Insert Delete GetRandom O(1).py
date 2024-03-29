'''
Level: Medium   Tag: [Random]

Design a data structure that supports all following operations in average O(1) time.

RandomizedSet() Initializes the RandomizedSet object.
insert(val): Inserts an item val to the set if not already present.
    Returns true if the item was not present, false otherwise.
remove(val): Removes an item val from the set if present.
    Returns true if the item was present, false otherwise.
getRandom: Returns a random element from current set of elements.
Each element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();


'''

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = {}
        self.data = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hashMap:
            return False
        self.hashMap[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hashMap:
            return False
        del self.data[self.data.index(val)]
        self.hashMap.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """

        return random.choice(self.data)




class RandomizedSet2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hash_map:
            return False

        self.hash_map[val] = None
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hash_map:
            return False

        self.hash_map.pop(val)
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        rand = random.randrange(len(self.hash_map))
        return self.hash_map.keys()[rand]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
["RandomizedSet","insert","insert","remove","insert","insert","insert","remove","remove","insert","remove","insert","insert","insert","insert","insert","getRandom","insert","remove","insert","insert"]
[[],                [3],     [-2],    [2],     [1],     [-3],   [-2],     [-2],    [3],     [-1],    [-3],     [1],    [-2],    [-2],    [-2],    [1],      [],        [-2],    [0],    [-3],     [1]]
'''
obj = RandomizedSet()
obj.insert(3)
obj.insert(-2)
obj.remove(2)
obj.insert(1)
obj.insert(-3)
obj.insert(-2)
obj.remove(-2)
obj.remove(3)
obj.insert(-1)
obj.remove(-3)
# obj.insert(1)