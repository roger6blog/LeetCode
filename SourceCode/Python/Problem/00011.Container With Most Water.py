'''
Level: Medium Tags:[]

You are given an integer array height of length n.

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,

such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:
"../../../question_11.jpg"

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 104

'''

class Solution(object):
    def maxArea_TLE(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            return min(height[1], height[0])

        max_area = 0
        for i in range(len(height)):
            for j in range(1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * abs(j-i))
        return max_area


    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) == 2:
            return min(height[1], height[0])

        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * abs(right-left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


height = [1,8,6,2,5,4,8,3,7]
assert 49 == Solution().maxArea(height)
height = [1, 3, 2]
assert 2 == Solution().maxArea(height)

height = [1, 3, 2, 2]
assert 4 == Solution().maxArea(height)