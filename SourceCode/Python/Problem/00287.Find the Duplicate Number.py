'''

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


'''

class Solution(object):
    def findDuplicate_not_meet_space_limit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate_num = {}
        for i in nums:
            if i not in duplicate_num:
                duplicate_num[i] = 0
            else:
                return i


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        We use fast/slow ptr method in checking cycle of LinkList
        Set two ptrs, slow one move 1 step, fast one 2 steps
        They must meet during traversal
        Then we set one of ptr to 0 to restart moving from start poing(usually fast ptr)
        If this pty whcich restart moving from start point still be able to reach other pts
        It means there is a cycle in LinkList, there is a duplicate number in list as welll

        Limittion:
        Integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
        1 <= n <= 105
        nums.length == n + 1
        1 <= nums[i] <= n
        '''

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


nums = [1,3,4,2,2]
assert 2 == Solution().findDuplicate(nums)
