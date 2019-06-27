'''

Given an unsorted array nums,
reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].


Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?


'''


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        new = sorted(nums)
        mid = ( len(new) + 1 ) / 2
        small = new[:mid]
        large = new[mid:]

        for i in xrange(len(new)):
            if i % 2 == 0:
                if small:
                    nums[i] = small.pop()
            else:
                if large:
                    nums[i] = large.pop()



b = [1, 3, 2, 2, 3, 1]
a = [1, 5, 1, 1, 6, 4]
c = [5,3,1,2,6,7,8,5,5]
Solution().wiggleSort(c)
print c