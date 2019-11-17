'''
5191->1191. K-Concatenation Maximum Sum
Difficulty: Medium
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array.

Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.



Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0


Constraints:

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4

'''

from sys import maxint

class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        max_so_far = -maxint - 1
        max_ending_here = 0
        a = []
        for _ in range(k):
            a.extend(arr)

        size = len(a)
        max_so_far = -maxsize - 1
        max_ending_here = 0
        start = 0
        end = 0
        s = 0

        for i in range(0,size):

            max_ending_here += a[i]

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                start = s
                end = i

            if max_ending_here < 0:
                max_ending_here = 0
                s = i+1
        return max_so_far


arr = [1,-2,1]
k = 5
print(Solution().kConcatenationMaxSum(arr, k))