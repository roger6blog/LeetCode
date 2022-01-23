'''
Level: Medium  Tag: [Union Find]

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),

write a function to find the number of connected components in an undirected graph

Example 1:

     0          3

     |          |

     1 --- 2    4

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:

     0           4

     |           |

     1 --- 2 --- 3

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

'''

class Solution:
    def countComponents(self, n, edges):
        self.count = n  # 一開始預期是分成n塊
        self.father = {}
        for i in range(n):
            self.father[i] = i

        for a, b in edges:
            self.union(a, b)

        print(self.count)
        return self.count

    def find(self, x):
        x2 = x
        if self.father[x] == x:
            return x

        while self.father[x] != x:
            self.father[x2] = self.father[self.father[x2]] # 路徑壓縮
            x = self.father[x]

        return x

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.count -= 1
            self.father[root_a] = root_b

n = 5
edges = [[0, 1], [1, 2], [3, 4]]
Solution().countComponents(n, edges)

n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
Solution().countComponents(n, edges)