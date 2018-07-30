'''

Given scores of N athletes,

find their relative ranks and the people with the top three highest scores,

who will be awarded medals:

"Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.

Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.


'''


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        Gold = "Gold Medal"
        Silver = "Silver Medal"
        Bronze = "Bronze Medal"
        rank = sorted(nums, reverse=True)
        count = 1
        for i in rank:
            if count == 1:
                nums[nums.index(i)] = Gold
            elif count == 2:
                nums[nums.index(i)] = Silver
            elif count == 3:
                nums[nums.index(i)] = Bronze
            else:
                nums[nums.index(i)] = str(count)
            count += 1
        return nums


nums = [5, 4, 3, 2, 1, 6]
print Solution().findRelativeRanks(nums)