'''

5088->1228. Missing Number In Arithmetic Progression
Difficulty: Easy
In some array arr, the values were in arithmetic progression:

the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

Then, a value from arr was removed that was not the first or last value in the array.

Return the removed value.



Example 1:

Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].
Example 2:

Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].


Constraints:

3 <= arr.length <= 1000
0 <= arr[i] <= 10^5

'''

class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        dic_missing = {}
        ma = 0
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff not in dic_missing:
                dic_missing[diff] = i
                if len(dic_missing) > 1:
                    for k in dic_missing.iterkeys():
                        ma = max(ma, k)

        return arr[dic_missing[ma]] + ma/2



arr = [15,13,12]
print(Solution().missingNumber(arr))