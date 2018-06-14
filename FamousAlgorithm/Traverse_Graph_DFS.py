
graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}


def dfs(graph, node, visited):
  '''
  visited: traversed node
  node: node which would visit
  graph: whole graph
  return: the sequence of traversed graph
  '''
  if node not in visited:
        visited.append(node)
        for item in graph[node]:
            dfs(graph, item, visited)
  return visited
  
result = dfs(graph, 'A', [])
print result
