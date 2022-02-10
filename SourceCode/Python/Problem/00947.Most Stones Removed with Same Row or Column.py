'''
Leevl: Medium  Tag: [Union Find]

On a 2D plane, we place n stones at some integer coordinate points.
Each coordinate point may have at most one stone.

A stone can be removed if
it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone,
return the largest possible number of stones that can be removed.



Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.


Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 10^4
No two stones are at the same coordinate point.


'''

'''
1. for each point, union two indexes.
2. return points number - union number
'''

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        self.father = {}

        for a, b in stones:
            '''
            # 此處的b需要用別的數字顯示, 他只是一個終點, 用index來表示
            # 但是不能和題目的y重複, 不然[[0,1],[1,0]]這兩個座標會造成無法分組
            # 可以用b的1補數~b 或是直接b+10000(題目的yi上限)來做區隔
            https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/197668/Count-the-Number-of-Islands-O%28N%29
            '''
            # self.union(a, ~b)
            self.union(a, b+10000)

        # 算出被分成幾組
        group = set()
        for x in self.father:
            group.add(self.find(x))

        # 石頭數量扣掉能分成的組數就是最多能移除多少石頭
        return n - len(group)

    def find(self, x):
        if self.father[x] == x:
            return x

        while self.father[x] != x:
            x = self.father[x]

        return x

    def union(self, a, b):
        self.father.setdefault(a, a)
        self.father.setdefault(b, b)
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_a] = root_b


stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Solution().removeStones(stones)

stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Solution().removeStones(stones)