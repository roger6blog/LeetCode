'''
Level: Medium Tag: [Topological Sort]

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.

The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 10^4.

Reconstruction means building a shortest common supersequence of the sequences in seqs
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it).

Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed,
because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:

Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation:
The reconstructed sequence can only be [1,2].

Example 3:

Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:

Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output:true


'''


'''
1) 建立indegree and neighbors(edges)
    两个dict来存放graph的信息,注意这里使用org的node来初始化dict
2) fill in graph的信息from seqs
    注意这里是边添加graph信息边检查, 是否出现了org里面没有的node, 如果有, 就立刻false
3) 利用queue来做topological sorting
    注意这里要用分层的BFS用来记录从定点到末端的距离
4) 最后要是唯一的topological order, 有三个条件:
    a) topological sorting所输出的数组 == org
    b) seq里面的node数目要等于org里面的node数目
    c) 顶点到末端距离 == org的长度

很容易错的点:
    1) 必须有个nodes_seqs来存储所有seqs里面出现的node
    2) 必须要检查seq里面的元素是否在org里面
    3) 用level记录距离
    4) return true的前提是三个要素


'''


from collections import deque
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):

        edges = {i: [] for i in org}
        degree = {i: 0 for i in org}
        nodes = set()

        for s in seqs:
            nodes |= set(s)
            for i in range(len(s)-1):
                edges[s[i+1]].append(s[i])
                degree[s[i]] += 1


        queue = deque()
        level = 0

        for o in org:
            if degree[o] == 0:
                queue.append(o)

        # 因為是唯一序列，queue裡應該只有一個唯一起點
        if len(queue) > 1:
            return False


        ans = []
        # BFS
        while queue:
            now_pos = queue.popleft()
            ans.append(now_pos)
            level += 1
            for next_pos in edges[now_pos]:
                degree[next_pos] -= 1
                if degree[next_pos] == 0:
                    queue.append(next_pos)

        return level == len(org) and ans[::-1] == org and len(nodes) == len(org)


org = [4,1,5,2,6,3]
seqs = [[5,2,6,3],[4,1,5,2]]
assert True == Solution().sequenceReconstruction(org, seqs)

org = [1,2,3]
seqs = [[1,2],[1,3],[2,3]]
assert True == Solution().sequenceReconstruction(org, seqs)

org = [1,2,3]
seqs = [[1,2],[1,3]]
assert False == Solution().sequenceReconstruction(org, seqs)