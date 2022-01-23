'''
Level: Medium   Tag: [Graph], [Topological Sort]

A tree is an undirected graph in which any two vertices are connected by exactly one path.

In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1,
and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between
the two nodes ai and bi in the tree, you can choose any node of the tree as the root.
When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.



Example 1:

"../../../Material/e1.jpg"

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:

"../../../Material/e2.jpg"

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]


Constraints:

1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.



'''









'''
无向图的拓扑排序。 在有向图中，最小入度是0. 这里最小入度是1， 因为双向关系。

想法是一层一层的剥掉叶子节点。 最后剩下一个或者两个节点就是答案。 为什么是最后一个或者两个?

举个例子，1-2-3， 肯定是 2 为中心，树高最小 1-2-3-4， 2或者3 为中心都得到相同的树高。

这里用算法班处理图遍历的三部曲模板 1. build graph 2. get indegrees 3. BFS

当我们遍历的时候，最后一层要么剩下两个点，要么剩下一个点。 答案必然是其中之一。
'''





class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            return [i for i in range(n)]

        from collections import deque

        ed = {i:[] for i in range(n)}
        degrees = [0] * n

        for node, neighbor in edges:
            ed[neighbor].append(node)
            ed[node].append(neighbor)
            degrees[node] += 1
            degrees[neighbor] += 1

        # 找出一個邊的點
        queue = deque()
        for i in range(n):
            if len(ed[i]) == 1:
                queue.append(i)

        # BFS
        while queue:
            res = list(queue)
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                for neighbor in ed[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)


        print(res)

        return res

