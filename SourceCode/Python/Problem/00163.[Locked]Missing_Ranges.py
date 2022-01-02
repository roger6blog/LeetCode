'''
Level: Easy
Time:  O(n)
Space: O(1)

Given a sorted integer array where the range of elements are [lower, upper] inclusive,
return its missing ranges.

Example 1
Input:
nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
Output:
["2", "4->49", "51->74", "76->99"]
Explanation:
in range[0,99],the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]

Example 2
Input:
nums = [0, 1, 2, 3, 7], lower = 0 and upper = 7
Output:
["4->6"]
Explanation:
in range[0,7],the missing range include range[4,6]
'''


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def getMissingRange(lower, upper):
            if lower == upper:
                return "{}".format(lower)
            else:
                return "{}->{}".format(lower, upper)

        ans = []
        pre = lower - 1


        for i in range(len(nums)+1):
            if i == len(nums):
                curr = upper + 1
            else:
                curr = nums[i]
            if curr - pre >= 2:
                # it must be a missing range in pre element and curr element
                ans.append(getMissingRange(pre+1, curr-1))

            pre = curr

        return ans


    def findMissingRanges2(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        nums.append(lower)
        nums.append(upper)
        nums = list(set(nums))
        nums.sort()
        tmp = []

        for n in range(1, len(nums)):

            if nums[n] - nums[n-1] != 1:
                if nums[n] == nums[-1]:
                    tmp.append([nums[n-1]+1, nums[n]])
                else:
                    tmp.append([nums[n-1]+1, nums[n]-1])

        ans = []
        for x, y in tmp:
            if x == y:
                ans.append("{}".format(x))
            else:
                ans.append("{}->{}".format(x, y))

        print(ans)
        return ans


assert ["2", "4->49", "51->74", "76->99"] == Solution().findMissingRanges2([0, 1, 3, 50, 75], 0, 99)