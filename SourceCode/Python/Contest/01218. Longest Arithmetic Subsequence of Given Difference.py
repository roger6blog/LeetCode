'''

5214->1218. Longest Arithmetic Subsequence of Given Difference
Difficulty: Medium
Given an integer array arr and an integer difference,

return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.



Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].

Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.

Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].

'''

import copy
class Solution(object):
    def __init__(self):
        self.longest = 1
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = {}
        for i in xrange(len(arr)):
            for j in xrange(i + 1, len(arr)):
                if arr[j] - arr[i] == difference:
                    dp[j, arr[j] - arr[i]] = dp.get((i, arr[j] - arr[i]), 1) + 1
        if dp:
            return max(dp.values())
        else:
            return 1

arr = [1,3,5,7]
difference = 1

print(Solution().longestSubsequence(arr, difference))