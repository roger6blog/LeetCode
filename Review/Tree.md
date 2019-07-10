

# 樹
## 樹的概念
樹(tree)是一種能夠分層存儲數據的重要數據結構，樹中的每個元素被稱為樹的節點，  
每個節點有若幹個指針指向子節點。  
從節點的角度來看，樹是由唯一的起始節點引出的節點集合。  
這個起始結點稱為根(root)。樹中節點的子樹數目稱為節點的度(degree)。  
在面試中，關於樹的面試問題非常常見，尤其是關於二叉樹(binary tree)、  
二叉搜索樹(Binary Search Tree, BST)的問題。

所謂的二叉樹，是指對於樹中的每個節點而言，至多有左右兩個子節點，  
即任意節點的度小於等於2。而廣義的樹則沒有如上限制。二叉樹是最常見的樹形結構。  
二分查找樹是二叉樹的一種特例。  
對於二分查找樹的任意節點，  
該節點存儲的數值一定比左子樹的所有節點的值大比右子樹的所有節點的值小    
(與之完全對稱的情況也是有效的：  
即該節點存儲的數值一定比左子樹的所有節點的值小比右子樹的所有節點的值大)。

基於這個特性，二分查找樹通常被用於維護有序數據。  
二分查找樹查找、刪除、插入的效率都會於一般的線性數據結構。  
事實上，對於二分查找樹的操作相當於執行二分搜索，其執行效率與樹的高度(depth)有關，  
檢索任意數據的比較次數不會多於樹的高度。  
這裏需要引入高度的概念：  
對一棵樹而言，從根節點到某個節點的路徑長度稱為該節點的層數(level)，  
根節點為第0層，非根節點的層數是其父節點的層數加1。  
樹的高度定義為該樹中層數最大的葉節點的層數加1，  
即相當於於從根節點到葉節點的最長路徑加1。  
由此，對於n個數據，二分查找樹應該以“盡可能小的高度存儲所有數據。  
由於二叉樹第L層至多可以存儲 2L 個節點，故樹的高度應在logn量級，  
因此，二分查找樹的搜索效率為O(logn)。

直觀上看，盡可能地把二分查找樹的每一層“塞滿”數據可以使得搜索效率最高，  
但考慮到每次插入刪除都需要維護二分查找樹的性質，要實現這點並不容易。  
特別地，當二分查找樹退化為一個由小到大排列的單鏈表(每個節點只有右孩子)，  
其搜索效率變為O(n)。為了解決這樣的問題，人們引入平衡二叉樹的概念。  
所謂平衡二叉樹，是指一棵樹的左右兩個子樹的高度差的絕對值不超過1，  
並且左右兩個子樹都是一棵平衡二叉樹。  
通過恰當的構造與調整，平衡二叉樹能夠保證每次插入刪除之後都保持平衡性。  
平衡二叉樹的具體實現算法包括AVL算法和紅黑算法等。  
由於平衡二叉樹的實現比較覆雜，故一般面試官只會問些概念性的問題。

## 樹型的概念
滿二叉樹(full binary tree)：  
如果一棵二叉樹的任何結點，或者是葉節點，或者左右子樹都存在，  
則這棵二叉樹稱作滿二叉樹。

完全二叉樹(complete binary tree)：  
如果一棵二叉樹最多只有最下面的兩層節點度數可以小於2，  
並且最下面一層的節點都集中在該層最左邊的連續位置上，則此二叉樹稱作完全二叉樹。

## 二叉樹的遍歷
二叉樹的常見操作包括樹的遍歷，即以一種特定的規律訪問樹中的所有節點。  
常見的遍歷方式包括：

* 前序遍歷(Pre-order traversal)：訪問根結點；按前序遍歷左子樹；按前序遍歷右子樹。
* 中序遍歷(In-order traversal)：按中序遍歷左子樹；訪問根結點；按中序遍歷右子樹。特別地，對於二分查找樹而言，中序遍歷可以獲得一個由小到大或者由大到小的有序序列。
* 後續遍歷(Post-order traversal)：按後序遍歷左子樹；按後序遍歷右子樹；訪問根結點。


以上三種遍歷方式都是深度優先搜索算法(depth-first search)。  
深度優先算法最自然的實現方式是通過遞歸實現，  
事實上，大部分樹相關的面試問題都可以優先考慮遞歸。  
此外，另一個值得注意的要點是：  
深度優先的算法往往都可以通過使用棧數據結構將遞歸化為非遞歸實現。  
這裏利用了棧先進後出的特性，其數據的進出順序與遞歸順序一致。

