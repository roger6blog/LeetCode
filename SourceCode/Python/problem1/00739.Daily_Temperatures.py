'''

Given a list of daily temperatures, produce a list that,

for each day in the input, tells you how many days you would have to wait until a warmer temperature.

If there is no future day for which this is possible, put 0 instead.

For example,

given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73],

your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].

Each temperature will be an integer in the range [30, 100].


'''
import timeit
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        ans = []
        length = len(temperatures)
        tMap = {}
        for day in xrange(length - 1, -1, -1):
            warmer = []
            tMap[temperatures[day]] = day
            for t in xrange(temperatures[day] + 1, 101):
                if t in tMap:
                    warmer.append(tMap[t] - day)
            if warmer:
                ans.insert(0, min(warmer))
            else:
                ans.insert(0, 0)

        return ans



    def dailyTemperaturesStack(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        length = len(temperatures)
        ans = [0] * length
        for i in xrange(length):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                temp = stack.pop()
                ans[temp] = i - temp

            stack.append(i)

        return ans


    def dailyTemperaturesTLE(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in xrange(len(temperatures)):
            bFound = False
            for j in xrange(i, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    bFound = True
                    ans.append(j-i)
                    break
            if not bFound:
                 ans.append(0)

        return ans



start = timeit.default_timer()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print Solution().dailyTemperatures(temperatures)
end = timeit.default_timer()
print (end - start)
