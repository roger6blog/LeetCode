'''

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order.

All of the tickets belong to a man who departs from JFK.

Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries,

you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

All airports are represented by three capital letters (IATA code).

You may assume all tickets form at least one valid itinerary.

Example 1:

Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
But it is larger in lexical order.


'''

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ans = []
        route = {}
        tickets.sort()
        for flight in tickets:
            if flight[0] in route:
                route[flight[0]].append(flight[1])
            else:
                route[flight[0]] = [flight[1]]

        ans = self.dfs(route, ans, 'JFK', tickets)
        return ans


    def dfs(self, travel, ans, spot, tickets):
        if len(ans) == len(tickets) + 1:
            return ans
        if travel == {}:
            return

        if spot not in travel:
            return

        for dst in sorted(travel[spot]):
            ans.append(spot)
            if len(travel) == 1:
                ans.append(travel[spot][0])
            print ans
            key = spot
            travel[spot].remove(dst)

            if len(travel[spot]) == 0:
                travel.pop(spot)

            valid = self.dfs(travel, ans, dst, tickets)
            if valid:
                return valid
            ans.pop()
            if key not in travel:
                travel[key] = [dst]
            else:
                travel[key].append(dst)


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets3 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# print Solution().findItinerary(tickets)
# print Solution().findItinerary(tickets2)
print Solution().findItinerary(tickets3)
