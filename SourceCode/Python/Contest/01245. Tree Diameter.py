'''

1245. Tree Diameter
Medium
211FavoriteShare
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.

Each node has labels in the set {0, 1, ..., edges.length}.



Example 1:

Input: edges = [[0,1],[0,2]]
Output: 2
Explanation:
A longest path of the tree is the path 1 - 0 - 2.
Example 2:

Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation:
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.


Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.



'''

from collections import defaultdict


class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        self.res = 0

        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def bfs(node, parent):
            print(node, parent)
            if len(graph[node]) == 1:
                if graph[node][0] == parent:
                    if 1 > self.res:
                        self.res = 1
                    return 1
                else:
                    t = 1 + bfs(graph[node][0], node)
                    if t > self.res:
                        self.res = t
                    return t
            else:
                res = []
                for i in graph[node]:
                    if i == parent:
                        continue
                    else:
                        res.append(bfs(i, node))
                print(res)
                if len(res) == 1:
                    if res[0] > self.res:
                        self.res = res[0] + 1
                    return res[0] + 1
                else:
                    res.sort()
                    if res[-1] + res[-2] > self.res:
                        self.res = res[-1] + res[-2]
                    return 1 + res[-1]

        bfs(0, None)
        return self.res