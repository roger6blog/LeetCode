'''
Level: Easy  Tag: [Array]

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


"../../../Material/PascalTriangleAnimated2.gif"

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30


'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        pascal = []
        for i in range(numRows):
            row = [None for _ in range(i+1)]
            # The first and last row elements are always 1.
            row[0] = 1
            row[-1] = 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left + above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = pascal[i-1][j-1] + pascal[i-1][j]
            pascal.append(row)

        print(pascal)
        return pascal


num = 5
print(Solution().generate(num))
Solution().generate(30)