'''
Level: Medium  Tag: [Array]

Given an integer array nums and two integers k and t,

return true if there are two distinct indices i and j in the array such that
    abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false


Constraints:

1 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^4
0 <= t <= 2^31 - 1

'''
import bisect

class Solution(object):
    def containsNearbyAlmostDuplicate_TLE(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        hash_map = {}
        for i, n in enumerate(nums):
            for d in range(t+1):
                if n-d in hash_map and i - hash_map[abs(n-d)] <= k:
                    return True
                elif n+d in hash_map and i - hash_map[n+d] <= k:
                    return True
            hash_map[n] = i

        return False





    '''
    利用 桶排序，进一步降低时间复杂度, 牺牲一些空间复杂度
    思维开拓一点，桶排序未必需要开一个数组，利用一个hashmap一样可以实现桶排序，尤其是在类似数据很稀疏的时候
    因为 两个数的差不能超过t，所以把间隔设置为t + 1， 从而避免K为0的时候，查找哪个桶的时候除数为0的情况。
    然后将每个数字除以t + 1， 从而实现把数组中每个数字分配到对应的桶中。
    如果同一个桶中，已经有数字了，则比较两个数字的值是否小于t，同时还需要比较左右相邻的桶中是否存在元素，
    因为要求的解有机会落在相邻的两个桶中
    当前数组index >= k的时候，可以开始删除不需要的桶元素，从而保证空间不会太大 有种 slide window的意思
    时间复杂度O(N)
    空间复杂度O(k)

    '''

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        if k == 0:
            return False

        bucket = {}
        for i, n in enumerate(nums):
            bucket_no = n // (t+1)  # 避免t為0時除以0
            offset = 1

            for index in range(bucket_no-offset, bucket_no+offset+1):
                if index in bucket and abs(bucket[index] - nums[i]) <= t:
                    return True

            bucket[bucket_no] = nums[i]

            if len(bucket) > k:
                del bucket[nums[i-k]//(t+1)]  # 避免t為0時除以0

        return False


nums = [1,2,3,1]
k = 3
t = 0
assert True == Solution().containsNearbyAlmostDuplicate(nums, k, t)

nums = [1,5,9,1,5,9]
k = 2
t = 3
assert False == Solution().containsNearbyAlmostDuplicate(nums, k, t)

nums = [8,7,15,1,6,1,9,15]
k = 1
t = 3
assert True == Solution().containsNearbyAlmostDuplicate(nums, k, t)

nums = [-2147483640,-2147483641]
k = 1
t = 100
assert True == Solution().containsNearbyAlmostDuplicate(nums, k, t)