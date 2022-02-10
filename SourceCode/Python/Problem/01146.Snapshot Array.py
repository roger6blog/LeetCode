'''
Level: Medium

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.
    Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id:
    the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index,
    at the time we took the snapshot with the given snap_id


Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5


Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9

'''



'''

用snap_id记录当前snap的版本号, 每次set操作的时候, 把(snap_id,index)当做key存入字典中
get操作的时候, 把当前(snap_id,index)当做key在字典中查找,
如果key存在则返回对应的值, 如果不存在就把snap_id减去1继续查找,直到找到值或者snap_id为0为止。

'''

class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.length = length
        self.dic = {}


    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if 0 <= index < self.length:
            self.dic[(index, self.snap_id)] = val


    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1


    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        while snap_id >= 0:
            if (index, snap_id) in self.dic:
                return self.dic[(index, snap_id)]
            else:
                snap_id -= 1
        return 0



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

length = 3
obj = SnapshotArray(length)
obj.set(0,5)
assert 0 == obj.snap()
obj.set(0,6)
assert 5 == obj.get(0,0)


# ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"]
# [[1],[0,15],[],[],[],[0,2],[],[],[0,0]]
# [null,null,0,1,2,15,3,4,15]