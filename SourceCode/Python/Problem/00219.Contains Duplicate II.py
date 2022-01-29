'''
Level: Easy  Tag: [Array]

Given an integer array nums and an integer k,

return true if there are two distinct indices i and j in the array such that
    nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5

'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}
        for i, n in enumerate(nums):
            if n in hash_map and i - hash_map[n] <= k:
                return True
            hash_map[n] = i
        return False


nums = [1,2,3,1,2,3]
k = 2
assert False == Solution().containsNearbyDuplicate(nums, k)

nums = [1,0,1,1]
k = 1
assert True == Solution().containsNearbyDuplicate(nums, k)

nums = [1,2,3,1]
k = 3
assert True == Solution().containsNearbyDuplicate(nums, k)