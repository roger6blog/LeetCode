'''
Level:  Tag: [Graph]

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed).

For example, the first node with val == 1, the second node with val == 2, and so on.

The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.

Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.

You must return the copy of the given node as a reference to the cloned graph.



Example 1:

"../../../Material/133_clone_graph_question.png"

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.


Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.












===========   Old Description     =============






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
