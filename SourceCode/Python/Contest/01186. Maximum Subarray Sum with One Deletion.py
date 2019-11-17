'''

5182->1186. Maximum Subarray Sum with One Deletion
Difficulty: Medium
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.



Example 1:

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
Example 2:

Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
Example 3:

Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.


Constraints:

1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4

'''

class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mi_n = 99999999999
        ma_n = -99999999999
        ne_count = 0
        subset = 0
        ma_subset = 0
        for i, num, in enumerate(arr):
            if num < 0:
                ne_count += 1
            if num > ma_n:
                ma_n = num
            if num < mi_n:
                mi_n = num

            if num >= 0:
                subset += num
            else:
                ma_subset = max(ma_subset, subset)
                subset = 0

        if sum(arr) < 0:
            if ma_subset == 0:
                return ma_n
            else:
                return max(ma_subset, ma_n)

        if ne_count >= 1:
            del arr[arr.index(mi_n)]
        ans = max(ma_n, sum(arr), ma_subset)
        return ans


arr = [-1, -1, -1, -1]
# arr = [1,-2,-2,3]
# arr = [2,1,-2,-5,-2]
print(Solution().maximumSum(arr))