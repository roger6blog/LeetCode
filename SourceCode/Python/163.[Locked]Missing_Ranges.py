# Time:  O(n)
# Space: O(1)
#
# Given a sorted integer array where the range of elements are [lower, upper] inclusive,
# return its missing ranges.
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# return ["2", "4->49", "51->74", "76->99"].
#

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


        for i in xrange(len(nums)+1):
            if i == len(nums):
                curr = upper + 1
            else:
                curr = nums[i]
            if curr - pre >= 2:
                # it must be a missing range in pre element and curr element
                ans.append(getMissingRange(pre+1, curr-1))

            pre = curr

        return ans
if __name__ == "__main__":
    print Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99)