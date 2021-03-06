
'''

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

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
        return largest
