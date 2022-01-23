'''
Level: Medium  Tag: [Graph], [DFS]


You are given an array of variable pairs equations and an array of real numbers values,

where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].

Each Ai or Bi is a string that represents a single variable.

You are also given some queries,

where queries[j] = [Cj, Dj] represents the j(th) query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid.

You may assume that evaluating the queries will not result in division by zero
and that there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.



======= Old Description ========




Equations are given in the format A / B = k,

where A and B are variables represented as strings,

and k is a real number (floating point number).

Given some queries, return the answers.

If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations,
vector<double>& values, vector<pair<string, string>> queries ,
where equations.size() == values.size(), and the values are positive.
This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid.
You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


'''





class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dicCalcMap = {}


        for i in xrange(len(equations)):
            if equations[i][0] in dicCalcMap:
                dicCalcMap[equations[i][0]][equations[i][1]] =  values[i]
            else:
                dicCalcMap[equations[i][0]] = {equations[i][1]: values[i]}

            if equations[i][1] in dicCalcMap:
                dicCalcMap[equations[i][1]][equations[i][0]] = 1.0 / values[i]
            else:
                dicCalcMap[equations[i][1]] = {equations[i][0]: 1.0 / values[i]}

        for e1 in dicCalcMap:
            dicCalcMap[e1][e1] = 1.0
            for e2 in dicCalcMap:
                for e3 in dicCalcMap:
                    try:
                        if dicCalcMap[e2][e1] and dicCalcMap[e1][e3]:
                            dicCalcMap[e2][e3] = dicCalcMap[e2][e1] * dicCalcMap[e1][e3]
                    except KeyError:
                        pass

        ans = []
        for e1, e2 in queries:
            try:
                if dicCalcMap[e1][e2]:
                    ans.append(dicCalcMap[e1][e2])
                else:
                    ans.append(-1.0)
            except KeyError:
                ans.append(-1.0)

        return ans


    '''
    先建好對應方程式關係的圖
    然後用DF來traversal能不能透過鄰接的點抵達目標
    可以的話填入經過時計算的答案
    '''


    def calcEquation2(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        calc_map = defaultdict(dict)

        # Build graph
        for i in range(len(equations)):
            calc_map[equations[i][0]][equations[i][1]] = values[i]
            calc_map[equations[i][0]][equations[i][0]] = 1.0
            calc_map[equations[i][1]][equations[i][1]] = 1.0
            calc_map[equations[i][1]][equations[i][0]] = 1.0 / values[i]

        ans = [-1.0] * len(queries)

        def dfs(start, target, res, index, visit):
            for neighbor, value in calc_map[start].items():
                if neighbor == target:
                    ans[index] = res * value
                    return

                if neighbor not in visit:
                    res *= value
                    visit.add(neighbor)
                    dfs(neighbor, target, res, index, visit)
                    visit.remove(neighbor)
                    res /= value


        for i, query in enumerate(queries):
            if query[0] not in calc_map or query[1] not in calc_map:
                continue
            dfs(query[0], query[1], 1, i, set(query[0]))


        print(ans)

        return ans





equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(Solution().calcEquation(equations, values, queries))
print(Solution().calcEquation2(equations, values, queries))