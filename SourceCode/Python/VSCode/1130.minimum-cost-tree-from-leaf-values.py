#
# @lc app=leetcode id=1130 lang=python
#
# [1130] Minimum Cost Tree From Leaf Values
#
import sys
class Solution(object):
    def mctFromLeafValues_TLE(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        def dfs(arr, b, e):

            mi = sys.maxint
            ma = -1
            if b == e:
                return 0, arr[b]

            for i in range(b, e):
                left_mi, left_ma = dfs(arr, b, i)
                right_mi, right_ma = dfs(arr, i+1, e)

                if mi > left_ma * right_ma + left_mi + right_mi:
                    mi = left_ma * right_ma + left_mi + right_mi
                    ma = max(left_ma, right_ma)

            return mi, ma

        n = len(arr)

        return dfs(arr, 0, len(arr)-1)[0]  

    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        

        def dfs(arr, b, e, dp_table):

            mi = sys.maxint
            ma = -1
            if b == e:
                return 0, arr[b]

            if dp_table[b][e] != -1:
                return dp_table[b][e]

            for i in range(b, e):
                left_mi, left_ma = dfs(arr, b, i, dp_table)
                right_mi, right_ma = dfs(arr, i+1, e, dp_table)

                if mi > left_ma * right_ma + left_mi + right_mi:
                    mi = left_ma * right_ma + left_mi + right_mi
                    ma = max(left_ma, right_ma)

                    dp_table[b][e] = [mi, ma]
            return mi, ma

        n = len(arr)
        dp_table = [[-1 for j in range(n)] for i in range(n)]
        return dfs(arr, 0, len(arr)-1, dp_table)[0]

#print Solution().mctFromLeafValues([10,14,7,10,6,14,4,14,4,4,4,15,7,4,9])

[6,2,4]