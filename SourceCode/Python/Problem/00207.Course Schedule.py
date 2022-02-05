'''
Level: Medium   Tag: [Topological Sort]

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.

You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished
course 1. So it is impossible.


Constraints:

1 <= numCourses <= 10^5
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

'''




'''
拓扑排序步骤:

建图并记录所有节点的入度。
将所有入度为0的节点加入队列。
取出队首的元素now，将其加入拓扑序列。
访问所有now的邻接点nxt，将nxt的入度减1，当减到0后，将nxt加入队列。
重复步骤3、4，直到队列为空。
如果拓扑序列个数等于节点数，代表该有向图无环，且存在拓扑序。

'''


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        edges = {i: [] for i in range(numCourses)}
        degrees = {i: 0 for i in range(numCourses)}

        # 建圖
        for course, pre in prerequisites:
            edges[pre].append(course)
            degrees[course] += 1

        queue = deque()
        choose = 0

        # 將不需先修的課程編號放入queue
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        # 將每條鄰邊刪去，如果入度降為零的話，再放入queue中
        while queue:
            now_pos = queue.popleft()
            choose += 1
            for next_pos in edges[now_pos]:
                degrees[next_pos] -= 1
                if degrees[next_pos] == 0:
                    queue.append(next_pos)

        print(choose)
        return choose == numCourses

numCourses = 2
prerequisites = [[1,0],[0,1]]
assert False == Solution().canFinish(numCourses, prerequisites)


numCourses = 2
prerequisites = [[1,0]]
assert True == Solution().canFinish(numCourses, prerequisites)