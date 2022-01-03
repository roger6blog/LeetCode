'''
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative.

The first difference (if one exists) may be either positive or negative.

A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences.
The first is not because its first two differences are positive, and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.



Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

Example 2:

Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).

Example 3:

Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000


Follow up: Could you solve this in O(n) time?

'''

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        wiggle_len_ascend = 1

        ascend = True

        for i in range(len(nums)-1):
            if ascend == True and nums[i+1] > nums[i]:
                wiggle_len_ascend += 1
                ascend = False

            elif ascend == False and nums[i+1] < nums[i]:
                wiggle_len_ascend += 1
                ascend = True

        wiggle_len_descend = 1
        ascend = False
        for i in range(len(nums)-1):
            if ascend == True and nums[i+1] > nums[i]:
                wiggle_len_descend += 1
                ascend = False

            elif ascend == False and nums[i+1] < nums[i]:
                wiggle_len_descend += 1
                ascend = True

        wiggle_len = max(wiggle_len_ascend, wiggle_len_descend)
        print(wiggle_len)
        return wiggle_len

nums = [1,7,4,9,2,5]
assert 6 == Solution().wiggleMaxLength(nums)

nums = [1,17,5,10,13,15,10,5,16,8]
assert 7 == Solution().wiggleMaxLength(nums)

nums = [1,2,3,4,5,6,7,8,9]
assert 2 == Solution().wiggleMaxLength(nums)

nums = [3,3,3,2,5]
assert 3 == Solution().wiggleMaxLength(nums)