'''

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


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print Solution().calcEquation(equations, values, queries)