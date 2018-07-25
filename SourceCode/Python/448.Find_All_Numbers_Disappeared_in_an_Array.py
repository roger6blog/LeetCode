'''

Given an array of integers where 1 <= a[i] <= n (n = size of array),

some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime?

You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


'''

class Solution(object):
    def findDisappearedNumbers_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        ans = []
        nums.sort()
        for c, i in enumerate(nums):
            if i != c+1 and c+1 not in nums:
                ans.append(c+1)
        return ans

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            nums[abs(n)-1] = -abs(nums[abs(n)-1])

        for c, i in enumerate(nums):
            if i > 0:
                ans.append(c+1)

        return ans


nums = [4,3,2,7,8,2,3,1]
print Solution().findDisappearedNumbers(nums)