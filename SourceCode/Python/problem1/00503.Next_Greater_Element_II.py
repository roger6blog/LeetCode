'''

Given a circular array (the next element of the last element is the first element of the array),

print the Next Greater Number for every element.

The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,

which means you could search circularly to find its next greater number.

If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.


'''


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        ans = [-1] * length
        # nums = nums + nums
        stack = []
        for i in xrange(length * 2):
            num = nums[i % length]
            while len(stack) > 0 and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            if i < length:
                stack.append(i)

        return ans

    def nextGreaterElementsTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in xrange(len(nums)):
            bFound = False
            newArr = nums[i:] + nums[:i]
            for j in xrange(len(newArr)):
                if nums[i] < newArr[j]:
                    bFound = True
                    ans.append(newArr[j])
                    break
            if not bFound:
                ans.append(-1)

        return ans







nums =[1,2,1]
nums1 = [1,2,3,4,3]
print Solution().nextGreaterElements(nums1)