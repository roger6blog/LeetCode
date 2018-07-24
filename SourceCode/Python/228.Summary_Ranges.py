'''

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.


Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


'''


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        length = len(nums)
        ans = []
        i = 0
        while  i < length:
            j = i
            res = str(nums[i])
            while i + 1 < length and nums[i+1] - nums[i] == 1:
                i += 1
            if i > j:
                res += "->" + str(nums[i])
            ans.append(res)
            i += 1
        return ans







Input= [0,2,3,4,6,8,9]
s = [0,1,2,4,5,7]
print Solution().summaryRanges(Input)