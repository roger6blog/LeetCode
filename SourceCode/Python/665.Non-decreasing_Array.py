'''

Given an array with n integers,

your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000].

'''
import unittest

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in xrange(len(nums)):
            if i >= 1 and nums[i] < nums[i-1]:
                if count >= 1:
                    return False
                count += 1
                if i > 1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1]

        return True



class TestcheckPossibility(unittest.TestCase):

    def setUp(self):
        pass

    def test_positive_input(self):
        nums = [4,2,3]
        self.assertTrue(Solution().checkPossibility(nums))
        nums = [2, 3, 3, 2, 4]
        self.assertTrue(Solution().checkPossibility(nums))
        nums = [-1,4,2,3]
        self.assertTrue(Solution().checkPossibility(nums))

    def test_false_input(self):
        nums = [3, 4, 2, 3]
        self.assertFalse(Solution().checkPossibility(nums))


# nums = [4,2,3]
# nums = [3,4,2,3]
# print Solution().checkPossibility(nums)

unittest.main()