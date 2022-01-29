'''
Level: Medium   Tag: [Array]

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.


Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]
Example 3:


Input: nums = [1,2]
Output: [1,2]


Constraints:

1 <= nums.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9


Follow up: Could you solve the problem in linear time and in O(1) space?


'''
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        c = Counter(nums)
        for k, v in c.items():
            if v > len(nums) // 3:
                ans.append(k)

        print(ans)

        return ans

nums = [3,2,3]
Solution().majorityElement(nums)
nums = [1,2]
Solution().majorityElement(nums)