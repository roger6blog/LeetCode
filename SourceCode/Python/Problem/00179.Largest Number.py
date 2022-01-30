'''
Level: Medium   Tag: [String]

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 10^9
'''


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        comp = lambda a, b: 1 if a+b > b+a else -1
        num_to_str = map(str,nums)
        num_to_str.sort(cmp=comp, reverse=True)
        largest = ''
        for i in xrange(len(num_to_str)):
            largest = ''.join([largest, num_to_str[i]])
        if largest[0] == "0":
            return "0"
        print(largest)
        return largest





    def largestNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 注意要先轉成string再比較  不然用數字比 30會大於3
        def cmp(a, b):
            if a+b > b+a:
                return 1
            else:
                return -1
        ans = []
        for n in nums:
            ans.append(str(n))
        ans.sort(reverse=True, cmp=cmp)


        ans = "".join(ans)
        if ans[0] == "0":
            return "0"

        print(ans)
        return ans


nums = [3,30,34,5,9]
Solution().largestNumber(nums)
Solution().largestNumber2(nums)
