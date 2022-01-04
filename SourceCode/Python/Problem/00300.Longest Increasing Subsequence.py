'''
Level: Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

 For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?



'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        max_sub = [nums[0]]

        for n in nums[1:]:
            if n > max_sub[-1]:
                max_sub.append(n)
            elif n < max_sub[-1]:
                i = bisect.bisect_left(max_sub, n)
                max_sub[i] = n

        print(len(max_sub))
        return len(max_sub)


nums = [10,9,2,5,3,7,101,18]
assert 4 == Solution().lengthOfLIS(nums)

nums = [7,7,7,7,7,7,7]
assert 1 == Solution().lengthOfLIS(nums)

nums = [4,10,4,3,8,9]
assert 3 == Solution().lengthOfLIS(nums)