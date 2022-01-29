'''
Level: Easy   Tag:[Array]

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


"../../../Material/PascalTriangleAnimated2.gif"

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33


Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?


'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        for i in range(rowIndex+1):
            row = [None for _ in range(i+1)]
            row[0] = 1
            row[-1] = 1

            for j in range(1, len(row)-1):
                row[j] = ans[i-1][j-1] + ans[i-1][j]

            ans.append(row)

        print(ans[-1])
        return ans[-1]


rowIndex = 3
Solution().getRow(rowIndex)