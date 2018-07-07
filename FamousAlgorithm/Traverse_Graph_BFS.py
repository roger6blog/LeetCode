# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']
         }

graph2 = {'A':['B','C'],
          'B':['D','E'],
          'C':['D','E'],
          'D':['E'],
          'E':['A']
          }




def bfs(graph, start, path=[]):
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in path:
            # add node to list of checked nodes
            path = path + [node]
            # add neighbours of node to queue
            queue = queue + graph[node]

    return path

print bfs(graph, 'A') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
print bfs(graph2, 'A') # returns ['A', 'B', 'C', 'D', 'E']