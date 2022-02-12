'''
Level: Hard
Given n non-negative integers representing an elevation map where the width of each bar is 1
compute how much water it is able to trap after raining.


"../../../Material/rainwatertrap.png"

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Thanks Marcos for contributing this image!

'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        n = len(height)
        left = 0
        right = len(height) -1
        water = 0
        minHeight = 0
        while left < right:
            while left < right and height[left] <= minHeight:
                water += minHeight - height[left]
                left += 1
            while left < right and height[right] <= minHeight:
                water += minHeight - height[right]
                right -= 1
            minHeight = min(height[left], height[right])
        return water

q = [0,1,0,2,1,0,1,3,2,1,2,1]

sol = Solution()
ans = sol.trap(q)
print ans
