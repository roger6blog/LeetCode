'''

1243. Array Transformation
Easy

Given an initial array arr, every day you produce a new array using the array of the previous day.

On the i-th day,
you do the following operations on the array of day i-1 to produce the array of day i:

If an element is smaller than both its left neighbor and its right neighbor,
then this element is incremented.

If an element is bigger than both its left neighbor and its right neighbor,
then this element is decremented.

The first and last elements never change.
After some days, the array does not change. Return that final array.



Example 1:

Input: arr = [6,2,3,4]
Output: [6,3,3,4]
Explanation:
On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
No more operations can be done to this array.
Example 2:

Input: arr = [1,6,3,4,3,5]
Output: [1,4,4,4,4,5]
Explanation:
On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
No more operations can be done to this array.


Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 100


'''

class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def transfer(a):
            res = [a[0]]
            for i in range(1, len(a)-1):
                if a[i] < a[i-1] and a[i] < a[i+1]:
                    res.append(a[i] + 1)
                elif a[i] > a[i-1] and a[i] > a[i+1]:
                    res.append(a[i] - 1)
                else:
                    res.append(a[i])
            res.append(a[-1])
            return res

        a = arr[:]
        while True:
            ans = transfer(a)
            if ans != a:
                a = ans
            else:
                return ans