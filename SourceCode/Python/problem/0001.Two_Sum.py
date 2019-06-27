'''



'''




class Solution(object):
    @staticmethod
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return(dic[num], i)
            else:
                dic[target - num] = i

nums = [2, 7, 11, 15]
target = 9
print Solution.twoSum(None, nums, target)