* 層次遍歷(Level traversal)：首先訪問第0層，也就是根結點所在的層；當第i層的所有結點訪問完之後，再從左至右依次訪問第i+1層的各個結點。層次遍歷屬於廣度優先搜索算法(breadth-first search)。廣度優先算法往往通過隊列數據結構實現。

## Trie
字典樹(trie or prefix tree)是一個26叉樹，  
用於在一個集合中檢索一個字符串，或者字符串前綴。  
字典樹的每個節點有一個指針數組代表其所有子樹，其本質上是一個哈希表，  
因為子樹所在的位置(index)本身，就代表了節點對應的字母。  
節點與每個兄弟具有相同的前綴，這就是trie也被稱為prefix tree的原因。

假設我們要存儲如下名字，年齡：
```
Amy 12
Ann 18
Bob 30
```
則構成的字典樹如下：
```
.                 root: level 0
a---------b       level 1
|         |  
m---n     o       level 2
|   |     |
y   n     b       level 3
|   |     |
12  18   30       level 4
```
由於Amy和Ann共享前綴a，故第二個字母m和n構成兄弟關係。

字典樹以及字典樹節點的原型：
```python
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.isWord = False
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """    
```    
字典樹的基本功能如下：

1) ```def insert(self, word):```

添加一個鍵:值對。  
添加時從根節點出發，如果在第i層找到了字符串的第i個字母，  
則沿該節點方向下降一層(注意，如果下一層存儲的是數據，則視為沒有找到)。  
否則，將第i個字母作為新的兄弟插入到第i層。將鍵插入完成後插入值節點。  

2) ```def search(self, word):```

查找某個鍵是否存在，並返回值。  
從根節點出發，在第i層尋找字符串中第i個字母是否存在。  
如果是，沿著該節點方向下降一層；否則，返回false。

3) ```def startsWith(self, prefix):```

找出任何符合指定開頭字串的數據。

  
對於樹的性質，一般全局解依賴於局部解。    
通常可以用DFS來判斷子問題的解，然後綜合得到當前的全局結論。  

值得注意的是，當我們在傳遞節點指針的時候，其實其代表的不只是這個節點本身，  
而是指對整個子樹進行操作。只要每次遞歸的操作對象的結構一致，  
我們就可以選擇Divide and Conquer  
(事實上對於樹和圖總是如此，因為subgraph和subtree仍然是graph和tree結構)。  
實現函式遞歸的步驟是：  
首先設置函式出口，就此類問題而言，遞歸出口往往是node == NULL。  
其次，在構造遞歸的時候，不妨將遞歸調用自身的部分視為黑盒，  
並想象它能夠完整解決子問題。以二叉樹的中序遍歷為例，函式的實現為：
```python
def printTreeInorder(self):
    if self.left:
        self.left.printTreeInorder()
    print(self.val),
    if self.right:
        self.right.printTreeInorder()
```        
想象遞歸調用的部分  
self.left.printTreeInorder()／self.right.printTreeInorder()  
能夠完整地中序遍歷一棵子樹，那麽根據中序遍歷“按中序遍歷左子樹；  
訪問根結點；按中序遍歷右子樹”的定義，寫出上述實現就顯得很自然了。  

### DFS 處理樹的問題
有一類關於樹的問題是，要求找出一條滿足特定條件的路徑。  
對於這類問題，通常都是傳入一個List記錄當前走過的路徑  
(為盡可能模版化，統一記為path)。  
還需要傳入另一個List引用記錄所有符合條件的path  
(為盡可能模版化，統一記為result)。  
注意， result相當於一個全局變數，或者就開辟一個獨立於函式的成員變數。　　
當然，那個特定條件，也是函式的一個輸入變數。　　

在解答此類問題的時候，通常都采用DFS來訪問，　　
利用回溯思想，直到無法繼續訪問再返回。　　
值得注意的是，path需要在返回之前消除之前所做的影響(回溯)。　　
因為List型態相當於把path也看作全局變數，對path的任何操作都會影響其他遞歸狀態，  
這樣的好處是可以減小空間開銷。

### 樹和其他數據結構的相互轉換
這類題目要求將樹的結構轉化成其他數據結構，  
例如鏈表、數組等，或者反之，從數組等結構構成一棵樹。  
前者通常是通過樹的遍歷，合並局部解來得到全局解，而後者則可以利用D&C的策略，  
遞歸將數據結構的兩部分分別轉換成子樹，再合併。

### 尋找特定節點
此類題目通常會傳入一個當前節點，要求找到與此節點具有一定關係的特定節點：  
例如前驅、後繼、左／右兄弟等。

對於這類題目，首先可以了解一下常見特定節點的定義及性質。  
在存在指向父節點指針的情況下，通常可以由當前節點出發，向上倒推解決。  
如果節點沒有父節點指針，一般需要從根節點出發向下搜索，搜索的過程就是DFS。

