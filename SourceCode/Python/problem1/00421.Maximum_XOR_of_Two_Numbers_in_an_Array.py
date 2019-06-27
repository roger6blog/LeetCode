'''

Given a non-empty array of numbers,

a0, a1, a2, ... , an-1, where 0 <= ai < 231.

Find the maximum result of ai XOR aj, where 0 <= i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

'''

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 0
        ans = 0
        for x in xrange(31, -1, -1):
            prefixSet = set()
            mask |= 1 << x
            temp = ans | 1 << x
            for num in nums:
                prefixSet.add(num & mask)
            for item in prefixSet:
                # item ^ temp = X, it means X ^ item is MAX ans
                # (current highest bit)
                if item ^ temp in prefixSet:
                    ans = temp
                    break
        return ans



nums = [3, 10, 5, 25, 2, 8]
nums2 = [4,6,7]
print Solution().findMaximumXOR(nums2)