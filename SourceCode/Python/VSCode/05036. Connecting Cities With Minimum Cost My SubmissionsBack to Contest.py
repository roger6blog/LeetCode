'''

5036. Connecting Cities With Minimum Cost My SubmissionsBack to Contest
Difficulty: Medium
There are N cities numbered from 1 to N.

You are given conections, where each conections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

 

Example 1:



Input: N = 3, conections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:



Input: N = 4, conections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.
 

Note:

1 <= N <= 10000
1 <= conections.length <= 10000
1 <= conections[i][0], conections[i][1] <= N
0 <= conections[i][2] <= 10^5
conections[i][0] != conections[i][1]


'''
class edge(object):
    def __init__(self, u, v, c):
        self.u = u
        self.v = v
        self.c = c

class Solution(object):
    def minimumCost(self, N, conections):
        """
        :type N: int
        :type conections: List[List[int]]
        :rtype: int
        """


        def find(num, pre):
            if pre[num] == num:
                return num

            pre[num] = find(num, pre)
            return pre[num]

        def merge(u, v, pre):
            f1 = find(u, pre)
            f2 = find(v, pre)
            if f1 != f2:
                pre[f2] = f1
                return 1
            return 0
        
        pre = [-1] * 10040
        e = [edge(0,0,0)] * 10040
        # for _ in range(10040):
        #     x = edge()
        #     e.append(x)
        for i in range(N):
            pre[i] = i

        n = len(conections)

        for i in range(n):
            e[i].u = conections[i][0]
            e[i].v = conections[i][1]
            e[i].c = conections[i][2]

        e = sorted(e, key=)    
        pass

print Solution().minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]])