
'''
Level: Medium

Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        numset = set(nums)

        for num in numset:
            if num-1 not in numset:
                num_curr = num
                longest_curr = 1

                while num_curr+1 in numset:
                    num_curr += 1
                    longest_curr += 1

                longest = max(longest, longest_curr)

        return longest

nums = [1,2,0,1]
assert 3 == Solution().longestConsecutive(nums)
nums = [0,3,7,2,5,8,4,6,0,1]
assert 9 == Solution().longestConsecutive(nums)