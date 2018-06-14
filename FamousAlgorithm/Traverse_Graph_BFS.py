# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}


# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of nodes to be checked
    queue = []
    # keep track of all visited nodes
    visited = []
    queue.append(start)

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop()
        neighbour = graph[node]
        if node not in visited:
            # add node to list of checked nodes
            visited.append(node)
            
            # add neighbours of node to queue
            for item in neighbour:
                queue.append(item)
    print visited

bfs_connected_component(graph,'A') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
