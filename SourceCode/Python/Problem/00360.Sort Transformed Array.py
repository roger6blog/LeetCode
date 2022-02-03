'''
Level: Medium  Tag: [Math]

Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form
f(x)=ax^2+bx+c  to each element  x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)


Example1

Input: nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5
Output: [3, 9, 15, 33]

Example2

Input: nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
Output: [-23, -5, 1, 7]


'''

class Solution:
    """
    @param nums: a sorted array
    @param a:
    @param b:
    @param c:
    @return: a sorted array
    """
    def sortTransformedArray(self, nums, a, b, c):
        # Write your code here
        n = len(nums)
        for x in range(n):
            nums[x] = a*(nums[x] **2) + b*nums[x] + c

        nums.sort()

        print(nums)

        return nums

    '''
    这道题用到了大量的高中所学的关于抛物线的数学知识，我们知道，对于一个方程f(x) = ax2 + bx + c 来说，如果a>0，则抛物线开口朝上，那么两端的值比中间的大，
    而如果a<0，则抛物线开口朝下，则两端的值比中间的小。而当a=0时，则为直线方法，是单调递增或递减的。
    那么我们可以利用这个性质来解题，题目中说明了给定数组nums是有序的，如果不是有序的，我想很难有O(n)的解法。正因为输入数组是有序的，我们可以根据a来分情况讨论：

    当a>0，说明两端的值比中间的值大，那么此时我们从结果res后往前填数，用两个指针分别指向nums数组的开头和结尾，指向的两个数就是抛物线两端的数，将它们之中较大的数先存入res的末尾，
    然后指针向中间移，重复比较过程，直到把res都填满。

    当a<0，说明两端的值比中间的小，那么我们从res的前面往后填，用两个指针分别指向nums数组的开头和结尾，指向的两个数就是抛物线两端的数，
    将它们之中较小的数先存入res的开头，然后指针向中间移，重复比较过程，直到把res都填满。

    当a=0，函数是单调递增或递减的，那么从前往后填和从后往前填都可以，我们可以将这种情况和a>0合并。
    '''

    def sortTransformedArray_O_n(self, nums, a, b, c):

        def quadratic(x, a, b, c):
            return a*(x **2) + b*x + c

        n = len(nums)
        ans = [0] * n
        i = 0
        j = n - 1

        # a 大於0時開口朝上  說明兩端的值比中間大，所以我們由後往前填
        if a >= 0:
            index = n-1
        else:
            index = 0

        while i <= j:
            if a >= 0 :
                if quadratic(nums[i], a, b, c) >= quadratic(nums[j], a, b, c):
                    ans[index] = quadratic(nums[i], a, b, c)
                    i += 1
                else:
                    ans[index] = quadratic(nums[j], a, b, c)
                    j -= 1
                index -= 1
            else:
                if quadratic(nums[i], a, b, c) >= quadratic(nums[j], a, b, c):
                    ans[index] = quadratic(nums[j], a, b, c)
                    j -= 1
                else:
                    ans[index] = quadratic(nums[i], a, b, c)
                    i += 1
                index += 1

        print(ans)

        return ans






nums = [-4, -2, 2, 4]
a = 1
b = 3
c = 5
Solution().sortTransformedArray(nums, a, b, c)
nums = [-4, -2, 2, 4]
a = 1
b = 3
c = 5
Solution().sortTransformedArray_O_n(nums, a, b, c)

nums = [-4, -2, 2, 4]
a = -1
b = 3
c = 5
Solution().sortTransformedArray(nums, a, b, c)