***
  
  
  
### [00208.Implement_Trie_(Prefix_Tree)](../SourceCode/Python/Problem/00208.Implement_Trie_(Prefix_Tree).py) Level: Medium Tags: [Tree]
  
Time:  O(n), per operation
Space: O(1)
思路:本題要求你實作一個字典樹(Trie)的insert, search和startWith  
在此之前你必須先了解字典樹是什麼  
  
![一個保存了8個Key的trie結構，"A", "to", "tea", "ted", "ten", "i", "in", and "inn".](Res/Problem/001200px-Trie_example.svg.png)
  
簡單來說就是一個方便搜尋同樣Prefix單字的樹  
有同樣prefix字的單字會被插到同一條Trie  
roo節點通常為空，底下有a~z 26個子Trie
好處是用空間換取時間  
搜尋速度比為最佳化的Hash快，只要O(n)    
壞處就是浪費空間和比不上最佳化的Hash  
  
  
***
 
### [00212.Word_Search_II](../../SourceCode/Python/Problem/00212.Word_Search_II.py) Level: Hard Tags: [DFS, Tree]
  
思路: 題目給了你一個2D陣列，要求你找出給予的單字中是能讓這陣列中的相鄰字元成為該單字  
例如  
words = ["oath","pea","eat","rain"]  
board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
因為e, a, t能在陣列中找出相鄰的字元    
看到2D陣列的traversal便能很自然想到用DFS或BFS解題  
而題目限制字元是a~z的組合也暗示了我們能用 Tries來拆解單字和搜尋  
因為自己寫的code一直敗在其中一個test case  
這裡附上能被Accept的版本  
[00212.Word_Search_II_Accept](../../SourceCode/Python/Problem/00212.Word_Search_II_Accept.py)

***
  
### [00298.[Locked]Binary_Tree_Longest_Consecutive_Sequence](../../SourceCode/Python/Problem/00298.[Locked]Binary_Tree_Longest_Consecutive_Sequence.py) Level: Medium Tags: [Tree]
    
Time:  O(n)  
Space: O(h), h is height of tree  
    
思路:給你一個二元樹，要你找出有連續遞增數字的節點數量  
例如以下二元樹:  
```
   1
    \
     3
    / \
   2   4
        \
         5
```
  
他的最長順序就是3-4-5，所以總和為3  
做法和[00687.Longest_Univalue_Path](../../SourceCode/Python/Problem/00687.Longest_Univalue_Path.py)  很像  
只差在判斷條件不同  
不斷遞迴去尋找下一個符合條件的子節點  
最後返回左右子樹的最大值  
具體解法可參考687題  
    
  
***
  
### [00686.Repeated_String_Match](../../SourceCode/Python/Problem/00686.Repeated_String_Match.py) Level: Easy Tags: [String]
      
Time:  O(n + m)  
Space: O(1)    
  
思路:給你兩個字串A和B，通常A有可能為B的子字串  
求A字串要重複幾次才能讓B成為A的子字串  
一開始可以用暴力解  
但後來的測試項目越來越刁鑽，最後敗在A="a"，B="a"x10000的測試項目  
重點在於測試A的次數，只要A字串長度比B字串長後還是沒能找到答案  
那麼再繼續循環也沒用  
至於重複次數可以用兩個字串的長度相除來取得  
不過Python的除法會向下取整，所以多加3次 (經驗得來)  
```python
na = len(A)
nb = len(B)
times = nb / na + 3
``` 
這個times就是for迴圈的上限
  
  
***
  
### [00687.Longest_Univalue_Path](../../SourceCode/Python/Problem/00687.Longest_Univalue_Path.py) Level: Easy Tags: [Tree]
       
Time:  O(n)  
Space: O(h), h is height of tree  
  
思路:給你一個BinaryTree  
要你找出同值節點所組成的最長路徑  
這路徑不一定要從root開始  
例如  
```
              1
             / \
            4   5
           / \   \
          4   4   5
```  
他的最長路徑為4-4-4組成的 2   
我們可以從root開始，統計到每個同值左右子節點的路徑  
如果不同值就返回，反之則繼續遞迴找下去
```python
max(self.longestUnivaluePath(root.left), \
self.longestUnivaluePath(root.right) )
```
  
因為可以不經過root，所以還要考慮他底下兩個子樹符合條件的路徑總和
```python
self.longestPath(root.left, root.value) + self.longestPath(root.right, root.value)
```
兩個條件合在一起就是  
```python
return max(self.longestPath(root.left, root.value) + self.longestPath(root.right, root.value), \
           self.longestUnivaluePath(root.left), \
           self.longestUnivaluePath(root.right)
           )
```
  
***

