
# 圖
圖(Graph)是節點集合的一個拓撲結構，節點之間通過邊相連。  
圖分為有向圖和無向圖。有向圖的邊具有指向性，即AB僅表示由A到B的路徑，  
但並不意味著B可以連到A。與之對應地，無向圖的每條邊都表示一條雙向路徑。

圖的數據表示方式也分為兩種，  
即鄰接表(adjacency list)和鄰接矩陣(adjacency matrix)。  
對於節點A，A的鄰接表將與A之間相連的所有節點以鏈表的形勢存儲起來，  
節點A為鏈表的頭節點。這樣，對於有V個節點的圖而言，鄰接表表示法包含V個鏈表。  
因此，鏈接表需要的空間複雜度為O(V+E)。  
鄰接表適用於邊數不多的稀疏圖。但是，如果要確定圖中邊(u, v)是否存在，  
則只能在節點u對應的鄰接表中以O(E)複雜度線性搜索。

對於有V個節點的圖而言，鄰接矩陣用V*V的二維矩陣形式表示一個圖。  
矩陣中的元素Aij表示節點i到節點j之間是否直接有邊相連。  
若有，則Aij數值為該邊的權值，否則Aij數值為0。  
特別地，對於無向圖，由於邊的雙向性，其鄰接矩陣的轉置矩陣為其本身。  
鄰接矩陣的空間複雜度為O(V2 )，適用於邊較為密集的圖。  
鄰接矩陣在檢索兩個節點之間是否有邊相連這樣一個需求上，具有優勢。  

## 图的访问
关于图的问题一般有两类。  
一类是前面提到的关于图的基本问题，例如图的遍历、最短路径、可达性等；  
另一类是将问题转化成图，再通过图的遍历解决问题。  
第二类问题有一定的难度，但也有一些规律可循：如果题目有一个起始点和一个终止点，  
可以考虑看成图的最短路径问题。

## 圖的遍歷
對於圖的遍歷(Graph Transversal)類似於樹的遍歷  
(事實上，樹可以看成是圖的一個特例)，也分為廣度優先搜索和深度優先搜索。  
算法描述如下：

### 廣度優先
對於某個節點，廣度優先會先訪問其所有鄰近節點，再訪問其他節點。  
即，對於任意節點，算法首先發現距離為d的節點，當所有距離為d的節點都被訪問後，  
算法才會訪問距離為d+1的節點。  
廣度優先算法將每個節點著色為白，灰或黑，白色表示未被發現，  
灰色表示被發現，黑色表示已訪問。  
算法利用先進先出隊列來管理所有灰色節點。  
一句話總結，廣度優先算法先訪問當前節點，  
一旦發現未被訪問的鄰近節點，推入隊列，以待訪問。

Python程式碼如下：  
```python
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
```
### 深度優先
深度優先算法盡可能“深”地搜索一個圖。  
對於某個節點v，如果它有未搜索的邊，則沿著這條邊繼續搜索下去，  
直到該路徑無法發現新的節點，回溯回節點v，繼續搜索它的下一條邊。  
深度優先算法也通過著色標記節點，  
白色表示未被發現，灰色表示被發現，黑色表示已訪問。  
算法通過遞歸實現先進後出。  
一句話總結，深度優先算法一旦發現沒被訪問過的鄰近節點，則立刻遞歸訪問它，  
直到所有鄰近節點都被訪問過了，最後訪問自己。

Python程式碼如下：
```python
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
```  
## 單源最短路徑問題  

對於每條邊都有一個權值的圖來說，  
單源最短路徑問題是指從某個節點出發，到其他節點的最短距離。  
該問題的常見算法有Bellman-Ford和Dijkstra算法。  
前者適用於一般情況(包括存在負權值的情況，但不存在從源點可達的負權值回路)，  
後者僅適用於均為非負權值邊的情況。  
Dijkstra的運行時間可以小於Bellman-Ford。  

特別地，如果每條邊權值相同(無權圖)，  
由於從源開始訪問圖遇到節點的最小深度就等於到該節點的最短路徑，  
因此 Priority Queue就退化成Queue，Dijkstra算法就退化成BFS。

Dijkstra的核心在於，構造一個節點集合S，對於S中的每一個節點，  
源點到該節點的最短距離已經確定。  
進一步地，對於不在S中的節點，  
我們總是選擇其中到源點最近的節點，將它加入S，並且更新其鄰近節點到源點的距離。  
算法實現時需要依賴優先隊列。  
一句話總結，Dijkstra算法利用貪心的思想，在剩下的節點中選取離源點最近的那個加入集合，  
並且更新其鄰近節點到源點的距離，直至所有節點都被加入集合。  
關於Dijkstra算法的正確性分析，可以使用數學歸納法證明，詳見《算法導論》第24章，單源最短路徑。 給出偽代碼如下：
```python
def dijkstra(edges, from_node, to_node):
    len_shortest_path = -1
    ret_path = []
    length, path_queue = dijkstra_raw(edges, from_node, to_node)
    if len(path_queue) > 0:
        len_shortest_path = length  ## 1. Get the length firstly;
        ## 2. Decompose the path_queue, to get the passing nodes in the shortest path.
        left = path_queue[0]
        ret_path.append(left)  ## 2.1 Record the destination node firstly;
        right = path_queue[1]
        while len(right) > 0:
            left = right[0]
            ret_path.append(left)  ## 2.2 Record other nodes, till the source-node.
            right = right[1]
        ret_path.reverse()  ## 3. Reverse the list finally, to make it be normal sequence.
    return len_shortest_path, ret_path
```    
## 任意兩點之間的最短距離
另一個關於圖常見的算法是，  
如何獲得任意兩點之間的最短距離(All-pairs shortest paths)。  
直觀的想法是，可以對於每個節點運行Dijkstra算法，該方法可行，  
但更適合的算法是Floyd-Warshall算法。

Floyd算法的核心是動態編程，利用二維矩陣存儲i，j之間的最短距離，  
矩陣的初始值為i，j之間的權值，如果i，j不直接相連，則值為正無窮。  
動態編程的遞歸式為：  
```
d(k)ij = min(d(k-1)ij, d(k-1)ik+ d(k-1)kj) (1<= k <= n)
```  
直觀上理解，對於第k次更新，  
我們比較從i到j只經過節點編號小於k的中間節點(d(k-1)ij)，  
和從i到k，從k到j的距離之和(d(k-1)ik+ d(k-1)kj)。  
Floyd算法的複雜度是O(n^3)。Python程式碼如下:
```python
def _init_Floyd(self):
    for k in range(self.node_length):
        for i in range(self.node_length):
            for j in range(self.node_length):
                tmp = self.node_map[i][k] + self.node_map[k][j]
                if self.node_map[i][j] > tmp:
                    self.node_map[i][j] = tmp
                    self.path_map[i][j] = self.path_map[i][k]
```      
  
                
***
  
  
  
### [133.Clone_Graph](../SourceCode/Python/133.Clone_Graph.py) Level: Medium Tags: [Graph, Sequence DFS]
  
思路:用DFS遍歷所有節點
差別在於接觸到相鄰節點時要做複製的動作
  
***
