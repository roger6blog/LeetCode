'''

Given a binary array,

find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

'''


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        words = [str(x) for x in nums]
        s = ''.join(words)
        t = s.split("0")
        ans = 0
        for i in t:
            ans = max(ans, len(i))

        return ans

    def findMaxConsecutiveOnesFaster(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        count = 0
        for num in nums:
            if num == 0:
                result = max(result, count)
                count = 0
            else:
                count += 1
        result = max(result, count)
        return result

nums = [1,1,0,1,1,1]
print Solution().findMaxConsecutiveOnes(nums)