

***
  
  
  
### [208.Implement_Trie_(Prefix_Tree)](../SourceCode/Python/208.Implement_Trie_(Prefix_Tree).py) Level: Medium Tags: []
  
Time:  O(n), per operation
Space: O(1)
思路:本題要求你實作一個字典樹(Trie)的insert, search和startWith  
在此之前你必須先了解字典樹是什麼  
  
![一個保存了8個Key的trie結構，"A", "to", "tea", "ted", "ten", "i", "in", and "inn".](Res/1200px-Trie_example.svg.png)
  
簡單來說就是一個方便搜尋同樣Prefix單字的樹  
有同樣prefix字的單字會被插到同一條Trie  
roo節點通常為空，底下有a~z 26個子Trie
好處是用空間換取時間  
搜尋速度比為最佳化的Hash快，只要O(n)    
壞處就是浪費空間和比不上最佳化的Hash  
  
  
***
 
### [212.Word_Search_II](../../SourceCode/Python/212.Word_Search_II.py) Level: Hard Tags: [DFS, Tree]
  
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
[212.Word_Search_II_Accept](../../SourceCode/Python/212.Word_Search_II_Accept.py)

***
