'''
Level: Easy     Tag: [Design], [Prefix Sum]

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


Constraints:

1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= left <= right < nums.length
At most 10^4 calls will be made to sumRange.


'''


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(self.nums[left:right+1])



class NumArray_prefix_sum(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i-1]


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix_sum[right+1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
assert 1 == obj.sumRange(0, 2)
assert -1 == obj.sumRange(2, 5)
assert -3 == obj.sumRange(0, 5)