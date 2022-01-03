'''

Given an unsorted array nums,
reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
Please sort the array in place and do not define additional arrays.


For example,
given nums = [3, 5, 2, 1, 6, 4],
one possible answer is [1, 6, 2, 5, 3, 4].

Example 2:

Input: [1, 2, 3, 4]
Output: [1, 4, 2, 3]

'''



class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in xrange(0, len(nums)):
            if i % 2 == 0:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums




a = [3, 5, 2, 1, 6, 4]
print(Solution().wiggleSort(a))