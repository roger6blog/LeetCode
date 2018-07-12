'''

Clone an undirected graph.
Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and ,
as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes,
and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself),
thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/


'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def __init__(self):
        self.visit = {}
        
    def cloneGraph(self, node):
        if not node:
            return
        if node.label in self.visit:
            return self.visit[node.label]
        
        # Clone node
        cloneGraph = UndirectedGraphNode(node.label)
        self.visit[node.label] = cloneGraph
        
        for neighbour in node.neighbors:
            cloneGraph.neighbors.append(self.cloneGraph(neighbour))
            
        return cloneGraph


sol = Solution()
node1 = UndirectedGraphNode(0)
node2 = UndirectedGraphNode(1)
node3 = UndirectedGraphNode(2)
node1.neighbors = [node2, node3]
node2.neighbors = [node3]
node3.neighbors = [node3]

a = sol.cloneGraph(node1)
print a
