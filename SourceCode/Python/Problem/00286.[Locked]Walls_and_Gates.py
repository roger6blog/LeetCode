'''

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room.

We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate.

If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4


'''

import sys
class Solution():
    def wallsAndGates(self, rooms):
        """
        input: List[int][int]
        rtype: List[int][int]
        """
        if len(rooms) == 0:
            return rooms

        row = len(rooms)
        col = len(rooms[0])

        ans = [[0 for _ in xrange(col) ] for _ in xrange(row)]


        for x in xrange(row):
            for y in xrange(col):
                if rooms[x][y] == 'INF':
                    rooms[x][y] = sys.maxint

        for x in xrange(row):
            for y in xrange(col):
                if rooms[x][y] == sys.maxint:
                    ans[x][y] = self.dfs(rooms, x, y, ans, [rooms[x][y]])
                elif rooms[x][y] == -1:
                    ans[x][y] = -1
        return ans

    def dfs(self, rooms, x, y, ans, path):
        if x >= len(rooms) or x < 0:
            return sys.maxint

        if y >= len(rooms[0]) or y < 0:
            return sys.maxint

        if rooms[x][y] == -1 or rooms[x][y] == -sys.maxint:
            return sys.maxint

        if rooms[x][y] == 0:
            if path != []:
                path.pop()
            return len(path)

        path.append(rooms[x][y])

        rooms[x][y] = -rooms[x][y]
        minLen = min(self.dfs(rooms, x + 1, y, ans, path),
                     self.dfs(rooms, x - 1, y, ans, path),
                     self.dfs(rooms, x, y + 1, ans, path),
                     self.dfs(rooms, x, y - 1, ans, path)
                     )

        rooms[x][y] = -rooms[x][y]
        if path != []:
            path.pop()
        return minLen

rooms = [
    ['INF',  -1,     0,   'INF'],
    ['INF', 'INF', 'INF',  -1],
    ['INF',  -1,   'INF',  -1],
    [  0,    -1,   'INF', 'INF']
]

print Solution().wallsAndGates(rooms)