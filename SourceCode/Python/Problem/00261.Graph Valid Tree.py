'''
Level: Medium   Tag: [Union Find]

Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.


You can assume that no duplicate edges will appear in edges.

Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.


Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.


'''



'''
判断图是否是树，首先要知道一棵树有x个点，x-1条边，其次图内所有点都连通且无环

1. 判断点与边的关系
2. 将所有边都添加入并查集
3. 记录连通块的数量
4. 最后只有一个块则图是树


复杂度分析

时间复杂度O(n)
空间复杂度O(n)

'''


class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        m = len(edges)
        if n != m + 1:
            return False

        self.count = n
        self.father = {}
        # 初始化Union Find的father map
        # 让每一个节点的初始parent指向自己（自己跟自己是一个Group）
        for i in range(n):
            self.father[i] = i

        # 在循环读取edge list时，查找两个节点的parent
        for a, b in edges:
            self.union(a, b)

        if self.count == 1:
            return True
        else:
            return False

    def find(self, x):
        x2 = x
        # 如果他自己就是他那群的源頭，就回報他自己的編號
        if self.father[x] == x:
            return x

        # 找出根節點，如果x的爸爸不是自己
        # 說明他和別人一組了，找出他爸是誰
        # 且把他的爸爸也改成終極老爸(源頭)的編號
        while self.father[x] != x:
            self.father[x2] = self.father[self.father[x2]] # 路徑壓縮
            x = self.father[x]

        # # 路徑壓縮，可做可不做
        # while x2 != x:
        #     temp = self.father[x2]
        #     self.father[x2] = x
        #     x2 = temp

        return x

    def union(self, a, b):
        # 查找两个节点的parent，如果相同，说明形成了环（Cycle）
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            # 不是環，把a和b標記為同一組
            self.father[root_a] = root_b
            self.count -= 1


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
assert True == Solution().validTree(n, edges)

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
assert False == Solution().validTree(n, edges)